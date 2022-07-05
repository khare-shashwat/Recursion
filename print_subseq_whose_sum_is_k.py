arr=[1,2,1]
n=len(arr)
k=2
def fun(ind=0,a=[],s=0):
    if(ind>=n):
        if(s==k):
            print(a)
            return
        else:
            return
    a.append(arr[ind])
    fun(ind+1,a,s+arr[ind])
    a.pop()
    fun(ind+1,a,s)

fun()
