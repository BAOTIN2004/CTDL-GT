def de_quy(n,cot_a,cot_b,cot_c):
    if n==0: return 
        
    
    
    de_quy(n-1,cot_a,cot_c,cot_b)
    print(f'{n} {cot_b} qua {cot_a}')
    # de_quy(n-1,c,b,a)
    
de_quy(5,'a','b','c')