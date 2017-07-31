//https://leetcode.com/submissions/detail/111896628/
public class Solution {
    public int MajorityElement(int[] nums) {
        double majBenchMark = (double)nums.Length/(double)2;
        var dict = new Dictionary<int,int>();
        foreach(int num in nums){
            if(dict.ContainsKey(num)){
                dict[num]++;
            } else{
                dict.Add(num,1);
            }
        }

        foreach(KeyValuePair<int,int> pair in dict){
            if(pair.Value > majBenchMark){            
                return pair.Key;
            }
        }
        
        return 0;
    }
}
