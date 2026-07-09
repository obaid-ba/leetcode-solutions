def allCellsDistOrder(rows, cols, rCenter, cCenter):
  cells = []
  for i in range(rows):
    for j in range(cols ):
      cells.append([i,j])
  cells.sort(key=lambda cell: abs(rCenter - cell[0]) + abs(cCenter - cell[1]))
  return cells 