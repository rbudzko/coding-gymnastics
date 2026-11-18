class Solution {
    public boolean hasDuplicate(int[] nums) {
        final HashSet<Integer> seen = new HashSet<>();

        for (Integer num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        
        return false;
    }
}