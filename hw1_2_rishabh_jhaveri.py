#1.	Create a file with name “hw1_2.py” and download “last.txt” file into the same directory, where “hw1_2.py” is located.





#2.	Open “last.txt” file with “read-only” file mode.

infile = open('last.txt', 'r')





#3.	Find the number of characters in the file and assign it to “ans3” variable.

def num_char(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    return len(content)
    
ans3 = num_char('last.txt')
print('answer3={}'.format(ans3))





#4.	Find the number of words in the file and assign it to “ans4” variable.

def num_words(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    word_list = content.split()
    return len(word_list)

ans4 = num_words('last.txt')
print('answer4={}'.format(ans4))





#5.	Find the number of lines in the file and assign it to “ans5” variable.

def num_lines(filename):
    infile = open(filename, 'r') 
    lineList = infile.readlines() 
    infile.close()
    return len(lineList)

ans5 = num_lines('last.txt')
print('answer5={}'.format(ans5))





#6.	Count the last names starting with “L” and assign it to “ans6” variable.

new_list = [ ]

def num_words_begin_L(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    
    word_list = content.split()
    for item in word_list:
        if item[0] == '0':
            word_list.remove(item)
            
    for item in word_list:
        if item[0] == 'L':
            new_list.append(item) 
            
    return len(new_list)

ans6 = num_words_begin_L('last.txt')
print('answer6={}'.format(ans6))





#7.	Count the last names ending with “E” and assign it to “ans7” variable.

new_list = [ ]

def num_words_end_E(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    
    word_list = content.split()
    for item in word_list:
        if item[0] == '0':
            word_list.remove(item)
            
    for item in word_list:
        if item[-1] == 'E':
            new_list.append(item) 
            
    return len(new_list)

ans7 = num_words_end_E('last.txt')
print('answer7={}'.format(ans7))





#8.	Count the last names with length 3 and assign it to “ans8” variable.

new_list = [ ]

def num_words_len_3(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    
    word_list = content.split()
    for item in word_list:
        if item[0] == '0':
            word_list.remove(item)
            
    for item in word_list:
        if len(item) == 3:
            new_list.append(item)
            
    return len(new_list)

ans8 = num_words_len_3('last.txt')
print('answer8={}'.format(ans8))





#9.	Count the numbers larger than 0.1 and assign it to “ans9” variable.

new_list = [ ]

def num_greater_than(file_name):
    with open(file_name, 'r') as infile:
        words = infile.read().split()
        
    for item in words:
        if item[0] != 0:
            words.remove(item)
            
    for item in words:
        if float(item) > 0.1:
            new_list.append(item)
            
    return len(new_list)

ans9 = num_greater_than('last.txt')
print('answer9={}'.format(ans9))





#10.	Count the numbers smaller than 0.02 and assign it “ans10” variable.


new_list = [ ]

def num_less_than(file_name):
    with open(file_name, 'r') as infile:
        words = infile.read().split()
        
    for item in words:
        if item[0] != 0:
            words.remove(item)
            
    for item in words:
        if float(item) < 0.02:
            new_list.append(item)
            
    return len(new_list)

ans10 = num_less_than('last.txt')
print('answer10={}'.format(ans10))





#11.	Get the number associated to your last name and assign it to “ans11” variable. If your last name doesn’t appear, “ans11” should be 0.


def get_num(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    word_list = content.split()
    
     
    s = 'JHAVERI'
    if s in word_list:
        x = word_list.index(s)
        return word_list[x + 1]
    elif s not in word_list:
        x = 0
        return x
    

ans11 = get_num('last.txt')
print('answer11={}'.format(ans11))





#12.	Find the last name that comes last in the dictionary order and assign it to “ans12” variable.

def last_word(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    
    word_list = content.split()
    for item in word_list:
        if item[0] == '0':
            word_list.remove(item)
        
    word_list.sort()
    return (word_list[-1])

ans12 = last_word('last.txt')    
print('answer12={}'.format(ans12))






#13.	Find the last name that comes first in the dictionary order and assign it to “ans13” variable.

def first_word(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    
    word_list = content.split()
    for item in word_list:
        if item[0] == '0':
            word_list.remove(item)
        
    word_list.sort()
    return (word_list[0])

ans13 = first_word('last.txt')    
print('answer13={}'.format(ans13))






#14.	Find the longest last name and assign it to “ans14” variable.

def word_max_len(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    
    word_list = content.split()
    for item in word_list:
        if item[0] == '0':
            word_list.remove(item)
            
    return max(word_list, key=len)
        
    
ans14 = word_max_len('last.txt')
print('answer14={}'.format(ans14))





#15.	Find the shortest last name and assign it to “ans15” variable.

def word_min_len(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    
    word_list = content.split()
    for item in word_list:
        if item[0] == '0':
            word_list.remove(item)
            
    return min(word_list, key=len)
        
    
ans15 = word_min_len('last.txt')
print('answer15={}'.format(ans15))





#16.	Open a new file “hw1_2_answers_FIRST_LAST.txt” using “write” mode, where FIRST and LAST should be your first and last names. For example, hw1_2_answers_GENE_LEE.txt.

outfile = open('hw1_2_answers_Rishabh_Jhaveri.txt', 'w')





#17.	Write your first name, last name, and email address in the first line of “hw1_2_answers_FIRST_LAST.txt” file. 

outfile.write('Rishabh Jhaveri rishabhsandeep.jhaveri@mavs.uta.edu \n')





#18.	Write all your answers into the “hw1_2_answers_FIRST_LAST.txt” file. Each answer will take a line with “answerXX=YY” format. 

outfile.write('answer 3 = 14962 \nanswer 4 = 2002 \nanswer 5 = 1001  \nanswer 6 = 42  \nanswer 7 = 81  \nanswer 8 = 16  \nanswer 9 = 64  \nanswer 10 = 438 \nanswer 11 = 0  \nanswer 12 = ZUNIGA  \nanswer 13 = ABBOTT  \nanswer 14 = FITZ-PATRICK   \nanswer 15 = O \n')





#19.	Write “Homework 1 Part 2 is done!!!” in the last line of “hw1_2_answers_FIRST_LAST.txt” file.

outfile.write('Homework 1 part 2 is done!!!')





#20.	Close “ hw1_2_answer_FIRST_LAST.txt” file. 

outfile.close()