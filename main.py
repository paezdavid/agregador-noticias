from flask import request
from flask import Flask, render_template, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html", data=get_data())
    

def get_data():

    # All data (the news) to be sent to the client is stored in this dictionary
    dict_of_data = {
        "prensa_py": [],
        "prensa_inter": []
    }

    url_list = ["https://www.ultimahora.com", "https://elpais.com/america", "https://cnnespanol.cnn.com", "https://www.abc.com.py", "https://npy.com.py", "https://www.lanacion.com.py", "https://www.bbc.com/mundo"]


    for url in url_list:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        if url == "https://npy.com.py":
            npy_results = soup.find_all("div", "meta-info-inner")
            counter_npy = 0 # A counter is needed to limit the amount of results sent to the client. A counter variable will be used for all news sites.

            for element in npy_results:
                if counter_npy < 5:
                    dict_of_data["prensa_py"].append({
                        "diario_marca": "NPY", 
                        "url_noticia": element.a["href"], 
                        "noticia_encabezado": element.h3.text
                    })
                else:
                    break

                counter_npy += 1

        elif url == "https://www.lanacion.com.py":
            counter_ln = 0

            for parentElement in soup.find_all(id="ph-dp"):
                childElement = parentElement.find_all('div', class_="tc")
                
                for noticia in childElement:
                    if counter_ln < 5:
                        dict_of_data["prensa_py"].append({
                            "diario_marca": "La Nación", 
                            "url_noticia": noticia.a["href"] if "https" in noticia.a["href"] else "https://www.lanacion.com.py" + noticia.a["href"], 
                            "noticia_encabezado": noticia.h3.text
                        })
                    else:
                        break

                    counter_ln += 1

        elif url == "https://www.abc.com.py":
            counter_abc = 0

            for parentElementABC in soup.find_all("div", class_="section-featurednews"):
                childElementABC = parentElementABC.find_all('div', "article-info")
                
                for noticiaABC in childElementABC:
                    if counter_abc < 5:
                        dict_of_data["prensa_py"].append({
                            "diario_marca": "ABC Color", 
                            "url_noticia": "https://www.abc.com.py" + noticiaABC.a["href"], 
                            "noticia_encabezado":  noticiaABC.find("div", class_="article-title").text
                        })
                    else:
                        break

                    counter_abc += 1
        
        elif url == "https://www.ultimahora.com":
            counter_uh = 0

            for parentElementUH in soup.find_all("div", class_="articles-3-col"):
                childElementUH = parentElementUH.find_all('h2', "article-title")
                
                for noticiaUH in childElementUH:
                    if counter_uh < 5:
                        dict_of_data["prensa_py"].append({
                            "diario_marca": "Última Hora", 
                            "url_noticia": noticiaUH.a["href"], 
                            "noticia_encabezado":  noticiaUH.text
                        })
                    else:
                        break
                    counter_uh += 1
        
        elif url == "https://www.bbc.com/mundo":
            counter_bbc = 0
            for noticia_bbc in soup.find_all("a", class_="bbc-1fxtbkn ecljyjm0"):

                if counter_bbc < 5:
                    dict_of_data["prensa_inter"].append({
                        "diario_marca": "BBC Mundo", 
                        "url_noticia": "https://www.bbc.com" + noticia_bbc["href"], 
                        "noticia_encabezado":  noticia_bbc.text
                    })
                else:
                    break
                    
                counter_bbc += 1
           
        elif url == "https://cnnespanol.cnn.com":
            counter_cnn = 0
            for noticia_cnn in soup.find_all("h2", class_="news__title"):
                if counter_cnn < 5:
                    dict_of_data["prensa_inter"].append({
                        "diario_marca": "CNN en Español", 
                        "url_noticia": noticia_cnn.a["href"], 
                        "noticia_encabezado":  noticia_cnn.text
                    })
                else:
                    break

                counter_cnn += 1

        elif url == "https://elpais.com/america":
            counter_pais = 0

            for main_section_pais in soup.find_all("section", class_="_g _g-md _g-o b b-d"):
                for noticia_pais in main_section_pais.find_all("h2", class_="c_t"):
                    if counter_pais < 5:
                        dict_of_data["prensa_inter"].append({
                            "diario_marca": "El País", 
                            "url_noticia": "https://elpais.com" + noticia_pais.a["href"], 
                            "noticia_encabezado":  noticia_pais.text
                        })
                    else:
                        break

                    counter_pais += 1


    return dict_of_data
                
        