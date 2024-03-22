def RightTriangle(Size):
	
	Pivot = 1
	
	for Loop in range(Size - 1):
		for i in range(Loop + 1):
			if (i == 0) or (i == Loop):
				print('#', end = "")
			else: 
				print(' ', end= "")
			#else
		#for i in range
		print()
	#for Loop
	
	LastLine = ['#'] * Size
	print(''.join(LastLine))
	
#def Triangle




def Main():
	print("Please input the size of the triangle: ", end="")
	Size = int(input())
	RightTriangle(Size)
#def Main

Main()
