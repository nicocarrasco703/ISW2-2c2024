; Ejercicio 2 b) 5x + 4y = 64
(declare-const x Int)
(declare-const y Int)
(assert (= (+ (* 5 x) (* 4 y)) 64))
(check-sat)
(get-model)


