###example1(a) of list in python###
# retrieving a specific item in the list
#a=["banana", "apple", "microsoft"]
#print(a[0])
#print(a[1])
#print(a[2])
#print(a[2])





##example1(b) of a list in python ###
# retrieving a specific item in the list
#a = ["kale", "cabbage", "tomato"]
#print(a[0])




 
 
 
 
# ## example2 of list in python ###
#b= [2,4,5,6,7,7]
#print(b)






### example3 of list in python ###
##it  shows the results of a adding an element to a list
#b = [1,2,3,4,5,6]
#b.append(7)
#print(b)




### example4 of a list in python #####
# one different feature of python unlike other programming languages is that it can hold different datatypes in a single list
#c =[1,2,3,4,5,6,67]
#c.append("felix")
#print(c)


####example5 of a list in python #####
# a list can also contain another list
#d = [1,1,3,4,5,5,6,]
#d.append([6,6,78,8])
#print(d)





# example6 of a  list in python ###
# deleting an element from the list ie the last element in the list
#  pop is a predefined function 
#e = [2,4,5,6,7,8]
#e.pop()
#print(e)






##example7 of a list in python ###
##changing a value of an element in the list ###
#f = [2,4,5,6,7,8,9,0]
#f[7] = 10
#7 denotes the seventh index position in the list
#print(f)







  
####example1 of a  for loop in python#######
###it helps in simplifying retrieval of elements in a list
#(for element in a) it simple says that for each elements in the list a 
#a = [20, 30, 40, 60]
#for element in a:
#   print(element)
#   print(element)





#####example2 of a for loop in python######
#b = [2,3,5,6,7,8,9,11,12,13,14,15]
#for e in b:
#      print(e)



### example3 of a for loop in python ###
#c=[3434, 39595, 394959]
#total = 0
#for e in c:
#         total = total + e
#print(total)
#



###example4 of a for loop in python ##
#c = [596969, 305969, 4050505]
#total =0
#for e in c:
#    total = total*e
#print(e)






###exampl5 of for loop in python####
#total = 0
#for i in range(1,8):
#    total += i
#print(total)







## example6 of for loop in python combined with a list
#given_list = [5, 6, 8, -2, -1]
#total = 0
#for element in given_list :
#    total += element
#
#print(total)









#### example7 of a for loop in python which will break the loop after certain condition is made
#given_list = [4, 6,7,8,9,9,-2, -1]
#total = 0
#i = 0
#for i in given_list:
#    if i < 4:
#        break
#    total += i
#print(total)








##Example8 of a for loop in python 
#a = ["Maize", "millet", "white", "Balcum"]
#for list in a:
#    print(a)
#for i in range(4):
#    print(a[i])
#





# example9 of a for loop in python##
# used in the case where the index matters
#a = ["beans", "peas", "ground nuts"]
#for i in range(len(a)):
#    print(a[i])
#

 
#example10 of a for loop in python ###
#for the case where you want to print "apple" once, "banana" twice and "oranges" three time"
#a = ["apple", "banana", "orange"]
#for i in range(len(a)):
#    for j in range (i + 1):
#        # i = 0 -> j = 0
#        # i = 1 -> j = 0, 1
#        # i = 2 -> j = 0, 1, 2
#        print(a[i])
#






#### example1 of a range in python####
##1,2, 3, 4
#the below range means that start a range at 1 and end at 5 but not include 5
#c = list(range(1,5))
#print(c)
#for i in range(1, 5):
#    print(i)
#



#range example2 in python #####
#c = list(range(1, 56))
#total = 0
#for e in range(1, 56):
#    total += e
#print(e)
#






###range example3 in python #####
# find the sum of multiples of 3 in a range
#total1 = 0
#for i in range(1, 25):
#    if i % 3 == 0:
#        total1 += i
#print (total1)
#




## question1 for for loop and a given range  in python ###
#can you compute all multiples of 3, 5  in the range 1 to 100
#####solution1#####
#total = 0
#for i in range(1, 100):
#    if i % 3 == 0:
#        total += i
#    elif i % 5 == 0:
#        total += i
#print(total)
####solution2##3
#total = 0
#for i in range(1,100):
#    if i % 3 ==0 or i% 5 ==0:
#        total += i
#print(total)







##question2 
### find the sum of only the positive numbers in the give_list =[7, 3,5,6,6,-1,-2,-5,-6, -7,-30]
##solution1
#given_list = [7,3,5,6,6,-1,-2,-5,-6,-7,-30]
#total = 0
#j = len(given_list) - 1
#while given_list[j] <  0:
#    total += given_list[j]
#    j-=1
#print(total)
 
 



#total = 0
#for i in range(1,10000):
# total += i
# print(total)


#total2 = 0
#for i in  range(1, 100):
#   total2 +=i
#
#print(total2)
#



# if condition
#total2 = 0
#for i in range(1, 231):
#    if i % 3 == 0:
#        total2 += 1
#        print(total2)



#a = 39495
#print(a)



#b = "my name is Felix Koech Cherop"
#c = "a student of catholic university of eastern Africa"
#d = "I am a christian ,brought up from a catholic denomination"
#e = "and i am in third year in computer science venturing in cybersecurity"
#print(b+c+d+e)










# a variable represence a value in python 
# a variable can be reassigned a new value in python
#a=4
#b=a
#print(b)
#a=6
#print(b)





####example1 of swapping in python####
#swapping of variable is a pit complex in python therefore the is need to introduce an extra variable which will represent the first variable, will the first variable then be allowed to repreent the second variable and then  the second variable be assigned the first variable for example
#vi = 40
#v2 = 50
#temp = vi
#vi = v2
#v2 = temp
#print(vi)
#print(v2)





###example2 of swapping in python ######
#g =["avacado", "mangoes", "banana", "orange"]
#temp = g[0]
#g[0] = g[3]
#g[3] = temp
#print(g)






## example3 of swapping items in a list in python ###
#b = ["leasure", "recreation", "reading"]
#b[0], b[2] = b[2], b[0]
#print(b)





#if Else Statement example1 in python
# python is sensitive and whatever statement to be excuted should be intended atleast 4 space in the conditional statement
#for example
#a = 20
#b = 30
#if a > b:
#    print("a is greater than b")
#print("not sure if any of them is greater")







##### if else statement example2 in python######
#c = 50
#d = 50
#if c > d:
#    print("c is larger than d")
#else:
#    print("d is greater than c")
#print("  the two values are equal")







####### if else example3 in python######
#e = 70
#f = 70
#if e > f:
#    print("e is greater than f")
#elif e == f:
#    print ("both e and f are equal")
#else:
#    print("f is greater than e")







####if else statement example4 in python#######
#g = 80
#h = 50
#if g < h:
#   print("g is less than h")
#else:
#    if g == h:
#      print("g is equal to h")
#    else:
#        print("g is greater than h")
#






#### a simple calculator for calculating the BMI #####
#name = "Felix"
#height_m = 2
#weight_kg = 90
#bmi = weight_kg / (height_m ** 2)
#print("bmi:")
#print(bmi)
#if bmi > 20:
#    print(name)
#    print("is an overweight")
#else:
#    print(name)
#    print("the bmi is ok")
#





##Functions in python#########
### how to use functions in python#######
#a function is a collection of codes or instuctions
## example1 of function in python
#def functionname1():
#    print("mimi nasoma")
#    print("nasidi kusoma")
#print("saidi kusoma")
#functionname1()# it is used to call whatever it is contained in the function to excution
#





#Example2 of functions in python#####
# a function can be considered a mapping since it maps one value to a return argument
#def functioname2(x):
#    #x is an input or a n argument
#    return 2*x
#a = functioname2(3)
## this will tell use 3 and call the function functioname2
#print(a)
#b=functioname2(4)
#print(b)
#c= functioname2(30405)
#print(c)
#


####example3 of function in python####
# a function can have more than one argument
#for example
#def functionname3(a,b,c,d):
#    return a/d+c*d-(a+b+c+d)
#e = functionname3(30, 20, 40, 4)
#print(e)





##example4 of function in python########
#collection of python as a collection of instructions and as a mapping
#def functioname4(x):
#    print("this argument")
#    print("is too large")
#    return 3*x
#f = functioname4(5)
#print(f)
#







##### example5 of function in python ########
##BMI calculator for more than one persons ###
#name1 = "Felix"
#height_m1 = 3
#weight_kg1 = 64.6
#
#name2 = "Jelimo"
#height_m2 = 2
#weight_kg2= 70
#
#name3 = "sharon"
#height_m3 = 2
#weight_kg3 = 42.1
#
#name4 = "amanda"
#height_m4 = 0.8
#weight_kg4 = 19.2
#
#name5 = "Aiden"
#height_m5 = 0.6
#weight_kg5 = 14.07
#
#def bmi_calculator(name, height_m, weight_kg):
#    bmi = weight_kg/(height_m **2)
#    print("bmi:")
#    print(bmi)
#    if bmi < 25:
#        return name + " is not overweight"
#    else:
#        return name + " is an overweight"
#
#result1 = bmi_calculator(name1, height_m1, weight_kg1)
#print(result1)
#result2 = bmi_calculator(name2, height_m2, weight_kg2)
#print(result2)
#result3 = bmi_calculator(name3, height_m3, weight_kg3)
#print(result3)
#result4 = bmi_calculator(name4, height_m4, weight_kg4)
#print(result4)
#result5 = bmi_calculator(name5, height_m5, weight_kg5)
#print(result5)
#















####Example1 of a while loop in python####
#total1 = 0
#j = 4
#while j < 5:
#    total1 += j
#    j +=1
#print(total1)
#





####example2 of a while loop in python ####
#give_list = [5, 4, 4, 3, 1, -2,-3, -5]
#total = 0
#i = 0
#while give_list[i] > 0:
#    total += give_list[i]
#    i += 1
#print(total)
#print(i)





# example3 of a while loop in python ###
#### len is a predefined function in python, it is used to find the length of a sequence ie characters in a string, check number of  elements  in a python list
#given_list = [5, 4, 3, 2, 1]
#total = 0
#i = 0
#while i < len(given_list) and  given_list[i] > 0:
#    total += given_list[i]
#    i += 1
#print(total)






## example4 of while loop in python ####
#`given_list = [3,5,6,7,7,-3,-2,-3]
#`total=0
#`i=0
#`while True:
#`    total += given_list[i]
#`    i += 1
#`    if given_list[i] <= 0:
#`        break
#`print(total)






####Dictionaries in python######
#example1 of a dictionaries in python###
#d = {}
#also a dictionary can be defined by d = dict{}
#defining new dictionary with the values ie d = {"George":24, "Tom":30}
#d["Felix"] = 23 # it says add a value key pair Felix with the value 23
#d["Vivian"]= 25
#d["Philemon"]= 28
#print(d["Felix"])
#print(d["Vivian"])









#### Example2 of dictionaries in python ####
# it is posible to change the value of a certain key ie 
#d = {}
#d["Felix"] =20
#print(d["Felix"])
#d["Felix"] = 23
#print(d["Felix"])








# a key are commonly string or numbers
#example3 of keys being numbers  dictionary in python  ####
#d = {}
#d[10] = 100
#print(d[10])






###how to iterate over key value pairs
## example4 of dictionaries in python ####
#d = {}
#d["Felix"] = 40
#d["Jesus"] = 1000
#for key, value in d.items():
#    print("key:")
#    print(key)
#    print("value:")
#    print(value)
#    print("")










###class in python
##Example1 of classes in python ##
#class Robot:
#    def introduce_self(self):
#        print("my name is " + self.name)
#        print("my color is" + self.color)
#        
#
#r1 = Robot()
#r1.name = "Tom"
#r1.color ="red"
#r1.weight =30
#
#r2 = Robot()
#r2.name = "james"
#r2.color = "blue"
#r2.weight ="46"
#r2.introduce_self()
#r1.introduce_self()








