def quick_sort(listt):
    pivot= listt[0]
    lesser= [x for x in listt[1:] if x< pivot]
    greater=[x for x in listt[1:] if x> pivot]
    return quick_sort(lesser)+[pivot]+quick_sort(greater)