def threeNumberSum(array, targetSum):
    n = len(array)
    ret = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if array[i]+array[j]+array[k] == targetSum:
                    ret.append([array[i],array[j],array[k]])
	return ret