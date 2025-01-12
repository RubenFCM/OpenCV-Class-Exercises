# Importar libreria cv2
# Instalar cv2  pip3 install opencv-python
import cv2
import os
import base64


# Función para guardar una imagen en la carpeta img
def save_image(ruta, text, img):
    # Usar os.path.splitext() para separar el nombre y la extensión
    nombre, extension = os.path.splitext(ruta)
    # Crear la nueva ruta con el nombre modificado y la misma extensión
    nueva_imagen = nombre + text + extension
    # La guardamos en memoria en un fichero distinto y devolvemos la ruta
    cv2.imwrite(nueva_imagen, img)


###########################################################################################
# Ejercicio 1
# Crea una función que pasándole la ruta de una imagen, la rote 180 grados y genere una
# nueva imagen.
###########################################################################################
def rotateImage(ruta):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    imagen_rotate = cv2.rotate(imagen, cv2.ROTATE_180)
    # Redimensionar las imágenes a un tamaño más pequeño
    imagen_resized = cv2.resize(imagen, (400, 300))
    imagen_resized_rotate = cv2.resize(imagen_rotate, (400, 300))

    save_image(ruta, '_rotated', imagen_rotate)

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

    save_image(ruta, '_negative', imagen_negative)

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
    # imagen_resized = cv2.resize(imagen, (400, 300))
    # imagen_resized_gray = cv2.resize(imagen_gray, (400, 300))

    save_image(ruta, '_gray', imagen_gray)

    # Mostrar imagenes
    # cv2.imshow('Imagen Original', imagen_resized)
    # cv2.imshow('Imagen en escala de grises', imagen_resized_gray)
    # Esperar hasta que el usuario presione una tecla
    # cv2.waitKey(0)  # Espera hasta que se presione cualquier tecla
    # Cerrar todas las ventanas de OpenCV
    # cv2.destroyAllWindows()
    return imagen_gray


###########################################################################################
# Ejercicio 4
# Crea una función que pasándole la ruta de una imagen, marque un cuadrado a partir de
# dos coordenadas.
###########################################################################################
def box_face_by_cordinates(ruta, coord1, coord2, color):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    box_face = cv2.rectangle(imagen, coord1, coord2, color, 5)

    # imagen_resized_box = cv2.resize(box_face, (800, 600))

    save_image(ruta, '_box', box_face)

    # Mostrar imagen
    # cv2.imshow('Imagen con cuadrado', imagen_resized_box)
    # Esperar hasta que el usuario presione una tecla
    # cv2.waitKey(0)  # Espera hasta que se presione cualquier tecla
    # Cerrar todas las ventanas de OpenCV
    # cv2.destroyAllWindows()

    return box_face


###########################################################################################
# Ejercicio 5
# Crea una función que pasándole la ruta de una imagen, invierta los colores de un cuadrado
# a partir de dos coordenadas, pasadas por parámetro.
###########################################################################################

def box_color_inverter(ruta, coord1, coord2):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)

    x1, y1 = coord1
    x2, y2 = coord2
    box = imagen[x2:y2, x1:y1]
    # Invertir los colores del box
    box_invertida = cv2.bitwise_not(box)
    # Reemplazar la ROI original con la invertida
    imagen[x2:y2, x1:y1] = box_invertida

    imagen_resized = cv2.resize(imagen, (800, 600))

    save_image(ruta, '_invcua', imagen)

    # Mostrar la imagen resultante
    cv2.imshow("Imagen con colores invertidos", imagen_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


###########################################################################################
# Ejercicio 6
# Crea una función que pasándole la ruta de una imagen, la recorte para evitar dimensiones
# con valores impares
###########################################################################################

def resize_image(ruta):
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    alto, ancho, canales = imagen.shape
    print(f"Alto: {alto} píxeles")
    print(f"Ancho: {ancho} píxeles")

    if alto % 2 != 0:
        alto -= 1
    if ancho % 2 != 0:
        ancho -= 1
    print('Imagen redimensionada')
    print(f"Alto: {alto} píxeles")
    print(f"Ancho: {ancho} píxeles")

    # Redimensionar la imagen para que sus dimensiones sean pares
    image_resized = imagen[0:alto, 0:ancho]

    save_image(ruta, '_resized', image_resized)


###########################################################################################
# Ejercicio 7
# Crea una función que pasándole la ruta de una imagen, retorne la imagen espejada
###########################################################################################

def mirror_image(ruta):
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)

    mirror_image = cv2.flip(imagen, 1)

    # imagen_resized = cv2.resize(imagen, (400, 300))
    # imagen_resized_mirror = cv2.resize(mirror_image, (400, 300))

    # cv2.imshow('Imagen Original', imagen_resized)
    # cv2.imshow('Imagen Espejo', imagen_resized_mirror)

    save_image(ruta, '_mirror', mirror_image)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return mirror_image


###########################################################################################
# Ejercicio 8
# Crea una función que pasándole la ruta de una imagen, invierta la mitad izquierda y la
# copie en la derecha.
###########################################################################################

def horizontal_half_mirror_image(ruta):
    # Cargar la imagen
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    # Obtener las dimensiones de la imagen original
    alto, ancho, canales = imagen.shape

    imagen[:, ancho // 2:] = cv2.flip(imagen[:, :ancho // 2], 1)

    # cv2.imshow('Imagen mitad espejo', imagen)

    save_image(ruta, '_halfmirrorH', imagen)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return imagen


###########################################################################################
# Ejercicio 9
# Crea una función que pasándole la ruta de una imagen, invierta la mitad superior y la copie
#  en la inferior, efecto espejo por la horizontal.
###########################################################################################

def vertical_half_mirror_image(ruta):
    # Cargar la imagen
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    # Obtener las dimensiones de la imagen original
    alto, ancho, canales = imagen.shape

    imagen[alto // 2:, :] = cv2.flip(imagen[:alto // 2, :], 0)

    # cv2.imshow('Imagen mitad espejo', imagen)

    save_image(ruta, '_halfmirrorV', imagen)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return imagen


###########################################################################################
# Ejercicio 10
#  Crea una función que pasándole la ruta de una imagen, genere un documento html donde
#  muestre la imagen original y las generadas en las tres funciones anteriores en una tabla
###########################################################################################

def generate_html(ruta, filename):
    image_0 = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    image_1 = mirror_image(ruta)
    image_2 = horizontal_half_mirror_image(ruta)
    image_3 = vertical_half_mirror_image(ruta)

    # Convertir imágenes a base64 para incrustarlas en el HTML
    img_0_base64 = image_to_base64(image_0)
    img_1_base64 = image_to_base64(image_1)
    img_2_base64 = image_to_base64(image_2)
    img_3_base64 = image_to_base64(image_3)

    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabla de Imágenes Generadas</title>
        <style>
            table {{
                width: 50%;
                margin: auto;
            }}
            th, td {{
                padding: 10px;
                text-align: center;
            }}
            img {{
                max-width: 300px;
                max-height: 300px;
            }}
        </style>
    </head>
    <body>
        <h1>Tabla de Imágenes Generadas</h1>
        <table>
            <tr>
                <td>
                    <p>Imagen Original</p>
                    <img src="{img_0_base64}" alt="Imagen Original">
                </td>
                <td>
                    <p>Imagen Espejo</p>
                    <img src="{img_1_base64}" alt="Imagen Espejo">
                </td>
            </tr>
            <tr>
                <td>
                    <p>Espejo Mitad Horizontal</p>
                    <img src="{img_2_base64}" alt="Espejo Mitad Horizontal">
                </td>
                <td>
                    <p>Espejo Mitad Vertical</p>
                    <img src="{img_3_base64}" alt="Espejo Mitad Vertical">
                </td>
            </tr>
        </table>
    </body>
    </html>
    '''
    save_html(html, filename)
    return html


# Función para pasar una imagen a base64
def image_to_base64(image):
    _, buffer = cv2.imencode('.png', image)
    base64_image = base64.b64encode(buffer).decode('utf-8')
    return f"data:image/png;base64,{base64_image}"


# Función para guargar un html generado en la carpeta html
def save_html(html, filename):
    # Obtener la ruta del directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta hacia la carpeta "html" un nivel arriba
    parent_dir = os.path.dirname(current_dir)
    html_dir = os.path.join(parent_dir, "html")

    # Asegurarse de que la carpeta "html" exista
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)

    # Ruta completa del archivo
    filepath = os.path.join(html_dir, filename)

    # Guardar el HTML en un archivo
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(html)


###########################################################################################
# Ejercicio 11
# Crea una función que pasándole la ruta de una imagen, además de marcar un cuadrado a
# partir de dos coordenadas, como se hizo en el ejercicio 4, añada un texto en la parte inferior
# del cuadrado.
###########################################################################################

def box_and_text_image(ruta, coord1, coord2, box_color, text):
    imagen = box_face_by_cordinates(ruta, coord1, coord2, box_color)

    imagen_txt = cv2.putText(imagen, text, (coord1[0] + 10, coord2[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, box_color, 2)

    # cv2.imshow('Imagen con cuadrado y texto.', imagen_txt)

    save_image(ruta, '_box&text', imagen_txt)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


###########################################################################################
# Ejercicio 12
# Crea una función que pasándole la ruta de una imagen, emborrone una zona determinada
###########################################################################################

def box_blur_image(ruta, coord1, coord2):
    # Cargar la imagen en memoria
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)

    # Extraer las coordenadas
    x1, y1 = coord1
    x2, y2 = coord2

    # Extraer el ROI (box)
    box = imagen[y1:y2, x1:x2]
    # Aplicar desenfoque al box
    box_blur = cv2.GaussianBlur(box, (99, 99), 0)
    # Reemplazar la ROI original con la desenfocada
    imagen[y1:y2, x1:x2] = box_blur

    # Guardar la imagen con el sufijo "_blurred"
    save_image(ruta, '_blurred', imagen)


###########################################################################################
# Ejercicio 13
# Crea una función que pasándole la ruta de una imagen, detecte y marque las
# caras de dicha imagen utilizando la funcionaliad de CV2. Esta librería posibilita la detección de
# objetos mediante aprendizaje automático en cascada. Podemos entrenar nuestros propios
# clasificadores, pero para este ejercicio utilizaremos un clasificador preentrenado que puedes
# encontrar en el gitHub de OpenCV (opencv/data/haarcascades/)
###########################################################################################

def face_detector_img(ruta_img, blur=False):
    cascade_path = "haarcascade_frontalface_default/haarcascade_frontalface_default.xml"
    # Cargar el clasificador Haar para detección de rostros.
    face_cascade = cv2.CascadeClassifier(cascade_path)
    # Leer la imagen
    imagen = cv2.imread(ruta_img)
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detectar caras
    # scaleFactor=1.1: Reduce la imagen en un 10% en cada iteración para detectar rostros de diferentes tamaños.
    # minNeighbors=5: Define cuántos rectángulos adyacentes deben agruparse para considerar que se ha detectado una cara.
    # minSize=(30, 30): Tamaño mínimo de las caras a detectar.
    caras = face_cascade.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar rectángulos alrededor de las caras detectadas
    for (x, y, w, h) in caras:
        print(f'x ={x}, y={y}, w={w}, h={h}')
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if (blur):
            # Extraer región de la cara
            rostro = imagen[y:y + h, x:x + w]
            # Aplicar un desenfoque Gaussian
            rostro_blur = cv2.GaussianBlur(rostro, (99, 99), 30)
            # Reemplazar la región original con la desenfocada
            imagen[y:y + h, x:x + w] = rostro_blur

    # Guardar el resultado
    save_image(ruta_img, '_face', imagen)
