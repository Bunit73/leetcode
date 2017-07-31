// https://leetcode.com/submissions/detail/111902731/
public class Solution {
    public bool IsAnagram(string s, string t) {
        char[] sStr = s.ToArray();
        char[] tStr = t.ToArray();
        
        Array.Sort(sStr);
        Array.Sort(tStr);
        
        return sStr.SequenceEqual(tStr);
    }
}
