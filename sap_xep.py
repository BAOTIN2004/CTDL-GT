# các loại sắp xếp.
# lưu ý các mã lệnh phía dưới đều là sắp xếp tăng dần.


def sap_xep_chon(lst):
    lst_1=lst.copy()
    for i in range(len(lst)-1):
        min=i
        for j in range(i+1,len(lst_1)):
            if lst_1[j]<lst_1[min]:
                min=j
        lst_1[min],lst_1[i]=lst_1[i],lst_1[min]
    return lst_1

# sắp XẾP NỔI 
def sap_xep_noi(lst):
    lst_1=lst.copy()
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst_1[i]>lst_1[j]:
                lst_1[i],lst_1[j]=lst_1[j],lst_1[i]
    return lst_1

def sap_xep_chen(lst):
    lst_1=lst.copy()
    for i in range(len(lst)):
        # 0,1,2
        # 1,4,3
        index=i
        value=lst_1[i]
        while( index>0 and(lst_1[index-1]>value)):
            lst_1[index]=lst[index-1]
            index-=1
        lst_1[index]=value
        print(lst_1[index])
    return lst_1

print(sap_xep_chen([1,4,3]))