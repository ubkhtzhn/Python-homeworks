# # # 1. is_prime(n) funksiyasi
# # # is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

def is_prime(a):
    if a<2:
        return False
    if a == 2:
        return True
    c = int(a**0.5)
    for n in range(2, c+1):
        if a%n==0:
            return False
    return True

# # # 2. digit_sum(k) funksiyasi
# # # digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

def digit_sum(k):
    return sum(int(n) for n in str(k))


# # # 3. Ikki sonning darajalari
# # # Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

def kvadrat(k):
    n = 1
    while 2**n <= k:  
        print(2**n, end =" ")
        n += 1 

kvadrat(16)
