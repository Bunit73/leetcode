//https://leetcode.com/submissions/detail/111289684/
public class Solution {
    public int TitleToNumber(string s) {
        int val = 0;
        int powVal = s.Length - 1;
        int idx = 0;
        for(int i = 0; i < s.Length; i++){
            idx = char.ToUpper(s[i]) - 64;
            if(powVal > 0){
                val += (int)Math.Pow(26,powVal) * idx;
                powVal--;
            }
            else{
                val += idx;
            }
        }
        return val;
    }
}
