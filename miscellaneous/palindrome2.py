def palindrome(input, i=0, j=1):
	 
	store = []
	while(j < len(input)-1):
		if input[i] == input[j]:
			store.append(input[i] + input[j])
			i += 1; j+=1
			palindrome(input, i, j)
		i += 1
		j += 1
	return store

input = 'This is aa sammple stringgg to teeest'
print(palindrome(input))