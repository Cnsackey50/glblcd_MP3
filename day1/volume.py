def pi_value():
    return 22/7

def volume_cylinder():
    return pi_value()*h*(r**2)
h = int(input('what is the value of the heigth of the cylinder: '))
r = int(input('what is the value of the radius of the cylinder: '))

print(volume_cylinder())