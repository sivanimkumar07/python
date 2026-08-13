attendance=[18,20,19,15,21]

fulldays=0
total_attendance=0
for students in attendance:
   total_attendance += students
   if students >=20:
      print("FULL")
      fulldays +=1
   else:
      print("NOT FULL")

print("full days:",fulldays)
print("total attendance:",total_attendance)
