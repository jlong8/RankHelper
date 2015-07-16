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
		for net in args:
			if not db.checkValidName(net):
				print "Error: Invalid name " + net
				return
		db.newRank(args)

def save():
	db.writeRanksToFile(rankFile)

def printSummary():
	print "Ranks:"
	db.printRanks()
	print ""
	print "Nets:"
	db.printNets()


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
		args = " ".join(line[1:])
		args = args.split(",")

		if command == "q" or command == "Q" or command == "quit":
			print "Saving..."
			save()
			keepGoing = False
		elif command == 'checkValidName':
			checkValidName(args)
		elif command == 'newRank':
			newRank(args)
		elif command == 'save':
			save()
		elif command == 'summary':
			printSummary()
		else:
			print "Command " + command + " not found."
