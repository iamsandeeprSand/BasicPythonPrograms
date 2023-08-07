#Calculation of Simple Interest
def SI(P,T,R):
    SimInt = (P * T * R)/100  # S.I = (PTR)/100
    return SimInt


a = input().split()  #Three values are given as the input. Values correspond to Principle amount, Interest Rate and Time in that particular order.
                      #separated by space

# a is in the form of list so the values of P,R & I are equated by calling the index as folows
P = float(a[0]) # P = Principle amount
R = float(a[1]) # R = Interest Rate
T = float(a[2]) # T = Time 

Ans = SI(P,T,R)

print('{:.2f}'.format(Ans)) # Output is given in the format of up to two decimal places
