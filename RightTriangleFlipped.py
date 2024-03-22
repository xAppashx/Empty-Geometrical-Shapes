def RightTriangleFlipped(Size):
	
	FirstLine = ['#'] * Size
	print(''.join(FirstLine))
	
	for Loop in range(Size - 2, -1, -1):
		for i in range(Loop + 1):
			if (i == 0) or (i == Loop):
				print('#', end = "")
			else: 
				print(' ', end= "")
			#else
		#for i in range
		print()
	#for Loop
	
	
#def RightTriangleFlipped




def Main():
	print("Please input the size of the triangle: ", end="")
	Size = int(input())
	RightTriangleFlipped(Size)
#def Main

Main()
