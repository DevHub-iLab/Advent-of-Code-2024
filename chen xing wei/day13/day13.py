file = open("day13\day13.txt", 'r')

ans = 0
for i in file:
    line = i.strip().split(" ")
    if(line[0] == "Button"):
        if(line[1] == "A:"):
            x1 = int(line[2][2: -1])
            y1 = int(line[3][2:])
        else: #button B
            x2 = int(line[2][2: -1])
            y2 = int(line[3][2:])

    elif(line[0] == "Prize:"):
        X = int(line[1][2: -1]) + 10000000000000 #uncomment 10T for part 2
        Y = int(line[2][2:]) + 10000000000000
        
        #Using Cramer's rule to solve the system of eqns
        #   a*x1 + b*x2 = X
        #   a*y1 + b*y2 = Y
        det = x1*y2 - x2*y1 
        a = (X*y2 - Y*x2) / det
        b = (Y*x1 - X*y1) / det
        if(a==int(a) and b==int(b)):
            ans += int(3*a + b)
print(ans)