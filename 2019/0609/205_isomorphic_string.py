def isIsomorphic (self, s, t):
    hashmap={}
    mapval={}
    for i in xrange(len(s)):
        if s[i] not in hashmap:
            hashmap[s[i]]=t[i]


        elif hashmap[s[i]]!=t[i]:
            return False

    mapval=[hashmap[k] for k in hashmap]
    return len(mapval)==len(set(mapval))