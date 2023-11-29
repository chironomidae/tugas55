name = input("enter your name: ")
num = int(input("enter a number: "))
if num < 10:
    for i in range(0,num):
        print(name)
else: 
    for i in range (0,3):
        print ("too high")
        