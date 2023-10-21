def fb_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a, b
        a, b = b, a + b
        count += 1

def kolicnik(n):
    for i, (x, y) in enumerate(fb_generator(n)):
        i += 1
        try:
            kol = float(y) / float(x)
            print("Količnik za par", i, ":", kol)
        except ZeroDivisionError:
            print("Količnik za par", i, ":", "oo")

n = int(input("Unesite broj n: "))

for num in fb_generator(n):
    print(num)

kolicnik(n)

