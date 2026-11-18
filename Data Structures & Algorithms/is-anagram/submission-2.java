class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> balance = new HashMap<>();

        for (int i=0; i<s.length(); i++) {
            balance.merge(s.charAt(i), 1, (a, b) -> a + b);
            balance.merge(t.charAt(i), -1, (a, b) -> a + b);
        }

        return balance.values().stream().allMatch(v -> v == 0);
    }
}
