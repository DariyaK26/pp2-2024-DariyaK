'''f=open('lab6/file.txt', 'r')
print(f.read(5))
f.seek(0)
print(f.read(8))
f.close()'''

#1
#import os
#print(os.getcwd())
#way=input()
##'/Users/77778/Desktop/pp2-2024-DariyaK/lab6'
#print(os.chdir(way))
#print(os.listdir())
#dirs=[i for i in os.listdir(way) if os.path.isdir(os.path.join(way, i))]
#files=[i for i in os.listdir(way) if os.path.isfile(os.path.join(way, i))]
#print(files)
#print(dirs)

#2
#import os
#
#file_path =input()
#print(os.chdir(file_path))
#print('Exist', os.access(file_path, os.F_OK))
#print('Read', os.access(file_path, os.R_OK))
#print('Write', os.access(file_path, os.W_OK))
#print('Execute', os.access(file_path, os.X_OK))

#3
#import os
#path=input()
#print(os.path.exists(path))

#4
#with open('lab6/file.txt', 'r') as f:
#    for i, l in enumerate(f):
#        pass
#print(i+1)

#5
#list=['sdf0', 'asdas', 'sdf']
#with open('lab6/file.txt', 'w') as f:
#    
#    for i in list:
#        f.write(str(i)+'\n')

#6
#import os
#import string
#for i in string.ascii_uppercase:
#    with open('lab6/'+i+'.txt', 'x') as f:
#        pass


#7
#from shutil import copyfile
#way1=input()
#way2=input()
#copyfile(way1, way2)

#8
import os
way=input()
if os.path.exists(way):
    os.remove(way)
else:
    print('no')
