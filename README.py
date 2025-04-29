# Linear-algebra-class-project
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


print(arr)

arr[n][0] = 1
arr[n-1][n-1] = 1
# for i in range(1,n-1):
#     arr[i-1][i] = q
#     arr[i+1][i] = p
print(arr)
vector = [0] * n
starting_state= int(x/w) +1
if x%w:
    starting_state+=1
print(starting_state)
vector[starting_state-1] = 1
print(vector)

arr = [[0 for i in range(n)] for j in range(n)]
arr[0][0] = 1
arr[n-1][n-1] = 1
for i in range(1,n-1):
    arr[i-1][i] = q
    arr[i+1][i] = p
print(arr)


