(declare-const a Int)
(declare-const b Int)
(declare-const c Int)
(assert (not (or (<= a 0) (or (<= b 0) (<= c 0)))))
(assert (not (and (> (+ a b) c) (and (> (+ a c) b) (> (+ b c) a)))))
(check-sat)
(get-model)