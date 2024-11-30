(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s)))

(define (caddr s) 
    (car(cddr s)))

(define (ascending? lst) 
    (if (and (null? (cddr lst)) 
        (<= (car lst) (cadr lst)))
        #t
        (if (<= (car lst) (cadr lst))
            (ascending? (cdr lst))
            #f)))


(define (interleave lst1 lst2)
    (if (not(or (null? lst1) (null? lst2)))
            (cons(car lst1) (interleave lst2 (cdr lst1 )))
            (if (null? lst1) lst2 lst1) 
        )
    )


(define (my-filter func lst)
    (if (not (null? lst))
        (if (func (car lst))
            (cons (car lst) (my-filter func (cdr lst)))
            (my-filter func (cdr lst)))
        nil))


(define (no-repeats lst) 
    (if (null? lst)
        nil
        (cons (car lst) (no-repeats (remove-given (cdr lst) (car lst) )))))

(define (remove-given lst key)
    (if (null? lst)
        '()
        (if (= (car lst) key)
            (remove-given (cdr lst) key)
            (cons (car lst) (remove-given (cdr lst) key))
        )
    ))
