class Textfile():
    #constructor
    def __init__(self, filename):
        self.file = open(filename)
        self.content = self.file.read()
        
    #returns the number of character in the file
    def nchars(self):
        return len(self.content)
    
    #returns the number of words in the file
    def nwords(self):
        words = self.content.split()
        return len(words)
    
    #returns the number of line in the file
    def nlines(self):
        linelist = self.content.split('\n')
        return len(linelist)
    
    #returns the test of the file as a string
    def read(self):
        return self.content
    
    #returns the lines in a file as a list
    def readlines(self):
        linelist = self.content.split('\n')
        return linelist
    
    #takes a string as an input, finds it in the file and returns the index of the input string in the file
    def grep(self, string = ' '):
        linelist = self.content.split('\n')
        linelist1 = []
        for item in linelist:
            if string in item:
                x = linelist.index(item) 
                print(str(x) + ' : ' + item)
                linelist1.append(item)
        print(linelist1)
    
    #returns the unique words in the file
    def words(self):
        wordlist = self.content.split()
        newlist= []
        for i in wordlist:
            if i not in newlist:
                newlist.append(i)
        print(len(newlist))
        return newlist
        
    
        
    
