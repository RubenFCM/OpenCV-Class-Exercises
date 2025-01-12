# Importar libreria cv2
# Instalar cv2  pip3 install opencv-python
import cv2
import os
import numpy as np


# Función para guardar una imagen en la carpeta img
def save_image_v2(ruta, text, img):
    # Usar os.path.splitext() para separar el nombre y la extensión
    nombre, extension = os.path.splitext(ruta)
    # Crear la nueva ruta con el nombre modificado y la misma extensión
    nueva_imagen = nombre + text + extension
    # La guardamos en memoria en un fichero distinto y devolvemos la ruta
    cv2.imwrite(nueva_imagen, img)


###########################################################################################
# Ejercicio 1
# Como variante del ejercicio 5 se propone invertir los colores de toda la imagen menos del
# marco indicado. Añadirlo como funcionalidad extra, es decir, por defecto la función operará
# como hasta ahora pero podrá pedírsele que realice la operación aquí descrita.

# El ejercicio 5 invertía los colores de un marco indicado por unas coordenadas pasadas por
# parámetro, vamos a añadir un parámetro para determinar si se invertirá el marco o el resto de la
# imagen.
###########################################################################################

def box_color_inverter_v2(ruta, coord1, coord2, in_box):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)

    x1, y1 = coord1
    x2, y2 = coord2
    if (in_box):
        box = imagen[x2:y2, x1:y1]
        # Invertir los colores de la imagen completa
        imagen = cv2.bitwise_not(imagen)
        # Reemplazar la zona del box en la imagen completa
        imagen[x2:y2, x1:y1] = box
    else:
        box = imagen[x2:y2, x1:y1]
        # Invertir los colores del box
        box_invertida = cv2.bitwise_not(box)
        # Reemplazar la ROI original con la invertida
        imagen[x2:y2, x1:y1] = box_invertida

    save_image_v2(ruta, '_invcua_V2', imagen)


###########################################################################################
# Ejercicio 2
# Como variante del ejercicio 11, se propone transformar toda la imagen fuera del marco a
# tonos de gris. Añadirlo como funcionalidad extra.
###########################################################################################

def gray_outside_frame(ruta, coord1, coord2):
    # Cargar la imagen en memoria
    img = cv2.imread(ruta)
    # Elegir con las coordenadas la parte de la imagen que queremos a color
    box = img[coord1[1]:coord2[1], coord1[0]:coord2[0]]
    # Convertir la imagen a escala de grises
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Convertir la imagen en escala de grises, pero con 3 canales
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # Reemplazar en la imagen en escala de grises la parte que nos interesa por la guardada antes a color
    img[coord1[1]:coord2[1], coord1[0]:coord2[0]] = box
    # Mostrar cuadrado en las coordenadas
    cv2.rectangle(img, coord1, coord2, (0, 0, 255), 5)

    save_image_v2(ruta, '_gray_outside', img)

    return img


###########################################################################################
# Ejercicio 3
# Como variante del ejercicio 11, se propone que la imagen generada contenga solo el
# marco seleccionado, incluyendo un perímetro en tonos de grises, además la etiqueta podrá
# estar vacía.
# Como variante del ejercicio 11 se propone que el texto sea opcional y se ajuste al tamaño
# del cuadro.
###########################################################################################
def paint_box_text(ruta, coord1, coord2, text, gray, cut):
    # Cargar imagen
    img = cv2.imread(ruta)
    # Elegir con las coordenadas la parte de la imagen que queremos a color

    if gray:
        img = gray_outside_frame(ruta, coord1, coord2)

    # Mostrar cuadrado en las coordenadas
    cv2.rectangle(img, coord1, coord2, (0, 0, 255), 5)

    if text != '':
        img = add_text(img, coord1, coord2, text)

    if cut:
        img = gray_outside_frame_img(img, coord1, coord2)
        img = img[coord1[1] - 100:coord2[1] + 100, coord1[0] - 100:coord2[0] + 100]

    save_image_v2(ruta, '_Text_Gray_Outside', img)

    return img


# Función para añadir texto a la imagen
def add_text(img, coord1, coord2, text):
    # Dimensiones del rectángulo
    box_width = coord2[0] - coord1[0]
    box_height = coord2[1] - coord1[1]
    # Tamaño inicial y cálculo de escala
    font_scale = 1  # Escala inicial
    thickness = 2
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
    # Calcular la escala necesaria para ajustar el texto al área disponible
    scale_width = box_width / text_size[0]
    scale_height = box_height / text_size[1]
    font_scale = min(scale_width, scale_height)  # Multiplicador de margen

    # Calcular la posición del texto para centrarlo
    text_x = coord1[0]
    text_y = coord2[1]

    img = cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), 2)

    return img


# Función para pasar a escala de grises la parte de la imagen fuera de las coordenadas
def gray_outside_frame_img(img, coord1, coord2):
    # Elegir con las coordenadas la parte de la imagen que queremos a color
    box = img[coord1[1]:coord2[1], coord1[0]:coord2[0]]
    # Convertir la imagen a escala de grises
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Convertir la imagen en escala de grises, pero con 3 canales
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # Reemplazar en la imagen en escala de grises la parte que nos interesa por la guardada antes a color
    img[coord1[1]:coord2[1], coord1[0]:coord2[0]] = box
    # Mostrar cuadrado en las coordenadas
    cv2.rectangle(img, coord1, coord2, (0, 0, 255), 5)

    return img
