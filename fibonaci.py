def fibonaci(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
        
        
        print 'i-->',i,'c===>',c
        

if __name__ == '__main__':
    fibonaci(10)
    
        
