name = input("soz va sonlar kriting : ")
name2 = []
name3 = []
name4 = {

}
for x in name:
    if x.isdigit():
        name2.append(x)

    if x.isalpha():
        name3.append(x)
name4["LETTERS"] = len(name2)
name4["DIGITS"] = len(name3)
print(name4)