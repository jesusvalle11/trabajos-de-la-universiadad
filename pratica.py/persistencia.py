
from io import open

objeto = open("archivo.txt","w")
objeto.write("esto es una prueba\n"
"hoy estudiamos python y manejo de archivos")
objeto.close()