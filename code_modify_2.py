def get_2CirclesArea(Radius1, Radius2):
    Pi = 3.141592
    Area1 = Radius1 ** 2 * Pi
    Area2 = Radius2 ** 2 * Pi

    if Area1 > Area2:
        Area = Area1 - Area2
    else: # Modified Source Code
        Area = Area2 - Area1
    return Area
    
S1 = get_2CirclesArea(5, 50)
S2 = get_2CirclesArea(3, 30)
S3 = get_2CirclesArea(7, 9)

print(S1)
print(S2)
print(S3)