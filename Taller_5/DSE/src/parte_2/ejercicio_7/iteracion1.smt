; c1_0
(declare-const n Int)
(declare-const c1_0 Bool)
(assert (= c1_0 (< 0 n)))

(assert c1_0)
(check-sat)
(get-model)