class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] found = new int[2];
        HashMap<Integer, Integer> pairs = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            pairs.put(nums[i],i);
        }
        for(int i=0;i<nums.length;i++){
            int diff = target - nums[i];
            if(pairs.containsKey(diff) && i!=pairs.get(diff)){
                return new int[]{Math.min(i, pairs.get(diff)),Math.max(i,pairs.get(diff))};
            }
        }
    return new int[0];
    }
}
