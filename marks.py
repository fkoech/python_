math = int(input("Maths:"))
English =int(input("English:"))
Science =int( input("Science:"))
Kiswahili = int(input("Kiswahili:"))
Social = int( input("Social:"))
total = math + English + Science + Kiswahili + Social
if total < 300:
   print( str(total) + " is for a subcounty school")
elif total > 300 and total < 350:
   print( str(total) + " is for county school")
else:
   print( str(total) + " is for a national school")

        

