m = int(input("son kriting :"))
skate_painting_shous =  {"skate": 200, "painting": 200, "shoes": 1 }
resulte = 0
for x in skate_painting_shous.values():
    resulte += x
print(resulte - m)