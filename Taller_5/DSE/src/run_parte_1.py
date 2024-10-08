import os
import z3

from src.utils import get_result_and_model

if __name__ == '__main__':
    # ejecuta cada .smt de la carpeta parte_1
    for file in sorted(os.listdir('parte_1')):
        print(f'*** Corriendo {file}')

        result, model = get_result_and_model(f"parte_1/{file}")

        print("Resultado: ", result)

        if model:
            print("Modelo: ", model)
        print()
