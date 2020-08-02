# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    S = str(input())
    print (S[::2], S[1::2])
