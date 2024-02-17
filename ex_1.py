def tub_bolmagan_sonlar(N):
    def tublar(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    joriy_son = 0

    while count < N:
        if not tublar(joriy_son):
            yield joriy_son
            count += 1
        joriy_son += 1


N = int(input("N ni kiriting: "))


obyekt_g = tub_bolmagan_sonlar(N)


for qiymat in obyekt_g:
    print(qiymat)
