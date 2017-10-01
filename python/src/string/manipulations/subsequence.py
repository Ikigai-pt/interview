# Ref : substring.js for details on the question
# Author : Prakash Thirunavukkarasu

def sub_sequence(inp_string, sub_str):
    i_len = len(sub_str) - 1
    i = 0
    for c in inp_string:
        if c == sub_str[i]:
            if i == i_len:
                return True
            i += 1
    return False

print sub_sequence("abdcefg", "dfa")
print sub_sequence("abdcefg", "ace")
print sub_sequence("abdcefg", "dce")
print sub_sequence("abdcefg", "bfg")
print sub_sequence("abdcefg", "adefb")

