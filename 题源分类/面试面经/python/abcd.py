#ABCD*4=DCAB

def abcd():
    for a in range(1,10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if int(str(a)+str(b)+str(c)+str(d)) * 4 == int(str(d)+str(c)+str(b)+str(a)):
                        return int(str(a)+str(b)+str(c)+str(d))
                    
if __name__ == "__main__":
    print(abcd())
    