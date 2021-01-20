{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40  is geater than30\n"
     ]
    }
   ],
   "source": [
    "#specifies the number of condition to be executed\n",
    "\n",
    "#example of two comparison between two values\n",
    "a = 40\n",
    "b = 30\n",
    "if a>b:\n",
    "   print(str(a)  +\"  is geater than\" + str(b))\n",
    "else:\n",
    "    print(str(b)+\" is greater than \" + str(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You have passed Your exam with excellent grade\n",
      "You have passed with Good reward\n"
     ]
    }
   ],
   "source": [
    "#including the elif condition\n",
    "#the elif condition reduce the use of the more indendation in a condition.\n",
    "#example\n",
    "List = ['A', 'B',]\n",
    "for grade in List:\n",
    "    if grade == 'A':\n",
    "        print(\"You have passed Your exam with excellent grade\")\n",
    "    elif grade == 'B':\n",
    "         print(\"You have passed with Good reward\")\n",
    "    else:\n",
    "        print(\"Not recognised\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "110 is greater than 80\n"
     ]
    }
   ],
   "source": [
    "#for the case you dont want to use the the elif condition, you introduce another if clause within the else:\n",
    "#example:\n",
    "a = 110\n",
    "b = 80\n",
    "if a > b:\n",
    "    print(str(a) + \" is greater than \"  + str(b))\n",
    "else:\n",
    "    if a == b:\n",
    "        print(str(a) + \" is equal to \" + str(b))\n",
    "    else:\n",
    "        print(str(b) + \" is greater than \" + str(a))\n",
    "              \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Waswa bmi is 42.5\n",
      "Waswa is overweight with a bmi of 42.5\n"
     ]
    }
   ],
   "source": [
    "# a simple bmi calculator\n",
    "# hyphotheticly let us generate data for two client \n",
    "name = \"Waswa\"\n",
    "height_m = 2\n",
    "weight_kg = 170\n",
    "bmi = weight_kg /(height_m ** 2)\n",
    "print(name + \" bmi is \" + str(bmi))\n",
    "if bmi > 24.9:\n",
    "    print(name + \" is overweight with a bmi of \" + str(bmi))\n",
    "else:\n",
    "    if bmi < 24.9 and bmi > 10.4:\n",
    "        print(name + \" is very much health with the bmi of \"+ str(bmi))\n",
    "    else:\n",
    "        print(name + \" is is underweight with the bmi of \" + str(bmi))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# functions in python \n",
    "# what is function in python\n",
    "# it can be defined in two ways:\n",
    "\"\"\"                           - a  collection or set of codes.\n",
    "                              - A mapping,  input or argement maps the parameter.\n",
    "                              - Facilitates the  reuse of codes \"\"\"\n",
    "#can be defined with a def function.\n",
    "#Should end with full colon to mark the function clause.\n",
    "#example one as as collection of code:\n",
    "#has name, precided by the def function\n",
    "def function1():\n",
    "    print(\"am learning python\")\n",
    "    print(\"it will take me arround one month\")\n",
    "    print(\"after one month i will be intermidiate in it\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "am learning python\n",
      "it will take me arround one month\n",
      "after one month i will be intermidiate in it\n"
     ]
    }
   ],
   "source": [
    "#call the function or use by function\n",
    "function1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "#using a function as a mapping\n",
    "def function2(x, y, z):\n",
    "    return \"the sum of x ,y z  is \" + str(x+y+z)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'the sum of x ,y z  is 342322'"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#call the function function2\n",
    "function2(20000, 302020, 20302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "# using the function as both the mapping and the collection of of codes\n",
    "def function3(name, reg, course):\n",
    "    print(\"your details\")\n",
    "    return name, reg, course\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "your details\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "('felix', 1033994, 'computer science')"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "function3(\"felix\", 1033994, \"computer science\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "# a samehow complex Bmi caclculator\n",
    "#let us hyphothicly generate data for three people\n",
    "name1 = \"Felix\"\n",
    "weight1_kg = 74\n",
    "height1_m = 2.4\n",
    "\n",
    "name2 = \"vivian\"\n",
    "weight2_kg =49\n",
    "height2_m = 1.2\n",
    "\n",
    "name3 = \"Justine\"\n",
    "weight3_kg = 74.1\n",
    "height3_m = 2.3\n",
    "\n",
    "def function3(name, weight, height):\n",
    "    bmi = weight /(height**2)\n",
    "    if bmi > 24.9:\n",
    "        print(name + \" is overweight with bmi weight of \" + str(bmi))\n",
    "    else:\n",
    "        if bmi <24.9 and bmi > 14.9:\n",
    "            print(name +\" is very much health with bmi weight of\"+ str(bmi))\n",
    "        else:\n",
    "            print(name + \" is underweight and should take alot of food and the bmi weigh is \" + str(bmi))\n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Felix is underweight and should take alot of food and the bmi weigh is 12.847222222222223\n",
      "vivian is overweight with bmi weight of 34.02777777777778\n",
      "Justine is underweight and should take alot of food and the bmi weigh is 14.007561436672969\n"
     ]
    }
   ],
   "source": [
    "result1 = function3(name1, weight1_kg, height1_m)\n",
    "result2 = function3(name2, weight2_kg, height2_m)\n",
    "result3 = function3(name3, weight3_kg, height3_m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'banana', 'apple']\n"
     ]
    }
   ],
   "source": [
    "# a list in python\n",
    "#list is datatype just like array in other languages\n",
    "# it can be defined by introducing the square brackets \n",
    "# example:\n",
    "fruits = [\"mango\", \"banana\", \"apple\"]\n",
    "print(fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'banana', 'apple', 'lemon']\n"
     ]
    }
   ],
   "source": [
    "# how can i add an item to a list? , you simple used the append() function , example:\n",
    "fruits.append(\"lemon\")\n",
    "print(fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'banana', 'apple', 'lemon', 1]\n"
     ]
    }
   ],
   "source": [
    "#unlike other lunguages , list in python can contain data of verious types for example:\n",
    "fruits.append(1)\n",
    "print(fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'banana', 'apple', 'lemon', 1, ['tomato', 'carrots', 'onion']]\n"
     ]
    }
   ],
   "source": [
    "# list can also contain other list for example:\n",
    "fruits.append([\"tomato\",\"carrots\",\"onion\"])\n",
    "print(fruits)\n",
    "               "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['mango', 'banana']\n",
      "['mango']\n"
     ]
    }
   ],
   "source": [
    "#how can i remove an item from a list? you simple use the pop() function for example:\n",
    "fruits.pop()\n",
    "print(fruits)\n",
    "fruits.pop()\n",
    "print(fruits)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mango\n"
     ]
    }
   ],
   "source": [
    "#how can i retrive some specific data types in a list? you can retrieve it by specifying the index number for example:\n",
    "print(fruits[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-79-f1dfcd7fc079>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#what will happen if i exit the index range or the list range? and indexError message will pop up index out of range\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfruits\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "#what will happen if i exit the index range or the list range? and indexError message will pop up index out of range\n",
    "print(fruits[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Maize', 'beans', 'millet', 'wheat']\n",
      "['wheat', 'beans', 'millet', 'Maize']\n"
     ]
    }
   ],
   "source": [
    "#can i swap data in a list? yes it is possible if you introduce a third variable. for example:\n",
    "cerials = [\"Maize\", \"beans\", \"millet\",\"wheat\"]\n",
    "print(cerials)\n",
    "# swaping the first list value with the last\n",
    "temp = cerials[0]\n",
    "cerials[0]=cerials[3]\n",
    "cerials[3]=temp\n",
    "print(cerials)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "githeri\n",
      "rice_beans\n",
      "beef_stew\n",
      "basua\n"
     ]
    }
   ],
   "source": [
    "# for loop\n",
    "# for loop facilitate the iteration of  values for example in a list.\n",
    "#for example:\n",
    "lunch = [\"githeri\", \"rice_beans\", \"beef_stew\", \"basua\"]\n",
    "#without for statement, if some one wants to use each of the elements in the list, it will be so complex for example:\n",
    "print(lunch[0])\n",
    "print(lunch[1])\n",
    "print(lunch[2])\n",
    "print(lunch[3])\n",
    "\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "githeri\n",
      "rice_beans\n",
      "beef_stew\n",
      "basua\n"
     ]
    }
   ],
   "source": [
    "#with the for statement one can easily iterate over the list with ease, for example:\n",
    "for lun in lunch:\n",
    "    print(lun)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4950\n"
     ]
    }
   ],
   "source": [
    "# how can i add components in a list? you can add by introducing a defined variable for holding the result, for example:\n",
    "total = 0\n",
    "for numbers in range(0, 100):\n",
    "    total += numbers\n",
    "print(total)\n",
    "    \n",
    "\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
