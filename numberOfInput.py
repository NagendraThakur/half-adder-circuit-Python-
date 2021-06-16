name = (input("Enter your name: "))
print("********** Welcome ", name," to the binary addition program **********")
## numberofInput() function is created
def numberOfInput():
    running = False
    first = False
    second = False
    complete = False
##    A set is created i.e. bset
    bset = {'-','2','3','4','5','6','7','8','9'}
    while(not running):
##      user is asked to input b or B for binary number system and d or D for decimal number system
        numType = input("Enter b or B if you want to input binary number \nElse d or D if you want to input decimal number:  ")
##      if the user chooses to input binary number
        if numType in ["b","B"]:
            while(not complete):
##              try and exception are used to handle exception
                try:
                    while(not first):
##                      use is asked to input first binary number
                        num1 = (input("Enter the first binary number:  "))
##                      if statement is used to check if first number is greater than 8-digit or not.
                        if(len(num1)>8):
                            print("The entered binary number cannot be greater than 8-digits.")
##                      elif statement is used to check if the use has input valid binary number
                        elif(set(num1).intersection(bset)):
                            print("Please input a vaild binary number. Example: 10101")
                        else:
                            int(num1)
                            first=True
                    while(not second):
##                      user is asked to input second binary number
                        num2 = (input("Enter the second binary number:  "))
##                      if statement is used to check if second number is greater than 8-digit or not.
                        if(len(num2)>8):
                            print("The entered binary number cannot be greater than 8-digits.")
##                      elif statement is used to check if the use has input valid binary number
                        elif(set(num2).intersection(bset)):
                            print("Please input a vaild binary number. Example: 10101")
                        else:
                            int(num2)
                            complete=True
                            second=True
                            return ("b",num1,num2)
##                          b, num1 and num2 are returned
                except:
                    print("Please donot enter alphabets or special characters!")
##      if the user chooses to input decimal number                    
        elif numType in ["d","D"]:
            while (not complete):
##              try and exception are used to handle exception
                try: 
                    while(not first):
##                      the user is asked to input first binary number
                        num1 = input("Enter the first decimal number:  ")
                        i = int(num1)
##                      if statement is used to checked if the first decimal number if  less than 0 and greater then 255
                        if(i<0 or i>255):
                            print("Enter the number which is greater than 0 and less than 255")
                        else:
                            first=True
                    while(not second):
##                      the user is asked to input second decimal number
                        num2 = input("Enter the second decimal number:  ")
                        j = int(num2)
##                      if statement is used to checked if the second decimal number if  less than 0 and greater then 255
                        if(j<0 or j>255):
                            print("Enter the number which is greater than 0 and less than 255")
##                          if statement is used to check if the sum of the binary is less than 0 and more than 255
                        elif((i+j)<0 or (i+j)>255):
                            print("Enter the two numbers whose sum are minium 0 and maxium 255")
                            running = False
                        else:
                            running = True
                            second = True
                            complete = True
                            return ("d",num1,num2)
##                          b, num1 and num2 are returned
                except:
                    print("Please donot enter alphabets or special characters!")
        else:
            print("invalid alphabate has been entered.")
