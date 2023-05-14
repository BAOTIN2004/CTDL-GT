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
        print(f'Chuyển đĩa 1 từ {cot_a} sang {cot_c}  ')
        return
    thap_ha_noi(n-1,cot_a,cot_c,cot_b)
    print(f'Chuyển đĩa {n} từ { cot_a} sang {cot_c} ')      
    thap_ha_noi(n-1,cot_b,cot_a,cot_c)
thap_ha_noi(3,'A',"B","C")

# Chuyển đĩa 1 từ A sang C
# Chuyển đĩa 2 từ A sang B
# Chuyển đĩa 1 từ C sang B
# Chuyển đĩa 3 từ A sang C
# Chuyển đĩa 1 từ B sang A
# Chuyển đĩa 1 từ A sang C
