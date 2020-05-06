def je_prastevilo(stevilo):
    if stevilo < 2:
        return False
    elif stevilo % 2 and stevilo =! 2:
        return False
    kandidat = 3
    while kandidat ** 2 <= stevilo:
        if n % kandidat == 0:
            return False
        else:
            kandidat += 2
    return True

for i in range(200):
    if je_prastevilo(i):
        print(i)