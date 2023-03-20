def bai_1(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst

def bai_2(lst):
    a=set(lst)
    for item in a:
            print(f'{item,lst.count(item)}')
