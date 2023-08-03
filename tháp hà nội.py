# sử dụng vòng lặp thong thường
def ucln(m,n):
    for i in range(min(m,n),0,-1):
        if m%i==0 and n%i==0: 
            return i
# sử dụng đệ quy
def ucln1(a, b):
    if a == 0 or b == 0:
        return a if b == 0 else b
    else:
        return ucln1(b, a % b)

def thap_ha_noi(n,cot_a,cot_b,cot_c):
    if n==1: 
        print(f'Chuyen dia 1 tu {cot_a} sang {cot_c}  ')
        return
    thap_ha_noi(n-1,cot_a,cot_c,cot_b)
    print(f'Chuyen dia {n} tu { cot_a} sang {cot_c} ')
    thap_ha_noi(n-1,cot_b,cot_a,cot_c)
#thap_ha_noi(3,'A',"B","C")


# giai thua 
def giai_thua(n):
    if n==1:
        return 1
    return n*giai_thua(n-1)
giai_thua(4)
