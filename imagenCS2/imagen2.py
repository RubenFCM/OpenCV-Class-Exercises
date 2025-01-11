# Importar libreria cv2
# Instalar cv2  pip3 install opencv-python
import cv2
import os


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

def box_color_inverter_v2(ruta, coordX, coordY, in_box):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)

    x1, x2 = coordX
    y1, y2 = coordY
    if (in_box):
        box = imagen[y1:y2, x1:x2]
        # Invertir los colores de la imagen completa
        imagen = cv2.bitwise_not(imagen)
        # Reemplazar la zona del box en la imagen completa
        imagen[y1:y2, x1:x2] = box
    else:
        box = imagen[y1:y2, x1:x2]
        # Invertir los colores del box
        box_invertida = cv2.bitwise_not(box)
        # Reemplazar la ROI original con la invertida
        imagen[y1:y2, x1:x2] = box_invertida

    save_image_v2(ruta, '_invcua_V2', imagen)
