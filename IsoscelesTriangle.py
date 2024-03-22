def IsoscelesTriangle(Height):
	
	NbPrinted = 1
	NbSpaces = Height
	FirstSpaces = [' '] * (Height - 2)
	Spaces = [' '] * (Height - 1)
	
	#printing the first line
	print(''.join(FirstSpaces), '#')
	
	#printing the rest
	for Loop in range(Height - 2):
		NbPrinted += 1
		Spaces.pop(0)
		
		#Printing the spaces before the #
		print(''.join(Spaces), end = "")
		
		#Printing the left #
		print('#', end = "")
		
		#Printing the spaces in betweeing the two #
		Middle = [' '] * ((Loop*2) + 1)
		print(''.join(Middle), end = "")
		
		#Printing the right #
		print('#')
	#for Loop
	
	#Printing the last line
	if (Height > 1):
		LastLine = ['#'] * ((NbPrinted * 2) + 1)
		print(''.join(LastLine))
	#if
	
#def IsoscelesTriangle




def Main():
	print("Please input the height of the triangle: ", end="")
	Height = int(input())
	IsoscelesTriangle(Height)
#def Main

Main()
