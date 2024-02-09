maximum_score = [
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]

result = 0
def find_all(object,res):
    for x in object:
        for value in x.values():
            if type(value) == int:
                res += value
    return res
print(find_all(maximum_score,result))