#Let's give this another go


#grab the file and assign it to a holder
cipherfile = open('the-last-cypher.txt')
dumpfile = open('dumpfile.txt', 'w')
#So let's try to apply what was in Chapter 9 to this


def FileTransit(fin):
	line = fin.readline()
	holder = ''
	for line in fin:
		word = line.strip()
		holder = Rot13Exchange(word)
		print holder
		#print dumpfile

#Now to plug in a rot13 cypher for each word

def Rot13Exchange(word):
	letter = ''
	ascii = 0
	SendBack = ''
	for letter in word:
		ascii = ord(letter)+13
		SendBack = SendBack[:-1] + chr(ascii)

	return SendBack


FileTransit(cipherfile)










