from numberOfInput import numberOfInput

## conversion() function is created
def conversion():
##  numberofInput() function is called
    system, num1, num2 =numberOfInput()
##  empty lists are created
    list1 = []
    list2 = []
    extra = []
    var1=0
    var2=0
##  the length of the returned value i.e. num1 and num2 are substracted by 1 and stored in k and l respectively
    i=len(str(num1)) - 1
    j=len(str(num2)) - 1
    k=i
    l=j
##  if statement is used to check if the user has choosen binary number or not
    if (system in ["b"]):
##      for each loop is used to extract each variable from num1 and store it at the 0 postion of list1
        for x in num1:
            list1.insert(0,int(num1[i]))
            i=i-1
##      for each loop is used to extract each variable from num1 and store it at the 0 postion of list1
        for x in num2:
            list2.insert(0,int(num2[j]))
            j=j-1
        for x in list1:
            var1 = var1 + (x * (2**k))
            k = k - 1
        
        for x in list2:
            var2 = var2 + (x * (2**l))
            l = l - 1
##      if statement is used to check if list2 is creater than list1
        if(len(list2)>len(list1)):
            list1, list2 = list2, list1
        zero = len(list1) - len(list2)
##      for each loop is used to insert 0 at 0 position of extract list
        for x in range (zero):
            extra.insert(0,0)
        extra.extend(list2)
        list2 = extra
##      var1, var2, list1, list2 are returned
        return (var1, var2, list1, list2)
        
    if (system in ["d"]):
        num1 = int(num1)
        num2 = int(num2)
        var1 = num1
        var2 = num2
##      while loop is used to convert num1 into binary number
        while (num1 > 0):
            variable = int(num1 / 2)
            result = num1 % 2
            list1.insert(0,result)
            num1 = variable
##      while loop is used to convert num1 into binary number
        while (num2 > 0):
            variable = int(num2 / 2)
            result = num2 % 2
            list2.insert(0,result)
            num2 = variable
##      if statement is used to check if list2 is creater than list1
        if(len(list2)>len(list1)):
            list1, list2 = list2, list1
        zero = len(list1) - len(list2)
##      for each loop is used to insert 0 at 0 position of extract list
        for x in range (zero):
            extra.insert(0,0)
        extra.extend(list2)
        list2 = extra
##      var1, var2, list1, list2 are returned
        return (var1, var2, list1, list2)

