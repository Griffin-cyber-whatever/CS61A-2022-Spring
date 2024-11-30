; Creates the rational number n/d (Assume n, d are integers and d != 0)
; Note that the constructor simplifies the numerator and denominator.
(define (pair n d)
    (cons n (cons d nil)))

(define (first lst)
    (car lst))

(define (rest lst)
    (car (cdr lst)))

(define (rational n d)
    (pair n d))

; Gets the numerator of rational number r
(define (numer r)
    (first r))

; Gets the denominator of rational number r
(define (denom r)
    (rest r))

; Adds two rational numbers x and y
(define (add-rational x y)
    (rational (+ (* (numer x) (denom y)) (* (numer y)(denom x)))(* (denom x) (denom y))))

; Multiplies two rational numbers x and y
(define (mul-rational x y)
    (rational (* (numer x) (numer y)) (* (denom x) (denom y))))

; Constructs tree given label and list of branches
(define (tree label branches)
    (pair label branches))

; Returns the label of the tree
(define (label t)
    (first t))

; Returns the list of branches of the given tree
(define (branches t)
    (cdr t))
; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t)
    (if (null? (branches t))
        #t
        #f))