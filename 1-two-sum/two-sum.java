class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hs = new HashMap<Integer, Integer>();
        for (int i=0; i < nums.length; i++){
            if (hs.containsKey(target-nums[i])){
                int diff = target-nums[i];
                int x =hs.get(Integer.valueOf(diff));
                return new int[]{x, i};
            } else {
                hs.put(nums[i], i);
            }
        }
        return new int[]{1};
    }
}