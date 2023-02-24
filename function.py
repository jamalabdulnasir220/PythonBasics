def sayhi(name):
    print("Hello " + name)


sayhi("Jamal")


def cube_number(num):
    return num * num * num


print(cube_number(3))

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")

elif is_male and not is_tall:
    print("You are a male and short")


else:
    print("You are not a male nor tall")
