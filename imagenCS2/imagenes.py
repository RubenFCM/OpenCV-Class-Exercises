# Importar libreria cv2
# Instalar cv2  pip3 install opencv-python
import cv2
import os

###########################################################################################
    # Ejercicio 1
    # Crea una función que pasándole la ruta de una imagen, la rote 180 grados y genere una
    # nueva imagen.
###########################################################################################
def rotateImage(ruta):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    imagen_rotate = cv2.rotate(imagen,cv2.ROTATE_180)
    # Redimensionar las imágenes a un tamaño más pequeño
    imagen_resized = cv2.resize(imagen, (400, 300))
    imagen_resized_rotate = cv2.resize(imagen_rotate, (400, 300))

    # Generamos un nombre para la nueva imagen
    #nueva_imagen = (ruta.split(".")[1] + "_rotated." + ruta.split(".")[2])

    # Usar os.path.splitext() para separar el nombre y la extensión
    nombre, extension = os.path.splitext(ruta)
    # Crear la nueva ruta con el nombre modificado y la misma extensión
    nueva_imagen = nombre + '_rotated' + extension

    # La guardamos en memoria en un fichero distinto y devolvemos la ruta
    cv2.imwrite(nueva_imagen, imagen_rotate)

    # Mostrar imagenes
    cv2.imshow('Imagen Original', imagen_resized)
    cv2.imshow('Imagen Rotada', imagen_resized_rotate)

    # Esperar hasta que el usuario presione una tecla
    cv2.waitKey(0)  # Espera hasta que se presione cualquier tecla

    # Cerrar todas las ventanas de OpenCV
    cv2.destroyAllWindows()

###########################################################################################
    # Ejercicio 2
    # Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir
    # de ella con los colores invertidos.
###########################################################################################
def negative_color(ruta):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    imagen_negative = cv2.bitwise_not(imagen)
    # Redimensionar las imágenes a un tamaño más pequeño
    imagen_resized = cv2.resize(imagen, (400, 300))
    imagen_resized_negative = cv2.resize(imagen_negative, (400, 300))

    # Usar os.path.splitext() para separar el nombre y la extensión
    nombre, extension = os.path.splitext(ruta)
    # Crear la nueva ruta con el nombre modificado y la misma extensión
    nueva_imagen = nombre + '_negative' + extension

    # La guardamos en memoria en un fichero distinto y devolvemos la ruta
    cv2.imwrite(nueva_imagen, imagen_negative)

    # Mostrar imagenes
    cv2.imshow('Imagen Original', imagen_resized)
    cv2.imshow('Imagen Color negativo', imagen_resized_negative)

    # Esperar hasta que el usuario presione una tecla
    cv2.waitKey(0)  # Espera hasta que se presione cualquier tecla

    # Cerrar todas las ventanas de OpenCV
    cv2.destroyAllWindows()

###########################################################################################
    # Ejercicio 3
    # Crea una función que pasándole la ruta de una imagen, genere una nueva imagen a partir
    # ella pero en escala de grises.
###########################################################################################
def gray_scale_color(ruta):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    imagen_gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Redimensionar las imágenes a un tamaño más pequeño
    imagen_resized = cv2.resize(imagen, (400, 300))
    imagen_resized_gray = cv2.resize(imagen_gray, (400, 300))

    # Usar os.path.splitext() para separar el nombre y la extensión
    nombre, extension = os.path.splitext(ruta)
    # Crear la nueva ruta con el nombre modificado y la misma extensión
    nueva_imagen = nombre + '_gray' + extension

    # La guardamos en memoria en un fichero distinto y devolvemos la ruta
    cv2.imwrite(nueva_imagen, imagen_gray)

    # Mostrar imagenes
    cv2.imshow('Imagen Original', imagen_resized)
    cv2.imshow('Imagen en escala de grises', imagen_resized_gray)

    # Esperar hasta que el usuario presione una tecla
    cv2.waitKey(0)  # Espera hasta que se presione cualquier tecla

    # Cerrar todas las ventanas de OpenCV
    cv2.destroyAllWindows()

###########################################################################################
    # Ejercicio 4
    # Crea una función que pasándole la ruta de una imagen, marque un cuadrado a partir de
    # dos coordenadas.
###########################################################################################
def box_face_by_cordinates(ruta,coordX,coordY,color):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    box_face = cv2.rectangle(imagen,coordX,coordY,color,5)

    imagen_resized_box = cv2.resize(box_face, (800, 600))

    # Usar os.path.splitext() para separar el nombre y la extensión
    nombre, extension = os.path.splitext(ruta)
    # Crear la nueva ruta con el nombre modificado y la misma extensión
    nueva_imagen = nombre + '_box' + extension
    # La guardamos en memoria en un fichero distinto y devolvemos la ruta
    cv2.imwrite(nueva_imagen, box_face)

    # Mostrar imagen
    cv2.imshow('Imagen con cuadrado', imagen_resized_box)

    # Esperar hasta que el usuario presione una tecla
    cv2.waitKey(0)  # Espera hasta que se presione cualquier tecla

    # Cerrar todas las ventanas de OpenCV
    cv2.destroyAllWindows()

###########################################################################################
    # Ejercicio 5
    # Crea una función que pasándole la ruta de una imagen, invierta los colores de un cuadrado
    # a partir de dos coordenadas, pasadas por parámetro.
###########################################################################################

def box_color_inverter(ruta,coordX,coordY):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)

    x1, x2 = coordX
    y1, y2 = coordY
    box = imagen[y1:y2, x1:x2]
    # Invertir los colores del box
    box_invertida = cv2.bitwise_not(box)
    # Reemplazar la ROI original con la invertida
    imagen[y1:y2, x1:x2] = box_invertida

    imagen_resized = cv2.resize(imagen, (800, 600))

    # Usar os.path.splitext() para separar el nombre y la extensión
    nombre, extension = os.path.splitext(ruta)
    # Crear la nueva ruta con el nombre modificado y la misma extensión
    nueva_imagen = nombre + '_invcua' + extension
    # La guardamos en memoria en un fichero distinto y devolvemos la ruta
    cv2.imwrite(nueva_imagen, imagen)

    # Mostrar la imagen resultante
    cv2.imshow("Imagen con colores invertidos", imagen_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()