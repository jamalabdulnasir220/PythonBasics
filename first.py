
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)
print(result)

lucky_numbers = [12, 34, 56, 43, 15, 78, 87]
friends = ["Jamal", "Abdallah", "Bawa", "Theophilus"]

friends.extend(lucky_numbers)
print(friends)

friends.append("Salman")
print(friends)

friends.insert(1, "Adam")
print(friends)

friends.remove("Salman")
print(friends)
