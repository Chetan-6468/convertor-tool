# postfix convertor
stack = input("enter a expresion")
operator = []
output =[]
presidence = {'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
for i in stack:
    if i=='(':
        operator.append(i)
    elif i==')':
        while operator[-1]!='(':
            a = operator.pop()
            output.append(a)
        operator.pop()
    elif i=='+' or i=='-' or i=='*' or i=='/' or i=='^':
        if len(operator)>0:
            while presidence[operator[-1]]>=presidence[i]:
                b=operator.pop()
                output.append(b)
                if len(operator)==0:
                    break

        operator.append(i)
    else:
        output.append(i)
while len(operator)!=0:
    c=operator.pop()
    output.append(c)
for i in output:
    print(i,end='')