import z3

if __name__ == '__main__':
    spec = """
    (declare-const x Bool)
    (declare-const y Bool)
    (assert ( = (not(and x y)) (or (not x)(not y))))
    (check-sat)
    """

    s = z3.Solver()
    s.add(z3.parse_smt2_string(spec))
    print(s.check())
    if s.check() == z3.sat:
        print(s.model())
