import os
import re
import unittest

import pandas as pd

from src.utils import get_result_and_model, get_all_values_from_model


class TestSyntaxParte2(unittest.TestCase):
    def parse_inputs(self, data: str, tipo):
        if pd.isna(data):
            return {}
        return {k.lower(): tipo(v) for k, v in (x.split("=") for x in data.replace(" ", "").split(","))}

    def ruta_to_dict(self, ruta):
        ruta = ruta.lower()
        # obtengo todas las condiciones (i.e., c1, c2, c3, c4, etc) siempre es una c seguida de uno o mas numeros)
        condiciones = re.findall(r"c\d+", ruta)
        # obtengo si son true o false
        valores = [not bool(re.search(f"not {condicion}", ruta)) for condicion in condiciones]
        return dict(zip(condiciones, valores))

    def dse_syntax_checker(self, working_dir, file_name, type_to_convert):
        original_dir = os.getcwd()
        try:
            os.chdir(working_dir)
            file_name = file_name
            data = pd.read_csv(file_name)

            # renombro las columnas para que sea más fácil acceder a ellas
            data.columns = ["iteracion", "input", "ruta", "especificacion", "resultado", "renombres"]

            renombres = data["renombres"].dropna().to_list()
            data.drop(columns=["renombres"], inplace=True)

            previous_is_unsat = False
            for i, row in data.iterrows():
                iteracion = row["iteracion"]

                # si resultado anterior era unsat => no cambiamos de iteración
                self.assertTrue(iteracion or previous_is_unsat, f"Debería cambiar de iteración, fila {i}")

                if not previous_is_unsat:
                    # parseo el input y la ruta
                    if pd.isna(row["input"]):
                        self.fail(f"El input no tiene valores, fila {i}")
                    input_concreto = self.parse_inputs(row["input"], type_to_convert)

                    if pd.isna(row["ruta"]):
                        self.fail(f"La ruta no tiene valores, fila {i}")
                    ruta = self.ruta_to_dict(row["ruta"])

                # veo la especificación de Z3, el archivo debe existir o debe ser "END"
                especificacion = row["especificacion"]
                if "END" in especificacion.upper():
                    break

                self.assertTrue(os.path.exists(especificacion), f"El archivo no existe, fila {i}")

                # la especificación de Z3 debe correr y tener datos
                result, model = get_result_and_model(especificacion)
                resultado_tabla = row["resultado"]

                if resultado_tabla.lower() == "unsat":
                    previous_is_unsat = True
                else:
                    previous_is_unsat = False

                    # tanto el modelo como la tabla tienen datos
                    table_values = self.parse_inputs(resultado_tabla, type_to_convert)
                    self.assertTrue(table_values, f"La tabla no tiene valores, fila {i}")

                    model_values = get_all_values_from_model(model)
                    self.assertTrue(model_values, f"El modelo no tiene valores, fila {i}")
        finally:
            # return to previous directory
            os.chdir(original_dir)

    def test_ejercicio_5(self):
        self.dse_syntax_checker("../src/parte_2/ejercicio_5/", "ejercicio_5.csv", int)

    def test_ejercicio_6(self):
        self.dse_syntax_checker("../src/parte_2/ejercicio_6/", "ejercicio_6.csv", float)

    def test_ejercicio_7(self):
        self.dse_syntax_checker("../src/parte_2/ejercicio_7/", "ejercicio_7.csv", int)
