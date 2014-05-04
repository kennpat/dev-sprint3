# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Patrick Kennedy

#STILL A WORK IN PROCESS>>> BECAUSE IT WON'T FRIGGING WORK
#Will need to utilize chr and ord to convert the characters back and forth into numbers/characters

def convert(changeme):
	index = -1 
	answer = "    "
	while index < len(changeme):
		index = index + 1
		answer = answer + chr(ord((changeme[index] + 13-97)%26)).to_char
	print answer
	






Test = "aaaaa"

convert(Test)

print "BBBBB"












# """
# From Class:

# def Rot13(String):
# 	x = -1, string ans = ""
# 	while x < (string.length-1):
# 		x+1
# 		ans = ans + ((String[x]+13-97)%26).to_char
# 	return ans

# """


# """
# def rotate_word(string, number):
# 	#this will shift depending on the number entered
# 	Rotated = 0
# 	Rotted = string
# 	x = 0
# 	while x < number:
		
		
		
# 		#Rotted = chr(Rotated) + Rotted[:x] 

		
# 		if (Rotated + number) > 122:
# 			print "post 1"
# 			Rotated = (ord(string[x])-122) + number 
# 			Rotted = chr(Rotated) + Rotted[:x]

# 		elif (Rotated + number) > 90:
# 			print "post 2"
# 			Rotated = (ord(string[x])-90) + number
# 			Rotted = chr(Rotated) + Rotted[:x]

# 		else:
# 			print "post 3"
# 			Rotated = ord(string[x]) + number
# 			Rotted = chr(Rotated) + Rotted[:x]

		
# 		x = x + 1
# 		print Rotted 
# 		print x
# 	return Rotted



# PushIn = "patz"
# letterCount = len(PushIn)

# print rotate_word(PushIn, letterCount)


# #testing functionality

# #print ord('z')
# #print ord('Z')

# """

# """
# Tyler's example:

# def rot13(Word):
# 	for x in ((len/word)-1):
# 		word[x] + 13
# 		if(word[x])>122:
# 			return (word[x] - 26)
# 		else:
# 			return word[x]
# """












