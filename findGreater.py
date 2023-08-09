#five inputs are given as an int 
a=int(input("enter the vaue of a "))
b=int(input("enter the vaue of b "))
c=int(input("enter the vaue of c "))
d=int(input("enter the vaue of d "))
e=int(input("enter the vaue of e "))
if a>b:
 if a>c:
  if a>d:
   if a>e:
    print("a is bigger")
else:
  if b>a:
   if b>c:
    if b>d:
     if b>e:
      print("b is bigger")
   else:
     if c>a:
      if c>b:
       if c>d:
        if c>e:
         print("c is bigger")
       else:
         if d>a:
          if d>b:
           if d>c:
            if d>e:
             print("d is bigger")
            else:
              if e>a:
               if e>b:
                if e>c:
                 if e>d:
                  print("e is bigger")


#The output will give the greater number 
