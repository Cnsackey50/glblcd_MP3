#def too_old(z):
    #z = x + y
  #  return z > 30
#ages = [22, 25, 29, 34, 56, 24, 12]
#print(list(filter(too_old(ages, ages))))

#filter
dict = [{'age':25, 'level':13},{'age':17, 'level':3},{'age':100,'level':2}]
def acceptable_student(x):
    age, level = x
    return((level>25) and (level >=2))
filtered_dict = list(filter(acceptable_student, dict))
print(filtered_dict)