import streamlit as st
import pandas as pd
from openai import OpenAI
import json

# Configração de página layuot
st.set_page_config(layout="wide")

# Configurando colunas
col1, col2 = st.columns(2)

# Configurando CSS
st.markdown('''<style>
                *{
                    margin:0;
                    padding:0;
                    box-sizing: border-box;
                }
        
                .letra{
                    color:white;
                }
                
                .block-container{
                    background-color: #611C8F;
                }
                
                .flex{
                    display:flex;
                }
                
                .main-1{
                    display:flex;
                    height: 200px;
                    margin: 10px;
                }
                .main-2{
                    display:grid;
                    heoght: 200px;
                    margin: 15px;
                }
                
                .italic{
                    color:rgb(107, 106, 104);
                    font-style: italic;
                }
                

                .header{
                    font-size: 25px;
                    border-radius: 10px;
                    background-color: #EE039C;
                    text-align: center;
                    color: white;
                    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
                }

                .mag{
                    margin: 15px auto;
                }
                
                .mag-auto{
                    display: flex;
                    justify-content: center; 
                    align-items: center;
                    width: 100%; 
                    margin: 0px auto;
                }
                .imagem{
                    border-radius: 15px;
                    border: solid 2px #EE039C;
                    width: 60%;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px;
                }
                .imagem-2{
                    border-radius: 15px;
                    border: solid 2px #EE039C;
                    margin: 30px;
                    width: 200px;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px;
                }
                .center{
                    text-align: center;
                    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
                    border-radius: 10px 10px 0 0;
                    background-color: #EE039C;
                    color: white;
                    box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
                }
                
                .card{
                    margin: 10px;
                    border: solid 1px;
                    background-color: aliceblue;
                    width: 100%;
                    height: 100%;
                    border-radius: 10px;
                }
                .card-2{
                    margin: 10px auto;
                    border: solid 1px;
                    background-color: aliceblue;
                    height: 100%;
                    width: 99%;
                    border-radius: 10px;
                }
                
                .title{ 
                    font-size: 20px;
                    font-weight: bold;
                    border-bottom: solid 1px;
                    margin: auto;
                }
                
                .justify{
                    text-align: justify;
                    margin:10px;
                }
                .stButton{
                    text-align: center;
                }
                
                .st-emotion-cache-l9bjmx{
                    margin: 10px 0;
                    padding: 10px;
                    color: white;
                    border: solid 2px #EE039C;
                    border-radius: 10px;
                    background-color: 611C8F;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px;
                }
                
                .e1b2p2ww15{
                    background-color: #EE039C;
                }
                
                .e1nzilvr5{
                    margin:10px;
                    background-color: #611C8F;
                    color: white;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px;
                    border: solid 1px #EE039C;
                }
                
                .e1b2p2ww5{
                    margin:10px;
                    background-color: #611C8F;
                    color: white;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px;
                    border: solid 1px #EE039C;
                }
                
                .ef3psqc12{
                    background-color: #611C8F;
                    color: white;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #611C8F 0px 3px 6px;
                    border: solid 1px #EE039C; 
                }
                
                .ef3psqc12:hover{
                    background-color: #EE039C;
                    color: white;
                    box-shadow: #611C8F 0px -30px 16px -10px inset;
                    border: solid 1px #611C8F;
                }
                
                .ef3psqc7{
                    background-color: #611C8F;
                    color: white;
                    border: solid 1px #EE039C;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px;
                }
                
                .ef3psqc7:hover{
                    background-color: #EE039C;
                    color: white;
                    box-shadow: #611C8F 0px -30px 16px -10px inset;
                    border: solid 1px #EE039C;
                }
                
                .eczjsme5{
                    color:white;
                }
                
                .eczjsme6{
                    margin: 10px;
                    background-color: #611C8F;
                    color: white;
                    border: solid 1px #EE039C;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #611C8F 0px 3px 6px;
                }
                
                .eczjsme3{
                    background-color: #EE039C;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px;
                        
                }
                
                .resposta{
                    background-color: #EE039C;
                    box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px; 
                    padding: 10px;
                    color: white;
                    border-radius: 10px;   
                }
                
                @media (max-width: 500px) {
                    
                    .title{
                        font-size: 12px;
                    }
                    .imagem{
                        border-radius: 15px;
                        width: 80%;
                        border: solid 2px #EE039C;
                        box-shadow: rgba(0, 0, 0, 0.16) 0px 4px 7px, #EE039C 0px 3px 6px;
                    }
                }
            </style>'''
            ,unsafe_allow_html=True)

# Configurando session_state

if not 'resposta' in st.session_state:
    resposta = ''
    st.session_state.resposta = ''

if not 'json' in st.session_state:
    st.session_state.json = ''

# Conectando com o ChatGPT
client = OpenAI()

def ask_openai(mensagem, df):
    if mensagem == "":
        return "Como posso ajudá-lo?"
    try:
        print("Iniciando chat")
        completion = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (f'''
                                    Você é um business analyst, um chatbot da itriad! Você deve avaliar cada caso de teste do arquivo json {df} e respoder da seguinte forma: Exemplo: Pergunta do usuário: 
                                    \"role\": \"user\", \"content\": \"O que significa FPFtech? Resposta do assistente: \"role\": \"assistant\", \"content\": \"A sigla FPFtech significa fundação Paulo Feitoza.\"    
                                '''
                                )
                },
                {
                    "role": "user",
                    "content": (f'''
                                   {mensagem} 
                                ''')
                }
            ],

            temperature=1,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0

            )
        
        answer = completion.choices[0].message.content
        print(f"answer: {answer}")
        return answer
    
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return None

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None
    
with col1:
    with st.container():
        with st.form(key='revisar_casos_form'):
            st.write('''<h1 class="header">Faça o upload dos casos de testes</h1>''', unsafe_allow_html=True)
            dados = st.file_uploader("Insira o arquivo abaixo:", type=["xlsx"])
            
            submit_button = st.form_submit_button(label='Submeter')

        if submit_button:
            df = pd.read_excel(dados)
            st.dataframe(df)
            json_df = df.to_json(orient='records',force_ascii=False,lines=True)
            st.session_state.json = json_df
            
with col2:
    with st.container():
        if st.session_state.json == '':
            img_path = "https://ibb.co/WgDQ1Fb"
            st.write('''<h1 class="header mag">Chat assistente</h1>
                        <div class="mag-auto" >
                            <img class ="imagem" src="https://i.ibb.co/MM8bLpY/sem-planilha.png" alt="sem-planilha" border="0" />
                        </div>
                    ''', unsafe_allow_html=True)
        else:
            st.write('''<h1 class="header mag">Planilha preenchida</h1>
                    ''', unsafe_allow_html=True)
            
            mensagem = st.text_input("Faça sua pergunta")
        
            if mensagem:
                resposta = ask_openai(mensagem, st.session_state.json)
                resposta_json = json.loads(resposta)
                resposta_final = json.dumps(resposta_json["content"], ensure_ascii=False).replace('"','')
                print(resposta_final)
                st.write(f'''
                            <div class="flex"> 
                                <img class ="imagem-2" src="https://i.ibb.co/MM8bLpY/sem-planilha.png" alt="sem-planilha" width="50" border="0" />
                                <div class="resposta"> 
                                    <div>{resposta_final}</div>
                                </div>
                            </div>
                    ''', unsafe_allow_html=True)