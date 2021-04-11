#Fib is just fibbonaci sequence
a = 0
b = 1
e = int(input("Please enter how many iterations of the fibbonaci sequence you want: "))
for i in range(e):
    c = a + b
    b = a
    a = c
    i = i+1
    print(str(i),":", a)
