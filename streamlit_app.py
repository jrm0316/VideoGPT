import streamlit as st
import os

import streamlit.components.v1 as components
from youtube_loader import baixar_audio_youtube
from audio_loader import carregar_audio
from rag import (
    gerar_embeddings,
    criar_indice,
    buscar
)

from llm import (
    responder,
    resumir_video,
    extrair_topicos
)
from memory import adicionar_interacao, obter_historico


# =========================
# CONFIG
# =========================

st.set_page_config(page_title="Chat com Vídeos")

st.title("Chat com Vídeos usando RAG")


# =========================
# UPLOAD
# =========================
youtube_url = st.text_input(
    "Ou cole uma URL do YouTube"
)

uploaded_file = st.file_uploader(
    "Envie um vídeo ou áudio",
    type=["mp4", "mp3", "wav"]
)


# =========================
# PROCESSAMENTO
# =========================

if uploaded_file or youtube_url:

    os.makedirs("temp", exist_ok=True)

    # =========================
    # YOUTUBE
    # =========================

    if youtube_url:

        st.info("📥 Baixando áudio do YouTube...")

        caminho_arquivo = baixar_audio_youtube(
            youtube_url
        )
        st.session_state["video_path"] = caminho_arquivo
        st.success("Áudio baixado!")

    # =========================
    # UPLOAD
    # =========================

    else:

        caminho_arquivo = f"temp/{uploaded_file.name}"

        with open(caminho_arquivo, "wb") as f:

            f.write(uploaded_file.read())

        st.success("Arquivo enviado!")
        st.session_state["video_path"] = caminho_arquivo

    st.success("Arquivo enviado com sucesso!")


    if st.button("⚙️ Processar"):

        with st.spinner("🎤 Transcrevendo áudio..."):

            textos = carregar_audio(caminho_arquivo)

        textos_str = [t["texto"] for t in textos]

        with st.spinner("🧠 Gerando embeddings..."):

            embeddings = gerar_embeddings(textos_str)

        with st.spinner("📦 Criando índice FAISS..."):

            index = criar_indice(embeddings)

        st.session_state["textos"] = textos
        st.session_state["index"] = index

        st.success("Vídeo processado!")


# =========================
# CHAT
# =========================

if "index" in st.session_state:
    video_path = st.session_state["video_path"]

    with open(video_path, "rb") as video_file:

        video_bytes = video_file.read()

    st.subheader("🎥 Vídeo")

# =========================
# VIDEO PLAYER
# =========================

    if video_bytes:

        import base64

        video_base64 = base64.b64encode(
            video_bytes
        ).decode()

        file_extension = video_path.split(".")[-1]

        media_type = {
            "mp4": "video/mp4",
            "mp3": "audio/mpeg",
            "wav": "audio/wav"
        }.get(file_extension, "video/mp4")

        video_html = f"""
        <video
            id="video-player"
            width="100%"
            height="500"
            controls
        >
            <source
                src="data:{media_type};base64,{video_base64}"
                type="{media_type}"
            >
        </video>
        """

        components.html(
            video_html,
            height=520,
        )

    else:

        st.error("Erro ao carregar vídeo")

    st.subheader("📄 Análise do Vídeo")

    st.subheader("📚 Tópicos Principais")

    # =========================
    # TÓPICOS
    # =========================

    if st.button("📚 Tópicos principais"):

        contexto_completo = "\n".join([
            t["texto"]
            for t in st.session_state["textos"]
        ])

        with st.spinner("🧠 Analisando tópicos..."):

            topicos = extrair_topicos(contexto_completo)

        st.subheader("📚 Principais tópicos")

        st.write(topicos)
    pergunta = st.text_input("💬 Faça uma pergunta sobre o vídeo")

    if pergunta:

        resultados = buscar(
            pergunta,
            st.session_state["textos"],
            st.session_state["index"]
        )

        contexto = "\n".join([
            r["texto"]
            for r in resultados
        ])

        historico = obter_historico()

        resposta = responder(
            pergunta,
            contexto,
            historico
        )

        adicionar_interacao(pergunta, resposta)

        st.subheader("🧠 Resposta")

        st.write(resposta)
        # =========================
        # MELHOR TRECHO
        # =========================

        if resultados:

            melhor_resultado = resultados[0]

            timestamp = int(
                melhor_resultado["inicio"]
            )

            minutos = timestamp // 60
            segundos = timestamp % 60

            st.info(
                f"📍 Resposta encontrada em: "
                f"{minutos:02}:{segundos:02}"
            )