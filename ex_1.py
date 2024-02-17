def tub_bolmagan_generator(N):
    def tubmi(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    current_number = 0

    while count < N:
        if not tubmi(current_number):
            yield current_number
            count += 1
        current_number += 1


N = int(input("N ni kiriting: "))


gen_obj = tub_bolmagan_generator(N)


for qiymat in gen_obj:
    print(qiymat)
