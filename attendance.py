attendance=[18,20,19,15,21]

fulldays=0
total_attendance=0
for students in attendance:
   if students >=20:
      print("FULL")
      fulldays +=1
   else:
      print("NOT FULL")
      total_attendance += students
      print("full days:",fulldays)
      print("total attendance:",total_attendance)
