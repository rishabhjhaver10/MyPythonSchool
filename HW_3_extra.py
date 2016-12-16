class Textfile():

    def __init__(self, filename):
        self.file = open(filename)
        self.content = self.file.read()

    def nchars(self):
        return len(self.content)

    def nwords(self):
        words = self.content.split()
        return len(words)

    def nlines(self):
        linelist = self.content.split('\n')
        return len(linelist)
        
    def read(self):
        return self.content
        
    def readlines(self):
        linelist = self.content.split('\n')
        return linelist
        
    def grep(self, string = ' '):
        linelist = self.content.split('\n')
        linelist1 = []
        for item in linelist:
            if string in item:
                x = linelist.index(item) 
                print(str(x) + ' : ' + item)
                linelist1.append(item)
        print(linelist1)
        
    def words(self):
        wordlist = self.content.split()
        newlist= []
        for i in wordlist:
            if i not in newlist:
                newlist.append(i)
        print(len(newlist))
        return newlist
        
    
        
    