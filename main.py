from adder import adder

##  main() function is created
def main():
    run = True
    while run:
##      adder function is called from adder module
        num1, num2, list1, list2, added = adder()

##      if statement is used to check the length if the added list    
        if (len(added)>8):
           print('please enter the two binary numbers whose sum are minium 00000000 and maxium 11111111')
           again = False
           added = adder()
        else:
##          the added value is displayed with suitable message
            print('-----------------------------------------------------------------------------------------')
            print('IN BINARY: \nThe sum of the fist number :',list1,'\nAnd the second number :',list2,'\nis ',added)
            print('-----------------------------------------------------------------------------------------')
            print('IN DECIMAL:\n The sum of the fist number :',num1,'\nAnd the second number :',num2,'\nis ',num1 + num2)
            print('-----------------------------------------------------------------------------------------')
            again = False
            while (not again):
##              user is asked if you want to continue the program
                var = input('Do you wish to continue (Y for YES /N for NO)?')
                if(var in ['y' or 'Y']):
                    again = True
                elif(var in ['n' or 'N']):
##                  the  program is ended with a thank you and the developer name
                    print('**********Thank You**********\n             Developed By Nagendra Thakur Sharma')
                    again = True
                    run = False
                else:
                    print('invalid choice.')
            
main()
