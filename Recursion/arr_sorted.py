def sorted_array(ar,index):
    if(len(ar)==index):
        return True
    if(ar[index]<ar[index-1]):
        return False
    return sorted_array(ar,index+1)

print(sorted_array([1,2,3,4,5,6],1))