ditet= int(input('Numri i diteve:'))
oret = int(input('Numri i orev:'))
minutat= int(input('Numri i minutave:'))
sekontat = int(input('Numri i sekontave:'))

conv1 = ditet * 86400
conv2 = oret * 3600
conv3 = minutat * 60

convertimi = conv1 + conv2 + conv3

print(f'Koha prej {ditet} dite, {oret} ore , {minutat} minuta dhe {sekontat} sekonta eshte gjithsej {convertimi} sekonta.')