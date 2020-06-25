def subarrayXor(arr, n, m): 

	ans = 0 
	xorArr =[0 for _ in range(n)] 

	mp = dict() 


	xorArr[0] = arr[0] 

	for i in range(1, n): 
		xorArr[i] = xorArr[i - 1] ^ arr[i] 


	for i in range(n): 

		tmp = m ^ xorArr[i] 

		if tmp in mp.keys(): 
			ans = ans + (mp[tmp]) 


		if (xorArr[i] == m): 
			ans += 1
		mp[xorArr[i]] = mp.get(xorArr[i], 0) + 1

	return ans 

arr = [4, 2, 2, 6, 4] 
n = len(arr) 
m = 6

print("Number of subarrays having given XOR is", 
						subarrayXor(arr, n, m)) 

