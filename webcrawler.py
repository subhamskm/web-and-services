import os,urllib.request,urllib.error,re
class decode():
    #class to take the response from the url
    def __init__(self,path=" ",fhand=None):
        self.path=path
        self.fhand=fhand
    def decode(self):   #saves the response to the specified file and path
        os.chdir(self.path)
        os.mkdir("Decode")
        os.chdir(self.path+"//Decode")
        self.file = open("decode.txt", "w")
        for i in self.fhand:
            line=i.decode()
            self.file.write(line)
        self.file.close()
class Webcrawler(decode):
    #class to different function on web crawling , superclass=  decode()
    #def check(self):
        #if self.fhand==None:
            #print("Enter valid Url")
            #exit(1)
    def Link_crawl(self,file_name=" "):    #link crawler
        self.file=open(self.path+"//Decode//decode.txt","r")
        for line in self.file:
            found_string=re.findall(r'href="[\w\W\S\s.]{1,80}">',line)
            self.file_name=open(self.path.join(self.path+"\\"+file_name),"a")
            for j in found_string:
                self.file.write(j[6:]+"\b\n")
        self.file_name.close()
        self.file.close()
    def Name_crawl(self,file_name=" "): #Name crawler
        self.file = open(path + "//Decode//decode.txt", "r")
        for line in self.file:
            self.found_string=re.findall(r'[A-Z]{3,15}[\s]')
            self.file_name = open(self.path.join(self.path + "\\" + file_name), "a")
            for j in self.found_string:
                self.file.write(j+ "\n")
        self.file_name.close()
        self.file.close()
    def Contact_number(self,file_name=" "):     #contact crawler
        self.file = open(path + "//Decode//decode.txt", "r")
        for line in  self.file:
            self.found_string=re.findall(r'[+(]{1}[\d]{1}[)]{1}[\d\s]{1,10}[\d]',line)
            self.file_name = open(self.path.join(self.path + "\\" + file_name), "a")
            for j in self.found_string:
                self.file.write(j + "\n")
        self.file_name.close()
        self.file.close()
while True:
    #url="https://www.regular-expressions.info/python.html"#str(input())
    fhand = urllib.request.urlopen("https://www.regular-expressions.info/python.html")
    path=str(input("enter the path"))
    obj_decode=decode(path,fhand)        #object of superclass = decode()
    obj_decode.decode()
    obj_crawl=Webcrawler()          #object of Webcrawler class
    #obj_crawl.check()
    num=input("0: Link_crawl 1:  Name_crawl  2: Contact_number e : exit\n")
    if num==0:
        obj_crawl.Link_crawl()
    elif num==1:
        obj_crawl.Name_crawl()
    elif num==2:
        obj_crawl.Contact_number()
    else:
        exit(1)