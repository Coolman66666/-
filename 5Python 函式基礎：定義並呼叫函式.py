#定義函式
#函數內部的程式碼，若是沒有函數呼叫，就不會執行
def multiply():
    print(3*6)

def multiply(n1,n2):
     print(n1*n2)

def multiply(n1,n2):
     print(n1*n2)
     return

def multiply(n1,n2):
     print(n1*n2)
     return 10

def multiply(n1,n2):
    print(n1*n2)
    return n1*n2

def multiply(n1,n2):
     return n1*n2

#呼叫函示
multiply()

multiply(3,3)
multiply(3,12)

value=multiply(3,4)
print(value)

value=multiply(3,4)
print(value)

value=multiply(3,4)
print(value)

value=multiply(3,4)+multiply(10,5) #(3*4)+(10*5)
print(value)

#函數的包裝
#函式可用來做成程式的包裝:同樣的邏輯可以重複利用
def calculate(n1,n2):
     sum=0
     for x in range(n1,n2+1):
         sum+=x
     else:
         print(sum)

calculate(10,12)
calculate(12,12)


