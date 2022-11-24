from flask import request
from flask import Flask, render_template, redirect, url_for
import requests
from bs4 import BeautifulSoup
import random

app = Flask(__name__)



@app.get("/")
def index():
    return render_template("index.html", data=get_data())
    

def get_data():

    list_of_data = []

    url_list = ["https://www.ultimahora.com", "https://www.abc.com.py", "https://npy.com.py", "https://www.lanacion.com.py"]


    for url in url_list:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        if url == "https://npy.com.py":
            # NPY
            npy_results = soup.find_all("div", "meta-info-inner")
            print("NPY")
            for element in npy_results:
                print(element.a["href"]) # link de la noticia
                print(element.h3.text) # encabezado de la noticia
                list_of_data.append({
                    "diario_marca": "NPY", 
                    "url_noticia": element.a["href"], 
                    "noticia_encabezado": element.h3.text
                })
                print("\n")


        elif url == "https://www.lanacion.com.py":
            # LA NACION
            print("LA NACION")

            for parentElement in soup.find_all(id="ph-dp"):
                childElement = parentElement.find_all('div', class_="tc")
                # print(element.text) # encabezado de la noticia
                for noticia in childElement:
                    print(noticia.a["href"])
                    print(noticia.h3.text)
                    list_of_data.append({
                        "diario_marca": "La Nación", 
                        "url_noticia": noticia.a["href"] if "https" in noticia.a["href"] else "https://www.lanacion.com.py" + noticia.a["href"], 
                        "noticia_encabezado": noticia.h3.text
                    })
                    print("\n")


        elif url == "https://www.abc.com.py":
            print("ABC")

            for parentElementABC in soup.find_all("div", class_="section-featurednews"):
                childElementABC = parentElementABC.find_all('div', "article-info")
                
                for noticiaABC in childElementABC:
                    print(noticiaABC.a["href"])
                    print(noticiaABC.find("div", class_="article-title").text)
                    print("\n")
                
                    list_of_data.append({
                        "diario_marca": "ABC Color", 
                        "url_noticia": "https://www.abc.com.py" + noticiaABC.a["href"], 
                        "noticia_encabezado":  noticiaABC.find("div", class_="article-title").text 
                    })
        

        elif url == "https://www.ultimahora.com":
            print("ULTIMA HORA")

            for parentElementUH in soup.find_all("div", class_="articles-3-col"):
                childElementUH = parentElementUH.find_all('h2', "article-title")
                
                for noticiaUH in childElementUH:
                    print(noticiaUH.a["href"])
                    print(noticiaUH.text)
                    print("\n")
                
                    list_of_data.append({
                        "diario_marca": "Última Hora", 
                        "url_noticia": noticiaUH.a["href"], 
                        "noticia_encabezado":  noticiaUH.text 
                    })
           
    return list_of_data
                
        