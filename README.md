# VideoGPT
Sistema multimodal de IA capaz de conversar com vídeos, áudios e conteúdos do YouTube utilizando RAG, Whisper, FAISS e busca semântica.

🎥 VideoGPT — Chat com Vídeos usando IA Generativa + RAG
Sistema inteligente de análise de vídeos utilizando IA Generativa, RAG (Retrieval-Augmented Generation), busca semântica e embeddings vetoriais.
O projeto permite enviar vídeos, áudios ou links do YouTube e conversar com o conteúdo do vídeo utilizando linguagem natural.

➤ Funcionalidades                                                                         
✔️ Upload de vídeos e áudios                                  
•	MP4                        
•	MP3                         
•	WAV                                 

✔️ Integração com YouTube                            
•	Download automático de áudio                          
•	Processamento direto da URL                           

✔️ Transcrição automática                         
•	Utilizando OpenAI Whisper                          
•	Conversão de áudio para texto                            

✔️ Busca semântica                        
•	Embeddings vetoriais                        
•	Recuperação contextual via FAISS                              

✔️ Chat contextual com IA                          
•	Perguntas sobre o conteúdo do vídeo                          
•	Respostas contextuais                          
•	Histórico de conversa                                      

✔️ Navegação temporal                            
•	Localização do momento do vídeo relacionado à resposta                          
•	Timestamp inteligente                                

✔️ Análise automática                             
•	Extração de tópicos principais                                 
•	Organização semântica do conteúdo                               


➤ Tecnologias Utilizadas                        
•	Python                          
•	Streamlit                              
•	Whisper                             
•	FAISS                             
•	Sentence Transformers                             
•	Embeddings                              
•	RAG                           
•	LLM                                  
•	Semantic Search                               
•	YouTube Downloader                                     

➤ Arquitetura do Projeto                             
🔹 Whisper                                         
Responsável pela transcrição automática do áudio.                      
🔹 Embeddings                                
Transforma os textos em vetores semânticos.                              
🔹 FAISS                            
Banco vetorial utilizado para busca semântica eficiente.                             
🔹 RAG                               
Sistema de recuperação contextual para melhorar respostas da IA.                          
🔹 LLM                         
Responsável pela geração das respostas contextuais.                                

➤ Estrutura do Projeto                               
VideoGPT/                            
│                        
├── streamlit_app.py                                   
├── rag.py                                    
├── llm.py                                   
├── audio_loader.py                                                        
├── youtube_loader.py                                         
├── memory.py                                                     
├── temp/                                                     
├── transcricoes/                                                      
└── requirements.txt                                                         

➤ Como Funciona                                                 
1.	Usuário envia vídeo ou URL do YouTube                                            
2.	Whisper realiza a transcrição                         
3.	Texto é dividido em chunks                          
4.	Embeddings são gerados                           
5.	Vetores são armazenados no FAISS                              
6.	Usuário faz perguntas                              
7.	Busca semântica encontra os trechos relevantes                            
8.	IA gera respostas contextualizadas                          

➤ Exemplos de Uso                                  
•	Chat com aulas gravadas                              
•	Busca inteligente em podcasts                           
•	Pesquisa em entrevistas                             
•	Navegação semântica em vídeos                       
•	IA para conteúdo multimodal                             
•	Análise automática de vídeos                            

➤ Objetivo do Projeto                         
Explorar aplicações reais de IA Generativa combinando:                        
•	Processamento multimodal                                  
•	Busca vetorial                               
•	Semantic Search                             
•	Temporal Retrieval                           
•	Video AI                              
•	RAG Systems                                 

➤ Conceitos de IA Aplicados                                  
•	Retrieval-Augmented Generation (RAG)                            
•	Semantic Search                                
•	Vector Databases                               
•	Embeddings                                   
•	Large Language Models                                     
•	Multimodal AI                           
•	Temporal Retrieval                                
•	Conversational AI                              

➤ Licença                                                  
Projeto desenvolvido por Juliano Rodrigues Madeira.                           
