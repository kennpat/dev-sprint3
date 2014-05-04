# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Patrick Kennedy
#4/27/14
import string

#Exercise 9.1 - 

def TwentyOrMore(fin):
	line = fin.readline()
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print word

fin = open('words.txt')


#TwentyOrMore(fin)

#Results in 3 words: counterdemonstrations, hyperagressiveness, and microminiaturizations

#Exercise 9.2 - 

def has_no_e(word):
	index = 0
	while index < len(word):
		if word[index] == 'e':
			#print 'has an E!'
			return False
		index = index + 1
	return True

def filetransit(fin):
	totalcounter = 0
	ecounter = 0

	line = fin.readline()
	for line in fin:
		word = line.strip()
		totalcounter = totalcounter + 1
		if has_no_e(word) == True:
			#print 'we got a true!'
			ecounter = ecounter + 1
	print "The percentage of words in the list with no letter 'e' is: "
	printed_result = ((ecounter/totalcounter) * 100)
	print printed_result
	
#Results - I know the traversals and tests are working, but for some reason my attempt to print out a percentage is just going nowhere
# I also tried to use the 'in' operator as shown in the text, but it kept blowing up so I did it using an index

#filetransit(fin)

#Exercise 9.3 - 

#attempting to use the 'in' operator for this one

def third_traversal(fin):
	line = fin.readline()
	to_avoid = get_user_input()
	wordcounter = 0

	for line in fin:
		word = line.strip()
		if avoids(word, to_avoid) == True:
			wordcounter = wordcounter + 1
	print "the number of words with the forbidden letters is: "
	print wordcounter

def get_user_input():
	print "Please enter some characters that you don't want to have within words pulled from the list:"
	stuff = raw_input()
	return stuff

def avoids(word, dont_use):
	letter = ''
	for letter in word:
		if letter in dont_use:
			return False
	return True



#third_traversal(fin)

#results - I'm pretty sure my avoids function is messed up... wait now it works. I think.


#Exercise 9.4 - 

def uses_only(word, comparo):
	letter = ''
	counter = 0
	for letter in word:
		if letter in comparo:
			counter = counter + 1
	if counter == len(word):
		return True


#that should do the trick

