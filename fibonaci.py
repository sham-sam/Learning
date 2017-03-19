from __main__ import name
def fibonaci(n):
    a = 0
    b = 1
    c = 0
    for i in n:
        c = a + b
        b = a
        b = c
        print 'i-->',i,'c===>',c
        

if name == '__main__()':
    fibonaci(10)
    
        
