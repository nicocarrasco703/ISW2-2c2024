import unittest
import z3


class TestParte1(unittest.TestCase):
    def solve_and_get_model(self, file, expected_result=z3.sat):
        s = z3.Solver()
        s.from_file(file)
        self.assertEqual(expected_result, s.check())
        if s.check() == z3.sat:
            return s.model()
        else:
            return None

    def test_ej1_a_b(self):
        for subindex in ['a', 'b']:
            file = f"../src/parte_1/ejercicio_1_{subindex}.smt"
            model = self.solve_and_get_model(file)
            # check that x and y are booleans
            try:
                x = model.eval(z3.Bool('x'))
                y = model.eval(z3.Bool('y'))
            except z3.Z3Exception:
                self.fail("El modelo no tiene x e y como booleanos")
            # check the model is empty
            self.assertEqual(0, len(model))

    def test_ej1_c(self):
        file = "../src/parte_1/ejercicio_1_c.smt"
        model = self.solve_and_get_model(file)

        # y and x should satisfy: ¬(x ∧ y) ≡ ¬(¬x ∧ ¬y)
        try:
            x = model.eval(z3.Bool('x'))
            y = model.eval(z3.Bool('y'))
        except z3.Z3Exception:
            self.fail("El modelo no tiene x e y como booleanos")
        self.assertTrue(not (x and y) == (not (not x and not y)))

    def test_ej2_a(self):
        file = "../src/parte_1/ejercicio_2_a.smt"
        model = self.solve_and_get_model(file)

        try:
            x = model.eval(z3.Int('x')).as_long()
            y = model.eval(z3.Int('y')).as_long()
        except z3.Z3Exception:
            self.fail("El modelo no tiene x e y como enteros")
        # 3x + 2y = 36
        self.assertEqual(36, 3 * x + 2 * y)

    def test_ej2_b(self):
        file = "../src/parte_1/ejercicio_2_b.smt"
        model = self.solve_and_get_model(file)

        try:
            x = model.eval(z3.Int('x')).as_long()
            y = model.eval(z3.Int('y')).as_long()
        except z3.Z3Exception:
            self.fail("El modelo no tiene x e y como enteros")
        # 5x + 4y = 64
        self.assertEqual(64, 5 * x + 4 * y)

    def test_ej2_c(self):
        file = "../src/parte_1/ejercicio_2_c.smt"
        model = self.solve_and_get_model(file)

        try:
            x = model.eval(z3.Int('x')).as_long()
            y = model.eval(z3.Int('y')).as_long()
        except z3.Z3Exception:
            self.fail("El modelo no tiene x e y como enteros")
        # x ∗ y = 64
        self.assertEqual(64, x * y)

    def test_ej3(self):
        file = "../src/parte_1/ejercicio_3.smt"
        model = self.solve_and_get_model(file)

        try:
            a1 = model.eval(z3.Real('a1')).as_long()
            a2 = model.eval(z3.Real('a2')).as_long()
            a3 = model.eval(z3.Real('a3')).as_long()
        except z3.Z3Exception:
            self.fail("El modelo no tiene a1, a2 y a3 como reales")
        # a1 = 16 mod 2
        # a2 = 16 dividido por 4
        # a3 = El resto de la divisi´on entera de 16 por 5.
        self.assertEqual(16 % 2, a1)
        self.assertEqual(16 // 4, a2)
        self.assertEqual(16 % 5, a3)
