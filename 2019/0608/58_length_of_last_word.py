def lengthOfLastWord(s):
    length=0
    for i in reversed(s):
        if i==" ":
            if length :
                break
        else:
            length+=1
    return length

def l2(s):
    return len(s.strip().split(" ")[-1])