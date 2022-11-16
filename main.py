from tabulate import tabulate
import random

maxint = int(1e10)
class v:
    arr = [30, 35, 15, 5, 10, 20, 25]
    size = 0
    head = []

# các hàm liên quan đến thuật toán
def topDown(p,n):
    minMulti = [[-1 for i in range(n)] for j in range(n)]
    k_pos = [[-1 for i in range(n)] for j in range(n)]
    memoization(p, 0, n-1,minMulti,k_pos)
    return minMulti,k_pos

def memoization(p,i,j,dp,k_pos):
    if (i == j):
        return 0

    if (dp[i][j] != -1):
        return dp[i][j]
    print(tabulate(dp, headers=v.head,showindex=v.head[1:]))
    print()
    print()

    dp[i][j] = maxint
    minAns= maxint
    for k in range(i, j):
        q = min(dp[i][j],memoization(p, i, k,dp,k_pos) + memoization(p, k + 1, j,dp,k_pos) + p[i] * p[k+1] * p[j+1])
        if(minAns>q):
            minAns=q
            k_pos[i][j]=k
    if(j==v.size-1):
        print(tabulate(dp, headers=v.head,showindex=v.head[1:]))
        print()
        print()
    dp[i][j] = minAns
    return dp[i][j]

def bottomUp(p, n):
    minMulti = [[-1 for x in range(n)] for x in range(n)]
    k_pos = [[-1 for x in range(v.size)] for x in range(v.size)]
    for i in range(0, n):
        minMulti[i][i] = 0
    print("Visualization:")
    print(tabulate(minMulti, headers=v.head, showindex=v.head[1:]))
    for L in range(2, n+1):
        for i in range(0, n - L +1):
            j = i + L -1
            minMulti[i][j] = maxint
            for k in range(i, j):
                q = minMulti[i][k] + minMulti[k + 1][j] + p[i] * p[k+1] * p[j+1]
                if q < minMulti[i][j]:
                    minMulti[i][j] = q
                    k_pos[i][j] = k
            print("Length=",L,":")
            print(tabulate(minMulti, headers=v.head, showindex=v.head[1:]))
        print()
        print("==================================================")
    return minMulti,k_pos

def CalUsingBottomUp():
    minMulti, k_pos = bottomUp(v.arr, v.size)
    print("Position of k for optimal value for each multiplication: ")
    print(tabulate(k_pos, headers=v.head,showindex=v.head[1:]))
    print("==================================================")
    print("Calculate optimal with input: ", end="")
    print(v.arr)
    print("Optimal parenthesization: " + parenthesis(k_pos, 0, len(v.arr) - 2, ""))
    print("Minimum number of multiplications: " + str(minMulti[0][v.size - 1]))
    print("Number of natural order multiplications: " + str(MatrixNormalMulti(v.arr)))

def CalUsingTopDown():
    minMulti, k_pos = topDown(v.arr, v.size)
    print(tabulate(minMulti, headers=v.head,showindex=v.head[1:]))
    print()
    print("Position of k for optimal value for each multiplication: ")
    print(tabulate(k_pos, headers=v.head,showindex=v.head[1:]))
    print("==================================================")
    print("Calculate optimal with input: ", end="")
    print(v.arr)
    print("Optimal parenthesization: " + parenthesis(k_pos, 0, len(v.arr) - 2, ""))
    print("Minimum number of multiplications: " + str(minMulti[0][v.size - 1]))
    print("Number of natural order multiplications: " + str(MatrixNormalMulti(v.arr)))

def MatrixNormalMulti(p):
    cal=0
    for i in range(0,len(p)-2):
        cal+=p[0]*p[i+1]*p[i+2]
    return cal

def parenthesis(s, i, j,ans):
    if i == j:
        ans +="A[{num}]".format(num = i+1)
    else:
        ans +="("
        ans = parenthesis(s, i, s[i][j],ans)
        ans = parenthesis(s, s[i][j]+1, j,ans)
        ans +=")"
    return ans


# Các chức năng của chương trình
def generateSizeMatrix():
    p=[]
    num= int( input("Enter number of matrix to calculate: ") )
    for i in range(num):
        tmp = int( input("Enter row of matrix {} (arr[{}]):".format(i+1,i)) )
        p.append(tmp)
    tmp = int(input("Enter column of matrix {} (arr[{}]):".format(num, num)))
    p.append(tmp)
    print("The input array: ",p)
    return p

def generateRandomMatrix():
    p = []
    print("Generate number of matrix to calculate: ",end=" ")
    num = random.randint(5,15)
    print(num)
    for i in range(num+1):
        p.append(random.randint(1,15)*5)
    print("The random generated array: ", p)
    return p

def generateMatrix():
    print("1.Generate random matrix")
    print("2.Generate custom matrix")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            v.arr=generateRandomMatrix()
        case "2":
            v.arr=generateSizeMatrix()
    MainMenu()

def preProcess():
    v.head.clear()
    v.head.append("")
    print("Calculate optimal with input: ",end="")
    print(v.arr)
    v.size = len(v.arr) - 1
    for i in range(v.size):
        v.head.append("A"+str(i+1))

def calMulti():
    print("1.Calculate using top-down approach")
    print("2.Calculate using bottom-up approach")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            CalUsingTopDown()
        case "2":
            CalUsingBottomUp()
    MainMenu()

def MainMenu():
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    print("\t\tOPTIMAL MATRIX MULTIPLICATION CALCULATOR")
    print("\t\t\t   Tạ Đình Sơn Tùng - HE160762")
    print("\t\t\t\t\t\tMain Menu")
    print()
    print("1.Generate matrix")
    print("2.Calculate optimal matrix multiplication")
    print("3.Exit program")
    choice=""
    while(choice!="3"):
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                generateMatrix()
            case "2":
                preProcess()
                calMulti()
    print("Thank you for using my program!")

MainMenu()


