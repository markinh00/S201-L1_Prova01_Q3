def multiply(array: list, number: float):
    for element in array:
        print(f"{element} x {number} = {element * number}")

    return None


list_of_number = []
for i in range(30, -1, -1):
    list_of_number.append(i)

while True:
    user_input = input("Digite um número: ")
    try:
        user_input = float(user_input)
        break
    except Exception as error:
        print(error)


multiply(list_of_number, user_input)
