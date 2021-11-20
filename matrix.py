# 1 - masala

# a = [ ]
# m,n = 4,5
# for i in range(1,m+1) :
#     b = []
#     for j in range(1,n+1) :
#         b.append(10*j)
#     a.append(b)
# for i in range(0,m) :
#     for j in range(0,n) :
#         print(a[i][j],end='\t')
#     print()

# 2 - masala

# a = [ ]
# m,n = int(input()),int(input())
# for i in range(m) :
#     b = []
#     for j in range(n) :
#         b.append(5*j)
#     a.append(b)
# for i in range(0,m) :
#     for j in range(0,n) :
#         print(a[i][j],end='\t')
#     print()

# 3 - masala

# a = []
# m,n = int(input()),int(input())
# for i in range(m) :
#     b = []
#     for j in range(n) :
#         b.append(m)
#     a.append(b)
# for i in range(m) :
#     for j in range(n) :
#         print(a[i][j],end='\t')
#     print()

# 4 - masala

# a = []
# m,n = int(input()),int(input())
# for i in range(m) :
#     b = []
#     for j in range(n) :
#         b.append(n)
#     a.append(b)
# for i in range(m) :
#     for j in range(n) :
#         print(a[i][j],end='\t')
#     print()

# 5 - masala

# a = []
# m,n = int(input()),int(input())
# d = 5
# for i in range(1,m) :
#     b = []
#     for j in range(1,n) :
#         if j==0 :
#             b.append(m)
#         else :
#             b.append(m+d)
#     a.append(b)
# for i in range(m) :
#     for j in range(n) :
#         print(a[i][j],end='\t')
#     print()

# 6 - masala

# a = []
# m,n = int(input()),int(input())
# q = 2
# for i in range(m) :
#     b = []
#     for j in range(n):
#         if j ==0 :
#             b.append(m)
#     a.append(b)
# for i in range(m) :
#     for j in range(n):
#         print(a[i][j],end='\t')
#     print()

# xato ishladi

# 7 - masala

# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# k = 2
# print(a[k])

# 8 - masala

# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# k = 2
# for i in range(len(a[0])) :
#     for j in range(len(a[0])) :
#         if j==k :
#             print(a[i][k])

# 9 - masala

# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# for i in range(0,len(a),2) :
#     print(a[i],end='\t')

# 10 - masala

# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# for i in range(1,len(a[0]),2) :
#     for j in range(len(a[0])) :
#         print(a[j][i])
#     print()

# 11 - masala

# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9],
#      [10,11,12]]
# for i in range(4) :
#     if i%2==0 :
#         for j in range(2,-1,-1):
#             print(a[i][j],end='\t')
#     else:
#         for j in range(3):
#             print(a[i][j],end='\t')
#     print()

# 12 - masala

# a = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# for j in range(3) :
#     if j%2!=0 :
#         for i in range(2,-1,-1):
#             print(a[i][j],end='\t')
#     else:
#         for i in range(3) :
#             print(a[i][j],end='\t')
#     print()

# 17 - masala

# a = []
# m,n = int(input()),int(input())
# for i in range(m):
#     b = []
#     for j in range(n) :
#         b.append(10*j+i)
#     a.append(b)
# k = int(input())
# for i in range(m) :
#     for j in range(n) :
#         print(a[i][j],end='\t')
#     print()
# print(sum(a[k]))

# 18 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# k = 0
# m,n = 0,1
# for i in range(4):
#     for j in range(4):
#         if k ==j :
#           m +=a[i][k]
#           n*=a[i][k]
# print(m,n)

# 19 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# for i in range(4) :
#     print(sum(a[i]))

# 20 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# for i in range(4) :
#     kopaytma = 1
#     for j in range(4) :
#         kopaytma *=a[j][i]
#     print(kopaytma)

# 21 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# for i in range(1,4,2) :
#     print(sum(a[i])/4)

# 22 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# for i in range(0,4,2) :
#     yigindi = 0
#     for j in range(4) :
#         yigindi+=a[i][j]
#     print(yigindi)

# 23 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# for i in range(4) :
#     print(min(a[i]))

# 24 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# for j in range(4):
#     max = a[0][j]
#     for i in range(4):
#         if max <a[i][0] :
#             max = a[i][j]
#     print(max)

# 25 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# b = []
# for i in range(4) :
#     b.append(sum(a[i]))
# print(max(b))

# 26 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# m = 0
# b = []
# for i in range(4) :
#     kopaytma = 1
#     for j in range(4) :
#         kopaytma*=a[j][i]
#     b.append(kopaytma)
# min = b[0]
# print(b)
# for i in range(4) :
#     if min>b[0] :
#         min = b[0]
#         m+=1
# print(min,m)

# 27 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# yigindi = 0
# b = []
# for i in range(4) :
#     for j in range(4) :
#         yigindi+=a[i][j]
#     b.append(yigindi)
#     print(yigindi)
# m = 0
# min = b[0]
# for i in range(4) :
#     if min > b[i] :
#         min=b[i]
#         m+=1
# print(min)
# print(max(a[m]))

# 28 - masala

# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]
# b = []
# for i in range(4) :
#     yigindi = 0
#     for j in range(4) :
#         yigindi+=a[j][i]
#     print(yigindi)
#     b.append(yigindi)
# max = b[0]
# m =0
# for i in range(4) :
#     if max <b[i] :
#         max = b[i]
#         m+=1
# min = a[0][m]
# for i in range(4) :
#     for j in range(4) :
#         if min >a[i][m] :
#             min = a[i][m]
# print(min)

# 29 - masala

a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
m = 0
for i in range(4):
    yigindi = 0
    for j in range(4) :
        yigindi+=a[i][j]
    print(yigindi/4)
