def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b) 
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
gcd_1 = gcd(a, b)
print("НОД:", gcd_1)