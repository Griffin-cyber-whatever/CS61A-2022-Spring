def fibo(n):
    pred, curr = 1,0
    index = 0
    while index < n:
        pred, curr = pred, pred + curr
        index += 1
    return curr
        
                
        
#sequeces
def seq(n,term):
    sum, k = 0, 1
    while k <= n:
        sum, k = sum + term(n), k+1