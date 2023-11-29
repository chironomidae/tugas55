A=int(input("variabel 1: "))
B=int(input("variabel 2: "))
if A<B:
    print("A less than B") #true
elif A<B or B<A:
    print("B less than A")
    print("finish")
else: #false
    print("false or equal")
    