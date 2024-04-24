a = int(input("Vendos numrin n: "))

if a > 100 or a < 1:
    print("Numri eshte gabim.")
else:
    sum_of_numbers = 0
    for x in range(1, a + 1):
        sum_of_numbers += x

    print(f"Shuma e numrave nga 1 deri ne {a} eshte: {sum_of_numbers}")