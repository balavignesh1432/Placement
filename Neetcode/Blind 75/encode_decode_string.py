# Can Simply join using delin, But string can contain delimiter itself
# So convert each character into ascii, the use delim for each character (:)
# For each word, use another delim, (#)
# So now encoded string contains only numbers for characters in the string, and # and : only
# TC: O(N * K), SC: O(N * K), where N is no. of strings, K is avg length of string
# Ascii digits is max 3 ( 0 - 255), so TC is optimal
def encode(self, strs):
    encoded = []
    for string in strs:
        for c in string:
            encoded.append(str(ord(c)))     # Convert to ascii 
            encoded.append(":")             # End of each character
        encoded.append("$")                 # For end of word
    return "".join(encoded)

def decode(self, s):
    res = []
    i = 0
    while i < len(s):   
        string = ""                     # For each word added to list
        while s[i] != "$":              # Find end of word
            ascii = ""                  # Appended Each digit 
            while s[i] != ":":          # End of ascii number (Each digit)
                ascii += s[i]
                i += 1
            character = chr(int(ascii))     # Total ascii number is converted to character
            string += character             # Added to string
            i += 1
        res.append(string)              # If reached end of word, add string to result list
        i += 1
    return res