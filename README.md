## Agregador de noticias
Para inicializar el proyecto de forma local (Ubuntu):
1. Crear la carpeta venv para el entorno virtual

    `python3 -m venv venv`
    
2. Activar el entorno virtual

    `. venv/bin/activate`
    
3. Ya dentro del entorno virtual, instalar Flask

    `pip install flask`
    
4. Instalar los paquetes que utiliza la aplicación

    `pip3 install -r requirements.txt`
    
5. Ejecutar la aplicación

    `flask --app main.py --debug run`
    
6. Visualizarla en `http://127.0.0.1:5000`



