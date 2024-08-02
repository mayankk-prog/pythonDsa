def merge_sort(listt):
    if len(listt)>1:
        mid= len(listt)//2
        leftlist= listt[:mid]
        rightlist= listt[mid:]

        merge_sort(leftlist)
        merge_sort(rightlist)

        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                listt[k]=leftlist[i]
                i+=1
            else:
                listt[k]= rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            listt[k]= leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            listt[k]= rightlist[j]
            j+=1
            k+=1

mylist= [34,45,56,67,78,23,12,34,56,76]
merge_sort(mylist)
print(mylist)