(define (make-list lst)
    (if (not (null? lst)) (cons (car lst) (make-list (cdr lst))) '()))

(define (make-kwlist1 keys values)
    (cons keys values))

(define (get-keys-kwlist1 kwlist)
    (car kwlist)
)

(define (get-values-kwlist1 kwlist)
    (cdr kwlist)
)
(define (make-kwlist2 keys values)
    (if (null? keys) '()
    (cons (cons (car keys) (cons (car values) '())) (make-kwlist2 (cdr keys) (cdr values))))
)

(define (get-keys-kwlist2 kwlist)
  (if (null? kwlist) '()
  (cons (car (car kwlist)) (get-keys-kwlist2 (cdr kwlist))))
)

(define (get-values-kwlist2 kwlist)
  (if (null? kwlist) '()
  (cons (car (cdr (car kwlist))) (get-values-kwlist2 (cdr kwlist))))
)

(define (length lst)
    (define (f lst n)
        (if (null? lst) n (f (cdr lst (+ n 1)))))
    (f lst 0))

(define (append lst n)
    (if (null? lst) (if (list? n) n (list n))
    (cons (car lst) (append (cdr lst) n))))

(define (add-to-kwlist kwlist key value)
  ; kwlist 1
  ; we cant detect when there total 4 elements in the list because both keyword list and value list are both consist of two elements
  (cond ((= (length kwlist) 2) (cons (append (get-keys-kwlist1 kwlist) key) (append (get-values-kwlist1 kwlist) value)))
        ; kwlist 2
        (else (append kwlist (list key value)))))

(define (get-first-from-keylist kwlist key valuelst)
    (define (f lst n)
        (if (null? lst) nil
        (if (= (car lst) key) (get-index valuelst n) (f (cdr lst) (+ n 1)))))
    (f kwlst 0))

(define (get-index lst n)
    (define (f index valuelst)
        (if (= index n) (car valuelst) (f (+ 1 index) (cdr (valuelst)))))
    (f lst 0))

(define (get-first-from-kwlist kwlist key)
  ;implement get-first-from-kwlist, which implements support for getting the first value bound to a key in kwlist. 
  ;If key is not present in the list, 
  ;the function should return nil to indicate that there were no valid keys found.
  (cond ((= (length kwlist) 2) (get-first-from-keylist (get-keys-kwlist1 kwlist) key (get-values-kwlist1 kwlist)))
        (else (get-first-from-keylist (get-keys-kwlist2 kwlist) key (get-values-kwlist2 kwlist))))
)

(define (prune-expr expr)
    """
    scm> (prune-expr '(+ 10 20))
    (+ 10)
    scm> (prune-expr '(+ 10 20 30))
    (+ 10 30)
    scm> (eval (prune-expr '(+ 10 20 30)))
    40
    """
    (define (prune-helper lst)
      (if (or (null? lst) (null? (cdr lst)))
        lst
        (cons (car lst) (prune-helper (cdr(cdr lst)))))
    )
    (cons (car expr) (prune-helper (cdr expr)))
)

(define (curry-cook formals body)
    """
    scm> (curry-cook '(a) 'a)
    (lambda (a) a)
    scm> (curry-cook '(x y) '(+ x y))
    (lambda (x) (lambda (y) (+ x y)))
    """
    (if (null? formals) body `(lambda (,(car formals)) ,(curry-cook (cdr formals) body)))
)

(define (curry-consume curries args)
    """
    scm> (define three-curry (curry-cook '(x y z) '(+ x (* y z))))
    three-curry
    scm> three-curry
    (lambda (x) (lambda (y) (lambda (z) (+ x (* y z)))))
    scm> (define three-curry-fn (eval three-curry)) ; three-curry-fn is a lambda function derived from the program
    three-curry-fn
    scm> (define eat-two (curry-consume three-curry-fn '(1 2))) ; pass in only two arguments, return should be a one-arg lambda function!
    eat-two
    scm> eat-two
    (lambda (z) (+ x (* y z)))
    scm> (eat-two 3) ; pass in the last argument; 1 + (2 * 3)
    7
    scm> (curry-consume three-curry-fn '(1 2 3)) ; all three arguments at once
    7
    """
    (if (null? args) 
        curries
        (curry-consume (curries (car args)) (cdr args)))
)