get_budgets = [
  { "name": "John", "age": "21", "budget": 23000 },
  { "name": "Steve",  "age": "32", "budget": 40000 },
  { "name": "Martin",  "age": "16", "budget": 2700 }
]
result = 0
def find_budjet(object,res):
    for x in object:
        for value in x.values():
            if type(value) == int:
                res += value
    return res
print(find_budjet(get_budgets,result))