import time

def fibonacci(idx):
    seq = [0, 1]
    for a in range(idx):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

def Fibonacci(idx):
    if idx <= 1 :
        return idx
    else:
        return Fibonacci(idx-1)+Fibonacci(idx-2)

print("***** recursion *****" )
rec = time.time()
print(Fibonacci(8))
print("speed : " +  str(time.time()-rec))

print("***** iteration *****"76yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy€$hbbbbb*6/+bg6-)
print(fibonacci(8))
print("speed : " +  str(time.time()-rec))