file = open ('test.py','w')
#Returns: a file object assigned to the variable file its create a file if a file not exist so its make problem 


try :
    file.write('chai aur code')
finally :
    file.close()
#try...finally is used to ensure that certain code always runs, even if an error occurs in the try block.

with open ('youtube.txt','w') as file :
    file.write('chai aur python')
#with open() is a context manager that automatically opens and closes a file.
#It ensures the file is properly closed, even if an error happens inside the block.its best syntax amoung of these 
