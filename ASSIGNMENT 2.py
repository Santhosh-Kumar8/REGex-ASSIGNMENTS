# 1)
##
##a = int(input("ENTER NO: "))
##b = int(input("ENTER NO: "))
##i = 1
##while (i <= a and i <=b) :
##    if (a%i == 0 and b%i == 0):
##        gcd = i
##    i += 1
##print(gcd)
## 


# 2)
##
##file = open("textfile.txt","w+")
##file.seek(15)
##file.truncate()
##file.write("HELLO")
##file.close()
##


# 3)

##def passval(password):
##    caps = False
##    small = False
##    spl = False
##    if len(password) > 5 and len(password) < 16:
##        
##        for i in password:
##            if i.isupper():
##                caps = True
##            if i.islower():
##                small =  True
##            if i in "!@#$%^":
##                spl = True
##            if caps and small and spl:
##                print("PASSWORD ACCEPTED")
##                break
##        if not caps:
##            print("SHOULD CONTAIN ATLEAST ONE CAP LETTER")
##        if not small:
##            print("SHOULD CONTAIN ATLEAST ONE SMALL LETTER")
##        if not spl:
##            print("SHOULD CONTAIN ATLEAST ONE OF !@#$%^ CHARACTERS ")
##            
##    else:
##        print("PASSWORD LENGTH SHOULD BE 6 - 15 CHARACTERS")
##
##
##password = input("ENTER PASSWORD: ")
##
##passval(password)


# 4)

##import string
##import os
##dirname = os.path.dirname(__file__)
##os.mkdir(dirname+ "\\TASK4")
##alphabet_string = string.ascii_uppercase
##for i in list(alphabet_string):
##    file = open(dirname+ "\\TASK4\\"+ i +".txt","w")
##    file.close()
##

# 5)

##import os
##
##
##if not os.path.exists(os.path.join(os.getcwd(), 'TASK 5')):
##    os.mkdir(os.path.join(os.getcwd(), 'TASK 5'))
##
##file1 = open(os.path.join(os.getcwd(), 'TASK 5','file1.txt'),"r")
##file2 = open(os.path.join(os.getcwd(), 'TASK 5','file2.txt'),"r")
##list1 = [line.strip() for line in file1]
##list2 = [line.strip() for line in file2]
##
### above code combine each line from the first file with the corresponding line in the second file
##
### save it into the Third file.
##
##file3 = open(os.path.join(os.getcwd(), 'TASK 5','file3.txt'),"w")
##for i in range(len(list1)):
##    file3.write(list1[i]+" - "+ list2[i]+"\n") 
##file3.close() 
##

# 6)

##import pywhatkit
##pywhatkit.sendwhatmsg('enter number', 'enter message', hrs, mins)
##





