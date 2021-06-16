from gates import AND, OR, XOR
from conversion import conversion
## adder() function is created
def adder():
##  conversion() function is called from conversion module
    num1, num2, list1, list2 = conversion()
##  empty list adder is created
    added = []
    carry_in = 0
##  the length of list1 is substracted by 1 and stored in length
    length = len(list1) - 1
    for x in range(length, -1, -1):
        var1 = list1[x]
        var2 = list2[x]
##      XOR() Function is called from gates module
        xor = XOR(var1, var2)
##      XOR() Function is called from gates module
        sum1 = XOR(xor, carry_in)
        added.insert(0,sum1)
##      AND function is called from gates module
        add1 = AND(var1, var2)
##      AND function is called from gates module
        add2 = AND(xor, carry_in)
##      OR function is called from gates module
        carry_in = OR(add1, add2)

    added.insert(0,carry_in)
##  the values of num1, num2, list1, list2, added are returned
    return num1, num2, list1, list2, added
                
