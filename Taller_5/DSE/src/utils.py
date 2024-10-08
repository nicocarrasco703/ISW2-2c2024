import sys

import z3


def get_result_and_model(file_path):
    """
    Run the Z3 solver on the given file and return the result and model.

    :param file_path: The path to the SMT file.
    :return: A tuple with the result and the model.
    """
    s = z3.Solver()
    s.from_file(file_path)

    # si el solver no tiene ninguna regla
    if str(s) == "[]":
        print(f"No se completó la solución de {file_path}!\n")
        sys.exit(1)

    result = s.check()
    model = s.model() if result == z3.sat and "get-model" in open(file_path).read() else None

    return result, model


def get_all_values_from_model(model):
    """
    Extract all variable values from a Z3 model.

    :param model: The Z3 model.
    :return: A dictionary with variable names as keys and their values.
    """
    values = {}
    for decl in model.decls():
        values[decl.name()] = model[decl]
    return values
