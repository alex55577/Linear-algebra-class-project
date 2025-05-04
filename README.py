
import numpy as np
x = float(input("How much money are you starting with? "))
y = float(input("How much money do you want to end with? "))
w = float(input("How much money will you gamble per round? "))

p = float(input("What is the probability of winning? Enter as a demicimal (e.g. 0.5 for 50%) "))
q = 1-p

##matrix 
arr = [[0.0]*n]*n# n is the number of columns/rows
n=int(y/w) +1
if y%w:
    n+=1
print(n)

rows = n
cols = n
m = [[0.0] * cols for _ in range(rows)]

m[0][0] = 1.0
m[n-1][n-1] = 1.0

#if the column is equal to the row, then we add p to the element above and q to the element below
for i in range(1,n-1):
    for j in range(1,n-1):
        if i == j:
            m[i][j-1]=p
            m[i][j+1]=p
print(m)

##The above code works ok


## final code?
import numpy as np
x = float(input("How much money are you starting with? "))
y = float(input("How much money do you want to end with? "))
w = float(input("How much money will you gamble per round? "))

p = float(input("What is the probability of winning? Enter as a demicimal (e.g. 0.5 for 50%) "))

q = 1-p


## n is the number of columns/rows
n=int(y/w) +1
if y%w:
    n+=1
arr = [[0 for i in range(n)] for j in range(n)]
arr[0][0] = 1
arr[n-1][n-1] = 1
for i in range(1,n-1):
    arr[i-1][i] = q
    arr[i+1][i] = p
print(arr)
vector = [0] * n
starting_state= int(x/w) + 1
if x%w:
    starting_state += 1
vector[starting_state-1] = 1
print(vector)
a = np.array(arr)
c_prev = np.array(vector)
c = np.round(np.dot(a,c_prev),4)

while not np.allclose(c,c_prev):
    print(c)
    c_prev = c
    c = np.round(np.dot(a,c_prev),4)
print(c)
