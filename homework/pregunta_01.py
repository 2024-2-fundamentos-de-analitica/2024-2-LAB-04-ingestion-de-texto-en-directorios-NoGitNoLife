# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import zipfile
import os
import pandas as pd


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
def pregunta_01():
    import zipfile
    import os
    import pandas as pd


    # Paso 1: Descomprimir el archivo input.zip
    zip_file = 'files/input.zip'
    output_dir = '.' # Extraer en la raíz del proyecto
    #adaptado ya que sacanba /input/input/

    
    # Verificar si el directorio de salida ya existe, si no, crearlo
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Descomprimir el archivo zip
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    


    output_dir = 'input' #adaptado ya que sacanba /input/input/

    # Paso 2: Función para leer los archivos de texto y etiquetarlos con su sentimiento
    def leer_archivos(directorio):
        data = []
        # Recorremos las carpetas "negative", "positive", "neutral"
        for sentiment in ['negative', 'positive', 'neutral']:
            sentiment_dir = os.path.join(directorio, sentiment)
            for file_name in os.listdir(sentiment_dir):
                file_path = os.path.join(sentiment_dir, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    phrase = file.read().strip()
                    data.append({'phrase': phrase, 'target': sentiment})
        return data

    # Paso 3: Leer los datos de entrenamiento y prueba
    train_data = leer_archivos(os.path.join(output_dir, 'train'))
    test_data = leer_archivos(os.path.join(output_dir, 'test'))

    # Paso 4: Crear los DataFrames y escribir los archivos CSV
    train_df = pd.DataFrame(train_data)
    test_df = pd.DataFrame(test_data)

    # Verificar si la carpeta de salida "output" existe, si no, crearla
    output_folder = 'files/output/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Guardar los archivos CSV
    train_df.to_csv(os.path.join(output_folder, 'train_dataset.csv'), index=False)
    test_df.to_csv(os.path.join(output_folder, 'test_dataset.csv'), index=False)