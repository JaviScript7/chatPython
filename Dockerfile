#Esto es un dockerfile para un entorno de produccion

#Elegimos la imagen base con la version respectiva
FROM python:3.8

#Indicamos quien es el respnsable de mantener el contenedor
LABEL Maintainer = "JaviScript"

#Creamos el directorio de la aplicacion
RUN mkdir -p /home/app

#Copiar los archivos de la aplicacion
COPY . /home/app

#Establecemos el espacio de trabajo
WORKDIR /home/app

#Exponemos el puerto en este caso para Flask
EXPOSE 5000

#Instalamos las dependencias necesarios para correr el programa
RUN pip install --no-cache-dir -r /home/app/requirements.txt

CMD ["python","app.py"]
#Ejecutar la aplicacion Flask usando Gunicorn
#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "categoria:app"]