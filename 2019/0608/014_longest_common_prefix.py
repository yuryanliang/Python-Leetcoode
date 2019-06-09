def longestCommonPrefix(strs):
    if not strs:
        return ""
    for i in xrange(len(strs[0])):
        print i
        for string in strs[1:]:
            if i>=len(string) or string[i]!=strs[0][i]:
                return strs[0][:i]
    return strs[0]


print longestCommonPrefix(["he", "heaven", "heavy"])
