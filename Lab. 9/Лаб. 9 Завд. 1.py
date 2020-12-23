arrayOfmelomanDict = []

def serch(choose, criterial):
    if choose == 1:
        for i in range(len(arrayOfmelomanDict)):
            if arrayOfmelomanDict[i]["Group"] == criterial:
                print(arrayOfmelomanDict[i])
    if choose == 2:
        for i in range(arrayOfmelomanDict):
            if arrayOfmelomanDict[i]["Songs"] == criterial:
                print(arrayOfmelomanDict[i])
    if choose == 3:
        for i in range(arrayOfmelomanDict):
            if arrayOfmelomanDict[i]["nameSong"] == criterial:
                print(arrayOfmelomanDict[i])

while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні про групу\n"
          "3. Вийти\n")

    choose = int(input("Напишітть цифру:"))

    if choose == 1:
        for i in range(len(arrayOfmelomanDict)):
            print(arrayOfmelomanDict[i])
    elif choose == 2:
        Group = input("Group: ")
        Songs = input("Songs: ")
        nameSong = input("Name Song: ")

        melomanDict = {"Group": Group, "Songs": Songs, "nameSong": nameSong}
        arrayOfmelomanDict.append(melomanDict)
    elif choose == 3:
        break
    else:
        print("Ведіть коректне число\n")