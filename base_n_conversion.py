from math import floor

itin=[]

def itinerary(n, num, den, tuple):
  n=n%den
  i=n
  for m in range(tuple):
    if(i/den>=m/tuple):
      g=m
  itin.append(g)
  i=i*tuple
  if i==num:
    for m in range(len(itin)):
      print(itin[m], end="")
  else:
    itinerary(i, num, den, tuple)

def naryexpand(num, d):
  stack=[]
  if num==0:
    print("0",end="")
  else:
    while num!=0:
      stack.append(num%d)
      num=floor(num/d)
    for i in range(1,len(nary)+1):
      print(stack.pop(-1), end="")
  

k=0
print("This program inputs a rational number expressed as a fraction and outputs its n-ary expansion. \n")
num=int(input("Enter the numerator of your number: "))
den=int(input("Enter the denominator of your number: "))
tuple=int(input("Enter the base you want your number converted to: "))
print("Your number is: ",num,"/",den," in base 10.\n", end="")
print("Converted to base ",tuple," your number is: ", end="")
naryexpand(floor(num/den), tuple)
print(".", end="")
itinerary(num, den, tuple)
print(" repeating.", end="")
