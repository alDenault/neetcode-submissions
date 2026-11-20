class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> charset = new HashMap<>();
        int l = 0;
        int r = 0;
        int max = 0;
        while(r<s.length()){
            if(charset.getOrDefault(s.charAt(r),-1)>=l){
                l=Math.max(charset.get(s.charAt(r))+1, l);
            }   
            charset.put(s.charAt(r),r);
            max=Math.max(max, r-l+1);    
            r++;     
        }
        return max;
   }
}
