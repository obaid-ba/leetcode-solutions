def floodFill(image, sr, sc, color):
  old_color = image[sr][sc]
  if old_color == color:
    return image
  m = len(image)
  n = len(image[0])
  def dfs(i,j):
    if i<0 or i>=m or j<0 or j>=n or image[i][j] != old_color:
      return
    image[i][j] = color
    dfs(i,j+1) 
    dfs(i,j-1) 
    dfs(i+1,j) 
    dfs(i-1,j)
  dfs(sr,sc)
  return image