import os

# File path to the file you wanna get deleted. 
file_path = '/Users/niclasjuulschaeffer/Downloads/Introduction.to.Algorithms.4th.Leiserson.Stein.Rivest.Cormen.MIT.Press.9780262046305.EBooksWorld.ir.PDF'

#Checks whether the file exists or not and delete it if it does. 
if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been removed")
else: 
    print('This file does Not exist')