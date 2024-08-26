from volume import pi_value
def volume_cone():
    return (1/3)*pi_value()*h*(r**2)
h = int(input('what is the value of the heigth of the cylinder: '))
r = int(input('what is the value of the radius of the cylinder: '))

print(volume_cone())
