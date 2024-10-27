; c1_0 and c1_1 and c1_2
(declare-const n Int)
(declare-const c1_0 Bool)
(declare-const c1_1 Bool)
(declare-const c1_2 Bool)
(assert (= c1_0 (< 0 n)))
(assert (= c1_1 (< 1 n)))
(assert (= c1_2 (< 2 n)))

(assert (and c1_0 (and c1_1 c1_2)))
(check-sat)
(get-model)