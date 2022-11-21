import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser
import time

st.markdown("<h1 style='text-align: center;'>Buscador de Imagens</h1>",unsafe_allow_html=True)
with st.form('Buscar'):
    imput = st.text_input("Entre com a palavra")
    busca = st.form_submit_button("Buscar")
limp = st.empty()
if imput:
    col1,col2 = limp.columns(2)
    saida = requests.get(f"https://unsplash.com/s/photos/{imput}")
    cont = 0
    soup = BeautifulSoup(saida.content, 'lxml')
    rows = soup.find_all("div", class_="ripi6")
    for index, row in enumerate(rows):
        figura = row.find_all('figure')
        for i in range(2):
            img = figura[i].find("img", class_="YVj9w")
            lista = img["srcset"].split('?')
            ancora = figura[i].find("a", class_="rEAWd")
            if "https://plus.unsplash.com/premium" in lista[0]:
                continue
            else:
                if cont %2 ==0 :
                    col1.image(lista[0])
                    button = col1.button("Download", key=str(index)+str(i))
                    cont+=1
                    if button:
                        webbrowser.open_new_tab("https://unsplash.com/"+ancora["href"])
                else:
                    col2.image(lista[0])
                    button = col2.button("Download", key=str(index)+str(i))
                    cont+=1
                    if button:
                        webbrowser.open_new_tab("https://unsplash.com/"+ancora["href"])
            time.sleep(0.5)
                