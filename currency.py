#To return the input amount in the least possible number of Indian currency notes and coins in Python
a=int(input("Enter value  for a "))
b=a//500 #500
c=a%500
d=c//200 #200
e=c%200
f=e//100 #100
g=e%100
h=g//50 #50
i=g%50
j=i//20 #20
k=i%20
l=k//10 #10
m=k%10
n=m//5 #5
o=m%5
p=o//2 #2
q=o%2
r=q//1 #1
print('FiveHundred',b)
print('TwoHundred',d)
print('Hundred',f)
print('fifty',h)
print('Twenty',j)
print('Ten',l)
print('Five',n)
print('Two',p)
print('One',r)
