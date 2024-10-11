mat = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# def iceland(mat):
#     count=0
#     def search(row, col):
#         mat[rows][cols]="0"
#         if cols+1<len(mat[0]) and mat[rows][cols+1]=="1":
#             search(row,col+1)
#         if cols-1>=0 and mat[rows][cols-1]=="1":
#             search(row,col-1)
#         if rows+1<len(mat) and mat[rows+1][cols]=="1":
#             search(row+1,col)
#         if rows-1>=0 and mat[rows-1][cols]=="1":
#             search(row-1,col)
#
#     for rows in range(len(mat)):
#         for cols in range(len(mat[1])):
#             element=mat[rows][cols]
#             if element=="1":
#                 search(rows,cols)
#                 count+=1
#     return count
#
# x=iceland(grid)
# print(x)


# class Solution:
#     def numIslands(self, grid):
#         def foo(idx, idy):
#             grid[idx][idy] = '0'
#             if idx - 1 >= 0 and grid[idx - 1][idy] == '1': foo(idx - 1, idy)
#             if idx + 1 < len(grid) and grid[idx + 1][idy] == '1': foo(idx + 1, idy)
#             if idy - 1 >= 0 and grid[idx][idy - 1] == '1': foo(idx, idy - 1)
#             if idy + 1 < len(grid[0]) and grid[idx][idy + 1] == '1': foo(idx, idy + 1)
#
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     foo(i, j)
#                     count += 1
#         return count

class Sol:
    def iceland(self,mat):
        count = 0

        def search(x, y):
            mat[x][y] = '0'
            if y + 1 < len(mat[0]) and mat[x][y + 1] == '1':
                search(x, y + 1)
            if y - 1 >= 0 and mat[x][y - 1] == '1':
                search(x, y - 1)
            if x + 1 < len(mat) and mat[x + 1][y] == '1':
                search(x + 1, y)
            if x - 1 >= 0 and mat[x - 1][y] == '1':
                search(x - 1, y)
            return
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                element = mat[x][y]
                if element == '1':
                    search(x, y)
                    count += 1
        return count

# grid =[["1"]]
ob=Sol()
print(ob.iceland(mat))