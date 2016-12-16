#==========================================================================================
# INSY 5378 Homework #1 
# 20 problems, 5 points each, total 100 points
#==========================================================================================
#
# Please input your first name, last name, and MAVS email address
first_name = "Rishabh"
last_name = "Jhaveri"
email = "rishabhsandeep.jhaveri@mavs.uta.edu"
#

#==========================================================================================
#
# For 1-10:
# Write (and evaluate) Python expressions that compute:
#
#
# 0. The sum of 10 and 20
ans0 = 30

#1. The product of 1111111 with itself.
ans1 = int(1111111 * 1111111) 

#
#2. How often does 81 go into 1000?
ans2 = int(1000 // 81) 

#
#3. What is the remainder when 1000 is divided by 81?
ans3 = int(1000 % 81) 

#
#4. You scored 90/100, 95/100 and 85/100: what is your average percentage score (in 0-100 scale) on these three exams?
ans4 = float((85 + 90 + 95)/3)

#
#5. You scored 92/100, 45/50, 55/60 and 45/70: what is your best percentage score (in 0-100 scale) on these four exams?
ans5 = max([92/100, 45/50, 55/60, 45/70]) * 100

#
#6. You scored 90/100, 46/50, 55/60 and 66/70: what is the lowest percentage score (in 0-100 scale)?
ans6 = min([90/100, 46/50, 55/60, 66/70]) * 100

#
#7. The sum of the numbers 1 to 10.
ans7 = 0
for i in range(1,11):
    ans7 += i

#
#8. The product of the numbers 1 to 10. 
ans8 = 1
for i in range(1,11):
    ans8 *= i

#
#9. A Kb (kilobyte) is really 1024 bytes, where 1024 is 2 raised to the power 10: 
# how many kiobytes are there in a gigabyte (2 raised to the power 30)?
ans9 = (2**30)/(2**10)

#
#10. The number of different encodings using 32 bits.
ans10 = 2**32

#==========================================================================================






#==========================================================================================
#
# For 11-15:
# Write (and evaluate) Python expressions that answer these questions: 
#
#11. How many letters are there in 'Supercalifragilisticexpialidocious'?
ans11 = len('Supercalifragilisticexpialidocious')

#
#12. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? 
ans12 = 'ice' in 'Supercalifragilisticexpialidocious'

#
#13. Which of the following words is the longest: 
# Supercalifragilisticexpialidocious, Honorificabilitudinitatibus,  or Bababadalgharaghtakamminarronnkonn? 
a = ['Supercalifragilisticexpialidocious', 'Honorificabilitudinitatibus', 'Bababadalgharaghtakamminarronnkonn']
b = max(a, key=len)
ans13 = b

#
#14. Which composer comes first in the dictionary: 
l = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
x = sorted(l)
ans14 = x[0]


#
#15. Which one comes last in the dictionary: 
# 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'?
#ans15 = int()
l = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
x = sorted(l)
ans15 = x[-1]



#==========================================================================================






#==========================================================================================
#
# For 16-18: Write (and evaluate) Python expressions that answer the below questions 
# regarding a list lst of scores of 15 deliverables: 
lst = [94, 86, 85, 81, 86, 96, 91, 85, 86, 83, 89, 81, 86, 98, 84]
#
#16. What is the difference between the highest and lowest scores?
ans16 = int(max(lst) - min(lst))

#
#17. What is the average score?
ans17 = float(sum(lst)/len(lst))

#
#18. How many of the scores are 85?
ans18 = int(lst.count(85))
#==========================================================================================






#==========================================================================================
#
# 19. Assume you already have a list defined, called name, containing three strings: 
# a person's first, middle, and last name, in that order. Write an expression that produces 
# a string consisting of the person' s last name followed by a comma and space, then the first name and a space, 
# then the person' s middle initial followed by a period. 
# So, for example, if name is equal to ['John', 'Phillip', 'Sousa'], 
# your expression will produce the string 'Sousa, John P.'
name = ['Barack', 'Hussein', 'Obama']
ans19 = name[2] + ', ' + name[0] + ' ' + name[1] [0] + '.'

#==========================================================================================






#==========================================================================================
#
# 20. Assume you already have a list defined, called numbers, containing only numeric values. 
# Write code (you may need more than one expression, or to manipulate the list in some way) that 
# finds the sum of the second-largest and second-smallest values in the list. 
# For example, if the list is [4, 1, 0.5, 10, 6], your code would find the sum of 1 and 6.
numbers = [0, 101, 2**3, 10**2]
x = sorted(numbers)
ans20 = (x[1] + x[2])
#==========================================================================================



#==========================================================================================
#
# Please DO NOT change any lines below
#
print('{}, {}, {}'.format(last_name, first_name, email))
print('answer1={}'.format(ans1))
print('answer2={}'.format(ans2))
print('answer3={}'.format(ans3))
print('answer4={}'.format(ans4))
print('answer5={}'.format(ans5))
print('answer6={}'.format(ans6))
print('answer7={}'.format(ans7))
print('answer8={}'.format(ans8))
print('answer9={}'.format(ans9))
print('answer10={}'.format(ans10))
print('answer11={}'.format(ans11))
print('answer12={}'.format(ans12))
print('answer13={}'.format(ans13))
print('answer14={}'.format(ans14))
print('answer15={}'.format(ans15))
print('answer16={}'.format(ans16))
print('answer17={}'.format(ans17))
print('answer18={}'.format(ans18))
print('answer19={}'.format(ans19))
print('answer20={}'.format(ans20))
