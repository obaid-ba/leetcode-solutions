def minNumber(nums1, nums2):
    first = min(nums1)
    second = min(nums2)
    common =  list(set(nums1) & set(nums2))
    if(common):
        return min(common)
    return   min(int(str(first) + str(second)) , int(str(second) + str(first)))
