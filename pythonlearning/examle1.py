n = int(input("Enter a number: "))
a = 0 
b = 1
print("Fibonacci sequence:")
print(a, b, end=" ")
for _ in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c 
