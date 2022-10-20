
upper = int(input("Enter the upper number"))
f = open("myfirstcalculator.py", "a")

def createline(f ,num1, num2, operator):
    if operator == "+":
        string = "if num1 =="+ str(num1)+ " and num2 =="+ str(num2)+ " and operator == '+':\n\tprint('The answer is ' +  str("+  str(num1 + num2) + "))\n"
    elif operator == "-":
        string = "if num1 =="+ str(num1)+ " and num2 =="+ str(num2)+ " and operator == '-':\n\tprint('The answer is ' +  str("+  str(num1 - num2) + "))\n"
    elif operator == "*":
        string = "if num1 =="+  str(num1)+ " and num2 =="+ str(num2)+ " and operator == '*':\n\tprint('The answer is ' + str("+  str(num1 * num2) + "))\n"
    f.write(string)
    

def openingline(f, upper):
    string ="print('Enter two numbers up to " + str(upper) + "'\n)" + """
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
operator = input("Enter one of the operators +, -, *")
"""
    f.write(string)

def createcalc(upper, f):
    openingline(f,upper)
    operands = ["+", "-", "*"]
    for operator in operands:
        print("Currently on on operator " + operator)
        for firstnum in range(upper):
            if firstnum % (upper/50) == 0:
                print("On: " + operator + str(firstnum))
            for secondnum in range(upper):
                createline(f,firstnum, secondnum, operator)

    f.close()

createcalc(upper, f)


