# https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/
# Count number of substrings with exactly k distinct characters
# Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
# Examples:

# Input: abc, k = 2
# Output: 2
# Possible substrings are {"ab", "bc"}

# Input: aba, k = 2
# Output: 3
# Possible substrings are {"ab", "ba", "aba"}

# Input: aa, k = 1
# Output: 3
# Possible substrings are {"a", "a", "aa"}

#code
def nDistinctSubString(k, text):
    print("is it working %i" %ord('a'))
    input = list(text)
    if (k <= 0 or len(input) < k):
        return -1
    maxNumSubSet = 0
    for i in range(0, len(input)):
        distinctChar = [0] * 26
        counter = 0
        for j in range(i, len(input)):
            index = ord(input[j]) - ord('a')
            if (distinctChar[index] == 0):
                counter+=1
                distinctChar[index] = 1
            if( counter == k ):
                maxNumSubSet+= 1
                print(" i %i j %i coutner %i index %i" %(i,j, counter, index))

    return maxNumSubSet

text2 = "hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs"
text = "aaa"
print(nDistinctSubString(2, text2))
