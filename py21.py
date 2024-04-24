num_students = int(input('Vendos nr e studentve:'))
shuma = 0

for i in range(1, num_students + 1):
    nota = float(input(f"Vendos noten e nxenesit te {i}: "))
    shuma += nota

mesararja = shuma / num_students
print("Mesatarja e mesatareve eshte:", mesararja)
