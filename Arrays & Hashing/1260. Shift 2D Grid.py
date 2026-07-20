def shiftGrid(grid, k):
  arr =[num for row in grid for num in row]
  while(k>0):
    arr.insert(0, arr.pop())
    k-=1
  f=0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      grid[i][j] = arr[f]
      f+=1
  return  grid