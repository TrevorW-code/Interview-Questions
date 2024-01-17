class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Comparing two hash maps
        char_counter_input = {}
        char_counter_test = {}

        for char in s:
            if char not in char_counter_input:
                char_counter_input[char] = 1
            else:
                char_counter_input[char] = char_counter_input[char] +1

        for char in t:
            if char not in char_counter_test:
                char_counter_test[char] = 1
            else:
                char_counter_test[char] = char_counter_test[char] + 1
        
        if char_counter_input == char_counter_test:
            return True
        else:
            return False