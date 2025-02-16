def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return num, False
    print("[*] " + str(num) + " [*]")
    return str(num), True
def check():
    l = []
    for i in range(2, int(input("HASTA QUE NUMERO SE COMPROBARA? →  "))):
        n, b = prime(i)
        if b == True:
            l.append("[*]" + n + "[*]")
    f = open("primes.txt", "w")
    for a in l:
        f.write(a + "\n")
    f.close()
check()
