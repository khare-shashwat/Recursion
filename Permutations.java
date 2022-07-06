// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;

class Permutations {
    public static void main(String[] args) {
        int[] nums={1,2,3};
        int[] map = new int[nums.length];
        for(int i=0;i<nums.length;i++)
            map[i]=0;
        System.out.println(myFun(nums,map,new ArrayList(),new ArrayList()));
    }
    
    public static List<List<Integer>> myFun(int[] nums,int[] arr,List<Integer> ds,List<List<Integer>> ans){
        if(ds.size()==nums.length){
            ans.add(new ArrayList(ds));
            return ans;
        }
        for(int i=0;i<nums.length;i++){
            if(arr[i]==1)
                continue;
            ds.add(nums[i]);
            arr[i]=1;
            myFun(nums,arr,ds,ans);
            arr[i]=0;
            ds.remove(ds.size()-1);
        }
        return ans;
        
    } 
}
