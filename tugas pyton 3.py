N = int(input("massukkan angka fibonacci: "))
ctr = 1
a = 1
b = 1
if ctr <= N:
    print(a)
    for i  in range (N):
        c = a+b
        a = b
        b = c
        ctr = ctr+1
        print (c)