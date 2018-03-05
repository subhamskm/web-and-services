import os,urllib.request,urllib.error,re
class decode():
    #class to take the response from the url
    def __init__(self,path=" ",fhand=None):
        self.path=path
        self.fhand=fhand
    def decode(self):   #saves the response to the specified file and path
        os.chdir(self.path)
        if not os.path.exists(path+"\\Decode"):
            os.mkdir("Decode")
        else:
            os.chdir(self.path+"\\Decode")
            file = open("decode.txt", "w")
        for i in self.fhand:
            line=i.decode()
            file.write(line)
        file.close()
class Webcrawler(decode):
    #class to different function on web crawling , superclass=  decode()
    def check(self):
        os.chdir(path + "\\Decode")
        if self.fhand==None:
            print("Enter valid Url")
            exit(1)
    def Link_crawl(self,file_name=" "):    #link crawler
        file=open(self.path+"\\Decode\\Decode.txt","r")
        file_name = open(file_name, "a")
        for line in file:
            found_string=re.findall(r'href="[\w\W\S\s.]{1,80}">',line)
            for j in found_string:
                file_name.write(j[6:]+"\b\n")
        file_name.close()
        file.close()
    def Name_crawl(self,file_name=" "): #Name crawler
        file = open(path + "\\Decode\\Decode.txt", "r")
        file_name = open(file_name, "a")
        for line in file:
            found_string=re.findall(r'[A-Z]{3,15}[\s]',line)
            for j in found_string:
                file_name.write(j+ "\n")
        file_name.close()
        file.close()
    def Contact_number(self,file_name=" "):     #contact crawler
        file = open(self.path + "\\Decode\\Decode.txt", "r")
        file_name = open(file_name, "a")
        for line in  file:
            found_string=re.findall(r'[+(]{1}[\d]{1}[)]{1}[\d\s]{1,10}[\d]',line)
            for j in found_string:
                file.write(j + "\n")
        file_name.close()
        file.close()
while True:
    #url="https://www.regular-expressions.info/python.html"#str(input())
    fhand = urllib.request.urlopen("https://www.regular-expressions.info/python.html")
    path=str(input("enter the path"))
    obj_decode=decode(path,fhand)        #object of superclass = decode()
    obj_decode.decode()
    obj_crawl=Webcrawler()          #object of Webcrawler class
    #obj_crawl.check()
    num=int(input("0: Link_crawl 1:  Name_crawl  2: Contact_number e : exit\n"))
    print(num)
    if num==0:
        obj_crawl.Link_crawl("links.txt")
    elif num==1:
        obj_crawl.Name_crawl("name.txt")
    elif num==2:
        obj_crawl.Contact_number("contact.txt")
    else:
        exit(1)