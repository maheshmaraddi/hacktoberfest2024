year = int(input(" which year do u like to choose"))

if year % 4 == 0:
 if year % 100 == 0:
  if year % 400 == 0:
   print("this is a leap year")
  else:
   print("this is not a leap year")
 else:
  print("this a leap year")
else:
    print("its not a leap year")
