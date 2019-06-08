
def Plus_one(d):
        for i in range(len(d)-1, -1,-1):
            if d[i]<9:
                d[i]+=1
                return d
            d[i]=0
        return [1]+d

if __name__=="__main__":
    Plus_one([1,2,3])