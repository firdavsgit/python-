
adversaries = ["a", "b", "c"]
resulte = {

}
for x in adversaries:
    m = x.casefold()
    n = x.capitalize()
    resulte[m] = n
print(resulte)