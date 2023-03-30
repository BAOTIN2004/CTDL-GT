def ucln(m,n):
    for i in range(min(m,n),0,-1):
        if m%i==0 and n%i==0: 
            return i

def thap_ha_noi(n,cot_a,cot_b,cot_c):
    if n==1: 
        print(f'Chuyển đĩa {n} từ {cot_a} sang {cot_c}  ')
        return
    thap_ha_noi(n-1,cot_a,cot_c,cot_b)
    print(f'Chuyển đĩa {n} từ { cot_a} sang {cot_c} ')      
    thap_ha_noi(n-1,cot_b,cot_a,cot_c)
n=int(input('Nhap so dia:\t'))
thap_ha_noi(n,"a","b","c")
        
        