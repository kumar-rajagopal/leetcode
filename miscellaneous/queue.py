queue = [1,2,3,4,5]
def enque(i, queue=[]):
	if i > 5:
		return
	else:
		queue.append(i)
		i += 1
		enque(i, queue=queue)
	return queue

def deque(queue):
	print(len(queue))
	if len(queue) == 0:
		print( "finished")
	else:
		b = queue.pop(0)
		#print(b)
		deque(queue)
	
	return queue
q = enque(1)
#q = deque(queue)
print (q)
