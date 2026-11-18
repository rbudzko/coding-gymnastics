class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            freq.merge(num, 1, (sum, next) -> sum + next);
        }

        return freq.entrySet()
            .stream()
            .sorted((a, b) -> b.getValue() - a.getValue())
            .limit(k)
            .mapToInt(e -> e.getKey())
            .toArray();
    }
}
