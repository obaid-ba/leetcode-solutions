def trimMean( arr):
  arr.sort()
  ele = int(0.05 * len(arr))
  return sum(arr[ele:-ele])/(len(arr)-2*ele)