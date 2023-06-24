# prefix convertor
stack1 = input("enter a expression:")
stack=stack1[-1::-1]
operator=[]
output=[]
dectionary={')':0,'+':1,'-':1,'/':2,'*':2,'^':3}
for i in stack:
    if i==')':
        operator.append(i)
    elif i=='(':
        while operator[-1]!=')':
            a= operator.pop()
            output.append(a)
        operator.pop()
    elif i=='+' or i=='-' or i=='*' or i=='/' or i=='^':
        if len(operator)>0:
            while dectionary[operator[-1]]>dectionary[i]:
                b=operator.pop()
                output.append(b)
                if len(operator)==0:
                    break
        operator.append(i)
    else:                                         
        output.append(i)
while len(operator)!=0:
    c = operator.pop()
    output.append(c)
output.reverse()
for i in output:
    print(i,end='')
    