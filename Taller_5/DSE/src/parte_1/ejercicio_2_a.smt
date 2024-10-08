; Ejercicio 2 a) 3x + 2y = 36
(declare-const x Int)
(declare-const y Int)
(assert (= (+ (* 3 x) (* 2 y)) 36))
(check-sat)
(get-model)
