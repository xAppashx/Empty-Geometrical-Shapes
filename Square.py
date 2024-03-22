def Square(Size):
	
	FullLine = ['#'] * Size
	print(''.join(FullLine))
	
	MiddleLine = [' '] * (Size - 2)
	
	for Loop in range(Size - 2):
		print('#', end = "")
		print(''.join(MiddleLine), end = "")
		print('#')
	#
	
	print(''.join(FullLine))
	
#def Square



def Main():
	print("Please input the size of the square: ", end="")
	Size = int(input())
	Square(Size)
#def Main

Main()
