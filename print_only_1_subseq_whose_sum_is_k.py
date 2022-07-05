arr=[1,2,1]
n=len(arr)
k=2
def fun(ind=0,a=[],s=0):
    if(ind>=n):
        if(s==k):
            print(a)
            return True
        return False
    a.append(arr[ind])
    if(fun(ind+1,a,s+arr[ind])==True):
        return True
    a.pop()
    if(fun(ind+1,a,s)==True):
        return True
    return False

fun()
        
