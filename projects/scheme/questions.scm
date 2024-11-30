(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  (define (f s index)
    (if (null? s)
        '()  ; If the list is empty, return an empty list
        (cons (list index (car s))  ; Create a pair (list index value)
              (f (cdr s) (+ index 1)))))  ; Recursively call f with the rest of the list and increment the index
  (f s 0))  ; Start with index 0


  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to INORDER? and return
;; the merged lists.
(define (merge inorder? list1 list2)
  (cond ((null? list1) list2)  ; If list1 is empty, return list2
        ((null? list2) list1)  ; If list2 is empty, return list1
        ((inorder? (car list1) (car list2))  ; Correctly check the order between the first elements of the lists
         (cons (car list1) (merge inorder? (cdr list1) list2)))  ; Add the first element of list1 to the result
        (else (cons (car list2) (merge inorder? list1 (cdr list2))))))  ; Add the first element of list2 to the result
 ; END PROBLEM 16


;; Optional Problem 1

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           'replace-this-line
           ; END PROBLEM 17
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           'replace-this-line
           ; END PROBLEM 17
           ))
        (else
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )))



;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'replace-this-line
  )
  ; END Question 21