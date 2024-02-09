get_student_names = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}
list = []
def get_value(object,lst):
    for value in object.values():
        lst.append(value)
        lst.sort()
    return lst
print(get_value(get_student_names,list))