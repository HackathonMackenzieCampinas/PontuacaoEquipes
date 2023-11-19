#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#import matplotlib.pyplot as plt
image01 = Image.open('ImagemLateral.jpg')
image02 = Image.open('Ranking.jpg')
st.sidebar.image(image01, width=300, caption='Mack Week CCT 2022') 
st.sidebar.markdown("<h1 style='text-align: justify; color: DarkBlue; font-size: 14px'>O evento Hackathon é um desafio de inovação onde os alunos, em suas equipes formadas, concorrerão com suas ideias e propostas de soluções para um dos desafios a seguir:</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: justify; color: black; font-size: 14px'>Resumo dos Desafios - 2º Hackathon 2023</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Desafio 1 - Equipes 2 e 14 (Mentor: Leonardo Fabris): Implementação de Chatbots para Atendimento Inicial com integração à platafor-ma omnichannel.</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Desafio 2 - Equipes 10 e 13 (Mentor: Rodolfo Ribeiro): Criação e Otimização de fluxos de Processos e apresentação de indicadores.</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Desafio 3 - Equipes 5, 8 e 12 (Mentor: Glaison Carvalho): Solução para roteirização e monitoramento de alunos no transporte escolar, em que a escola e pais/responsáveis possam monitorar,via geolocalização, cada aluno desde que ele iniciou o seu trajeto no ônibus até a sua chegada na escola, além de toda a sua movimentação no ambiente escolar,e também no trajeto de retorno da escola à sua residência.</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Desafio 4 - Equipes 6 e 11 (Mentor: Vinicius Gomes da Silva): Sistema para controle de Escala</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Desafio 5 - Equipes 3 e 4 Mentor: Ana Carolina Melão): Sistema de Controle de Mobiliário(solicitar manutenção, troca, pedido de cadeira)</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Desafio 6 - Equipes 1, 7 e 15 (Mentores: Marcos Ribeiro e/ou Rafael Damaceno): Sistema da prestação de contas telefônico.</h1>", unsafe_allow_html=True)

#st.title("PAINEL - EQUIPES HACKATHON")
Titulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 32px;">2ª EDIÇÃO DO DESAFIO HACKATHON: MACKENZIE CAMPINAS - LOGITHINK.IT - IMA (Edição 2023)</p>'
st.markdown(Titulo_Principal, unsafe_allow_html=True)
Sub_Titulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 28px;"> "O aluno inovando na universidade e nas empresas" </p>'
st.markdown(Sub_Titulo_Principal, unsafe_allow_html=True)
mystyle1 =   '''<style> p{text-align:center;}</style>'''
st.markdown(mystyle1, unsafe_allow_html=True) 
st.markdown(
"""
[Drive para acessar Relatórios e Projetos enviados pelas Equipes](https://drive.google.com/drive/folders/1XqsLFmxDp5bIpoUbdAlJveS04JccW6_G?usp=sharing)
""")
#============================================================================================
#IMPORTAÇÃO DOS DADOS DA PLANILHA Pontuação das Equipes II Hackathon Mackenzie-Logithink-IMA (hackathon.cct.2023@gmail.com)
rP = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQj4zhEz_COCvFMKnizUaRZz87rl8tOVv3b-U7q9fQFMauMRbT7vJDIlI8HPSLAdoCsthRh6yEigLsX/pub?gid=87278842&single=true&output=csv')
dataP = rP.content
dfP = pd.read_csv(BytesIO(dataP))
dfP.columns = ['D/H', 'Participacao', 'Criatividade', 'Coerencia', 'Apresentacao', 'MVP', 'Inovacao', 'OBS', 'Equipe']
resumo = dfP.groupby(["Equipe"]).sum()
rotulo = resumo.index
nEquipes = len(rotulo)
qtdDadosPorEquipe = []
for count in range(nEquipes):
  selecao01P = dfP['Equipe']==rotulo[count]
  df01P = dfP[selecao01P]
  qtdDadosPorEquipe.append(len(df01P))
  del(df01P)

resumo = dfP.groupby(["Equipe"]).sum()
dfresumo = pd.DataFrame(resumo)
n=len(rotulo)
#============================================================================================
# IMPORTAÇÃO DO FORM RESPOSTAS ÀS DÚVIDAS PELOS TUTORES
rT = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTIxe7VmjCRpyVvwKaajuRFyp6T1MRGOx_GCUg7ghiA2QWbiNLYam-xpLYhXE2Gdn6RgLjRRJPD4WZ-/pub?gid=1131399848&single=true&output=csv')
dataT = rT.content
dfT = pd.read_csv(BytesIO(dataT))
dfT.columns = ['D/T', 'e-mail', 'Equipe', 'Nome', 'Resposta', 'OBS', 'mail', 'Classificacao' ]
dfT.fillna(value = ' ',  inplace = True)
#===============================================
if len(dfP) != 0:
  vetNOTAS = []
  colNotas1,colNotas2, colNotas3 = st.columns((1,1,1))
  with colNotas1:
    st.markdown("<h1 style='text-align: center; color: blue;'>Resumo dos Pontos</h1>", unsafe_allow_html=True)
    for i in range(n):
      pa = float(dfresumo['Participacao'][i])/qtdDadosPorEquipe[i]
      cr = float(dfresumo['Criatividade'][i])/qtdDadosPorEquipe[i]
      co = float(dfresumo['Coerencia'][i])/qtdDadosPorEquipe[i]
      ap = float(dfresumo['Apresentacao'][i])/qtdDadosPorEquipe[i]
      mvp =  float(dfresumo['MVP'][i])/qtdDadosPorEquipe[i]
      inov = float(dfresumo['Inovacao'][i])/qtdDadosPorEquipe[i]
      nota = round(pa + cr + co + ap + mvp + inov, 2)
      vetNOTAS.append(nota)
      st.write("Média Total da " + str(rotulo[i]))
      st.success(nota)
  with colNotas2:
    st.markdown("<h1 style='text-align: left; color: blue;'>Ranking de Pontuação</h1>", unsafe_allow_html=True)
    DF = pd.DataFrame(vetNOTAS)
    DF.columns = ['Nota']
    DF.index = rotulo
    st.dataframe(DF.sort_values(by='Nota', ascending=False))     
  with colNotas3:
    st.title(" ")
    st.image(image02, width=150, caption='Classificação Final')
    st.markdown("<h1 style='text-align: justify; font-family:arial; font-size: 14px; color: gray;'>Este painel tem o objetivo de auxiliar a Equipe de Gestão do Hackathon 2023 escolher as 5 equipes finalistas que participarão do Evento Final, disputando uma das 3 vagas na dinâmica Elevator Pitch.</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left; color: blue; font-size: 20px'>Ranking de Citação nas Avaliações</h1>", unsafe_allow_html=True)
    st.write(dfP["Equipe"].value_counts())  
                 
  st.markdown("<h1 style='text-align: left; color: blue;'>Auditoria dos Dados</h1>", unsafe_allow_html=True)
  st.dataframe(dfP.sort_values(by='D/H', ascending=True))  

  coluna1, coluna2 = st.columns((1,1))
  with coluna1:
    st.markdown("<h1 style='text-align: left; color: blue;font-size: 14px'>Participação dos Tutores (Alunos Mackenzie)</h1>", unsafe_allow_html=True)
    selecao01T = dfT['Classificacao']=='Tutor(a)'
    df01T = dfT[selecao01T]
    resumoT = pd.DataFrame(df01T["Nome"].value_counts())
    resumoT.columns = ['qtdRESPOSTAS']
    PorcentPART = []
    nTotal = df01T["Nome"].value_counts().sum()
    for i in range(len(resumoT['qtdRESPOSTAS'])):
      part = round(100*resumoT['qtdRESPOSTAS'][i]/nTotal,2)
      PorcentPART.append(str(part)+"%")
    dfPorcentPART = pd.DataFrame(PorcentPART)
    dfPorcentPART.index = resumoT.index
    dfPorcentPART.columns = ['%Participação']
    st.dataframe(dfPorcentPART)
  with coluna2:
    st.markdown("<h1 style='text-align: justify; color: DarkBlue; font-size: 16px'>Resumo dos Tutores por Equipe:</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Equipe 03: Elisabete Olimpio</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Equipe 06: Gabriel Ferrarese</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Equipe 07: Otávio Sigolo</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Equipe 08: Beatriz Scarpato</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Equipe 10: Romualdo dos Santos</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Equipe 11: Laura Gurgel</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Equipe 12: Luana Paes</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: justify; color: black; font-size: 12px'>Equipe 15: Roberto Guimaraes</h1>", unsafe_allow_html=True)
