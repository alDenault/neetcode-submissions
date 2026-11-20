class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet set = new HashSet<>();
        int max = 0;
        for(int i:nums){
            set.add(i);
        }
        for(int num:nums){
            if(!set.contains(num-1)){
                int temp=1;
                while(set.contains(num+temp)){
                    temp+=1;
                }
                max = Math.max(temp,max);
            }
        }
        return max;
    }
}
