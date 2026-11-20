class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()==t.length()){
            HashMap<Character, Integer> map = new HashMap<>();
            HashMap<Character, Integer> map2 = new HashMap<>();
            char[] S = s.toCharArray();
            char[] T = t.toCharArray();
            for(char ch:S){
                if(map.containsKey(ch)){
                    int temp = map.get(ch);
                    map.remove(ch);
                    map.put(ch,temp+1);
                } else {
                    map.put(ch,1);
                }
            }
            for(char ch:T){
                if(map2.containsKey(ch)){
                    int temp = map2.get(ch);
                    map2.remove(ch);
                    map2.put(ch,temp+1);
                } else {
                    map2.put(ch,1);
                }
            }
        return map.equals(map2);
        }
    return false;
    }
}
