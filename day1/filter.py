#names = ["sam","john","james"]
#map_name = map(len, names)
#print(list(map_name))

#for i in names:
#    print(len(i))


def too_old(x): return x > 30
ages = [22, 25, 29, 34, 56, 24, 12]
print(list(filter(too_old, ages)))

filtered_ages = [age for age in ages if too_old(age)]
print(filtered_ages)


