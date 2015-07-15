import os
from rankHelperDb import *

db = None

#Configuration
netFile = "netFile.csv"
rankFile = "rankFile.csv"

def checkValidName(args):
	if len(args) == 1:
		name = args[0]
		print db.checkValidName(name)
	else:
		print "Invalid arguments. Usage: checkValidNames <name>"

def newRank(args):
	if len(args) < 1:
		print "No arguments provided. Usage: newRank <name1> <name2> <name3> <name4>"
	else:
		db.newRank(args)

if __name__ == "__main__":

	#Prepare folders
	os.system('touch ' + netFile)
	os.system('touch ' + rankFile)

	#Instantiate rankHelperDb
	db = rankHelperDb()
	db.loadNets(netFile)
	db.loadRanks(rankFile)

	#Start command prompt while loop
	keepGoing = True
	while keepGoing:
		line = raw_input(" > ")
		line = line.split()
		command = line[0]
		args = line[1:]

		if command == "q" or command == "Q" or command == "quit":
			keepGoing = False
		elif command == 'checkValidName':
			checkValidName(args)
		elif command == 'newRank':
			newRank(args)
