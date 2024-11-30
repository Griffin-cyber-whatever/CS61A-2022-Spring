(define (over-or-under num1 num2) 
    (cond ((< num1 num2) -1)
          ((> num1 num2) 1) 
          (else 0)))

(define (make-adder num) 
    (define (f inc)
        (+ inc num))
    f)
    
(define (composed f g) 
    (define (h x)
        (f(g x)))
    h)

(define (square n) (* n n))

(define (pow base exp) 
    (if (= exp 0)
        1 
        (if (= (modulo exp 2) 0) 
            (square (pow base (quotient exp 2))) 
            (* base (pow base (- exp 1))))))
