
class Solution {
    public int maxArea(int[] heights) {
        int l=0;
        int r=heights.length-1;
        int maxvol = 0;
        while(r>l){
            maxvol=Math.max(maxvol,((r-l)*Math.min(heights[l], heights[r])));
            if(heights[l]<heights[r]){
                l++;
            } else {
                r--;
            }
        }
    return maxvol;
    }
}
