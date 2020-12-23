array_of_CookDict = []

def serch(choose, criterial):
    if choose == 1:
        for i in range(len(array_of_CookDict)):
            if array_of_CookDict[i]["Name_of_dish"] == criterial:
                print(array_of_CookDict[i])
    if choose == 2:
        for i in range(len(array_of_CookDict)):
            if array_of_CookDict[i]["Number_of_components"] == criterial:
                print(array_of_CookDict[i])
    if choose == 3:
        for i in range(len(array_of_CookDict)):
            if array_of_CookDict[i]["List_of_components"] == criterial:
                print(array_of_CookDict[i])
    if choose == 4:
        for i in range(len(array_of_CookDict)):
            if array_of_CookDict[i]["Time_for_cook"] == criterial:
                print(array_of_CookDict[i])

while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Вести дані про страву\n"
          "3. Кінець\n")

    choose = int(input("Напишітть цифру:"))

    if choose == 1:
        for i in range(len(array_of_CookDict)):
            print(array_of_CookDict[i])
    if choose == 2:
        Name_of_dish = input("Name of dish: ")
        Number_of_components = int(input("Number of components: "))
        List_of_components = input("List of components: ")
        Time_for_cook = int(input("Time for cook: "))

        CookDict = {"Name_of_dish": Name_of_dish, "Number_of_components": Number_of_components,
                    "List_of_components": List_of_components, "Time_for_cook": Time_for_cook}
        array_of_CookDict.append(CookDict)
    elif choose == 3:
        break
    else:
        print("Ведіть коректне число\n")
