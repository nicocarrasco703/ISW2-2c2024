; c1_0 and c1_1
(declare-const n Int)
(declare-const c1_0 Bool)
(declare-const c1_1 Bool)
(assert (= c1_0 (< 0 n)))
(assert (= c1_1 (< 1 n)))

(assert (and c1_0 c1_1))
(check-sat)
(get-model)