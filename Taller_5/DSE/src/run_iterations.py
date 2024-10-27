import os
import sys

from src.utils import get_result_and_model

if __name__ == '__main__':
    root_folder = "parte_2/ejercicio_7"

    if len(sys.argv) > 1:
        root_folder = sys.argv[1]

    # ejecuta cada .smt de la carpeta parte_2/ejercicio_5
    for file in sorted(os.listdir(root_folder)):
        if not file.endswith('.smt'):
            continue

        file_path = f"{root_folder}/{file}"
        print(f'*** Corriendo {file}')

        result, model = get_result_and_model(file_path)

        print("Resultado: ", result)

        if model:
            print("Modelo: ", model)
        print()

