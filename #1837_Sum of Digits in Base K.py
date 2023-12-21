n = input("Enter a number in base 10: ")
k = input("Enter a number in base whatever: ")
r = 0
while n:
    r = (int(n) % int(k)) + r
    n = int(n) // int(k)
print(r)
