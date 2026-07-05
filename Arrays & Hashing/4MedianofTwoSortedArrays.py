def findMedianSortedArrays( nums1, nums2):
  m, n = len(nums1), len(nums2)

  i = j = 0
  arr = []

  while i < m and j < n:
      if nums1[i] <= nums2[j]:
          arr.append(nums1[i])
          i += 1
      else:
          arr.append(nums2[j])
          j += 1

  while i < m:
      arr.append(nums1[i])
      i += 1

  while j < n:
      arr.append(nums2[j])
      j += 1

  total = m + n

  if total % 2 == 0:
      return (arr[total // 2 - 1] + arr[total // 2]) / 2.0
  else:
      return arr[total // 2]