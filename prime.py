num=int(input("Enter the number: "))
if num>1:
  for i in range(2,num):
    if num%i==0:
      print("Not a prime number")
    else:
      print("Prime number")
else:
  print("Not a prime number")
