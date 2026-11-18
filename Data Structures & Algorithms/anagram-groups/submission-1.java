class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for (String s : strs) {
            groups.computeIfAbsent(hash(s), k -> new ArrayList<String>()).add(s);
        }

        return new ArrayList<>(groups.values());
    }

    private String hash(String s) {
        int[] h = new int[26];

        for (char c : s.toCharArray()) {
            h[c - 'a']++;
        }

        return Arrays.toString(h);
    }
}
