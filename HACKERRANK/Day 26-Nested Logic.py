actually = str(input()).split(" ")
d = int(actually[0])
m = int(actually[1])
y = int(actually[2])

expected = str(input()).split(" ")
de = int(expected[0])
me = int(expected[1])
ye = int(expected[2])

fine = 0
if y > ye:
    fine = 10000
elif y == ye:
    if m > me:
        fine = (m - me) * 500
    elif m == me and d > de:
        fine = (d - de) * 15
print(fine)
