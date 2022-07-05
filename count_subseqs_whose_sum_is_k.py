arr=[1,2,1]
n=len(arr)
k=2
def fun(ind=0,s=0):
    if(ind>=n):
        if(s==k):
            return 1
        return 0
    l=fun(ind+1,s+arr[ind])
    r=fun(ind+1,s)
    return l+r

print(fun())
