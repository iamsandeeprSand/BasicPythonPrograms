#Find out what all a person can afford by giving the amount as input which he/she is ready to spend for food or juice.
money=int(input("money "))    #meals-Rs.100, Snacks-Rs.50, Juice-Rs.20, Water-Rs.0
if money>=170:
    print("meals,snacks,juice")
elif money>=150 and money<170:
    print("meals & snacks or meals & juice")
elif money>=120 and money<150:
    print("meals & juice or juice & snacks")
elif money>=100 and money<120:
    print("meals or snacks & juice")
elif money>=70 and money<100:
    print("snacks & juice")
elif money>=50 and money<70:
    print("snacks or juice")
elif money>=20 and money<50:
    print("juice")
else:
    print("water") 
#Output gives the possibility of what all can that person afford for the amount given in input.
