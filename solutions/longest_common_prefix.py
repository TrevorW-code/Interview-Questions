class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        
        # for the index of the first word
        for idx in range(len(strs[0])):
            
            # for the word in the list 
            for word in strs:
                
                # if the index is the same as the length of the word
                # OR
                # the letter at the index of the word is not the same as the letter at the same index in the first word
                if idx == len(word) or word[idx] != strs[0][idx]:
                    
                    # end the loop and return answer
                    return prefix
                
            #other add the letter to prefix from the first word
            prefix += strs[0][idx]
                
        return prefix
