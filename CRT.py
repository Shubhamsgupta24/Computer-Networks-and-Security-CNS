def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def chinese_remainder_theorem(remainders, mods):
    N = 1
    for modulus in mods:
        N *= modulus

    x = 0
    
    for bi, ni in zip(remainders, mods):
        Ni = N // ni 
        gcd, yi, xyz = extended_gcd(Ni, ni)  
        x += bi * Ni * yi 
    return x % N  

remainders = [1, 2, 3] 
mods = [3, 5, 7]   
for i in range(len(mods)):
    print("x=", remainders[i], "mod", mods[i])
solution = chinese_remainder_theorem(remainders, mods)
print("The solution is:", solution)
