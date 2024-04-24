viti = int(input("Vendos vitin: "))

if viti > 2020 or viti < 1548:
    print('Viti eshte gabim!')
else:
    if viti % 4 == 0 and (viti % 100 != 0 or viti % 400 == 0):
        print(f'Viti {viti} eshte vit i brishte.')
    else:
        print(f'Viti {viti} nuk eshte vit i brishte.')