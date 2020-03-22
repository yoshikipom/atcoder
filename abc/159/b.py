S = input()
N = len(S)
result = True

if S != S[::-1]:
    result = False

S2 = S[0:int((N-1)/2)]
if S2 != S2[::-1]:
    result = False

S3 = S[int((N+1)/2):]
if S3 != S3[::-1]:
    result = False

if result:
    print("Yes")
else:
    print("No")
