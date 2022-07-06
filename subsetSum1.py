#print the sum of all possible subsets in increasing order
def subsetSum(ind,arr,s,ans):
    if(ind==len(arr)):
        ans.append(s+0)
        return
    subsetSum(ind+1,arr,s+arr[ind],ans)
    subsetSum(ind+1,arr,s,ans)
    return sorted(ans)

print(subsetSum(0,[3,1,2],0,[]))
