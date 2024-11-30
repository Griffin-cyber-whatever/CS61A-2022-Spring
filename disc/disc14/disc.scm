(define (nondecreaselist s)
    (if (nul? s)
        nil
        (let ((rest (nondecreaselist (cdr s))))
            (if (or (null? (cdr s))) (> (car s) (car (cdr s)))
                (cons (list (car s))  rest)
                (cons (cons (car s) (car rest)) (cdr rest))
            ) ; recursive call itself by using rest when calling (cdr rest) it either traversed through all the elements or the next item is less
              ; than its next item which is calling this recursive function on the next of next item
        )
    )
)
(expect (nondecreaselist '(1 2 3 1 2 3)) ((1 2 3) (1 2 3)))

(expect (nondecreaselist '(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1))
        ((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1)))

(define (nondecreaselist s)
    (define (sublist s) ; create the sublist
        (if (null? s) nil
        (if (or (null? s) (> (car s) (car (cdr s))))
            nil
            (cons (car s) (sublist (cdr s))))))
    (define (rest s) ; move the cursor
        (if (null? s) nil
        (if (<= (car s) (car (cdr s)))
            (rest (cdr s))
            (cdr s)))))
    (cons (sublist s)) (nondecreaselist (rest s))

;Q6
;global in dynamically scope parent is the frame in which it was called
;global

;f1 global
;lexical
;f2 parent:global
;saddel -> dynamic
;f3 global
;f4 global
;horns 7 saddle 25
;no

(define (make-long-or args)
    (if (null? (cdr args)) (eval (car agrs))
    (if (car agrs) (eval (car agrs)) 
    (make-long-or (cdr agrs))))
)