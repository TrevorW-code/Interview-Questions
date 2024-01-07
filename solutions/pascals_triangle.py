class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = [[1]] # start off loop
                
        for i in range(numRows - 1): # already made first row
            
            temp = [0] + output[-1] + [0] # write new invisible nums to not point out of range

            row = [] # set new row as empty
            
            for j in range(len(output[-1]) + 1): # for the length of previous row + 1       
                
                row.append(temp[j] + temp[j+1]) # get nums at index & index + 1, return sum
            
            output.append(row) # append the new row
        
        return output