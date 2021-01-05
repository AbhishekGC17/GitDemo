#file = open('simple.txt')
#t = file.readline()
#while t!="":
#    print(t)
#   t=file.readline()
#for t in file.readlines():
#    print(t)
#print(file.read())
#file.close()
with open('simple.txt','r') as file:
    l=file.readlines()
    reversed(l)
    print(l)
with open('simple.txt','w') as win:
    for lin in reversed(l):
        win.write(lin)