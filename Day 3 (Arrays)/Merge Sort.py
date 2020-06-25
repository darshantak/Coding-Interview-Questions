def mergesort(array):   
    inv_count=0
    if len(array)>1:
        
        mid=len(array)//2
        l=array[:mid]
        r=array[mid:]

        mergesort(l)
        mergesort(r)

        i=j=k=0
        
        while i<len(l) and j<len(r):
            if l[i]>r[j]:
                array[k]=r[j]
                j+=1
                k+=1
            else:
                array[k]=l[i]
                inv_count += (mid-i + 1)
                i+=1
                k+=1
    
        while i<len(l):
            array[k]=l[i]
            i+=1
            k+=1
        
        while j<len(r):
            array[k]=r[j]
            j+=1
            k+=1
    return inv_count
    
arr=[12, 13, 11, 6, 7, 5]
print(mergesort(arr))
