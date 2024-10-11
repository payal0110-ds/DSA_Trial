# def print_all(grid):
#     for row in range(len(grid)):
#         for column in range(len(grid[0])):
#             item=grid[row][column]
#             print(item)

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# # print_all(grid)

# def print_all2(grid):
#     for column in range(len(grid[0])):
#         for row in range(len(grid)):
#             item=grid[row][column]
#             if row==column:
#                 print(item)
#
# print_all2(grid)


# def print_all2(grid):
#     for item in range(len(grid)):
#         if item%2==0:
#             print(grid[item])


# def even_mat(mat):
#     for row in range(len(mat)):
#         for column in range(len(mat[0])):
#             item=mat[row][column]
#             if item == "1":
#                 print(item)

# def even_mat(mat):
#     temp=0
#     for row in range(len(mat)):
#         for column in range(len(mat[0])):
#             item=mat[row][column]
#             if item == "1":
#                 temp=temp+1
#     print(temp)
#
# mat=[
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
#
# even_mat(mat)
#
# ar=[2,3,7,2]
# n=len(ar)
# # for i in range(n-1,-1,-1):
# #     print(ar[i])
# ar=ar[::-1]
# for i in range(n):
#     print(ar[i])
#
# def reverse_diagonal(mat):
#     n=len(mat)
#     for rows in range(n-1,-1,-1):
#         for cols in range(mat[0]):
#             if rows==cols:
#                 print(rows)


