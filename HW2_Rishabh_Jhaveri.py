def make_word_count(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    word_list = content.split()
    counters = dict()
    for item in word_list:
        item1 = item.lower()
        if item1 in counters:
            counters[item1] += 1
        else:
            counters[item1] = 1
    return counters
    
x = make_word_count('test.txt')
print(x)



def make_length_wordcount(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()
    word_list = content.split()
    counters = dict()
    len_item = 0
    for item in word_list:
        len_item = len(item)
        if len_item in counters:        
            counters[len_item] += 1
        else:
            counters[len_item] = 1
    return counters
    
x = make_length_wordcount('test.txt')
print(x)


def analyze_text(file_name):
    infile = open(file_name, 'r')
    content = infile.read()
    word_list = content.split()
    outfile = open(file_name + '_analyzed_RISHABH_JHAVERI.txt', 'w')
    
    a = make_word_count(file_name)
    b = make_length_wordcount(file_name)
    
    for i, j in b.items():
        outfile.write('Words of length ' + str(i) + ' : ' + str(j) + '\n')
        
    for m, n in a.items():
        outfile.write(str(m) + ' : ' + str(n) + '\n')
        
analyze_text('test.txt')
analyze_text('nasdaq.txt')
analyze_text('raven.txt')
analyze_text('frankenstein.txt')