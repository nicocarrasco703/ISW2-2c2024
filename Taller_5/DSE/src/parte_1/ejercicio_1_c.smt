; Ejercicio 1 c) ¬(x ∧ y) ≡ ¬(¬x ∧ ¬y)
(declare-const x Bool)
(declare-const y Bool)
(assert ( = (not(and x y)) (not (and (not x) (not y)))))
(check-sat)

