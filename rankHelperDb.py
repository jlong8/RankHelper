import string

class rankHelperDb:
	def __init__(self):
		self.ranks = list()
		self.nets = list()
		self.rankBuddies = list()

	def loadNets(self, netsFile):
		file = open(netsFile)
		netsLines = file.readlines()
		file.close()

		for line in netsLines:
			self.rankBuddies.append(set())
			thisNet = list()
			line = line.rstrip().split(",")
			for nickname in line:
				thisNet.append(nickname.lower())

			self.nets.append(thisNet)

	def loadRanks(self, ranksFile):
		file = open(ranksFile)
		ranksLines = file.readlines()
		file.close()

		rankSet = set()
		for rank in ranksLines:
			rank = rank.rstrip().split(",")
			rank = [ int(stringNum) for stringNum in rank ]
			self.addRankToRanks(rank)
			self.addRankToRankBuddies(rank)

	def getNetId(self, name):
		name = name.lower()
		index = None

		for i in range(0, len(self.nets)):
			net = self.nets[i]
			if name in net:
				index = i
		return index

	def checkValidName(self, name):
		numOccurrences = 0
		name = name.lower()

		for i in range(0, len(self.nets)):
			net = self.nets[i]
			if name in net:
				numOccurrences += 1

		if numOccurrences == 1:
			return True
		else:
			return False

	def newRank(self, args):
		rankInNums = self.convertRankToNums(args)
		self.addRankToRanks(rankInNums)
		self.addRankToRankBuddies(rankInNums)
		print self.ranks
		print self.rankBuddies

	def convertRankToNums(self, args):
		rankInNums = set()
		for name in args:
			rankInNums.add(self.getNetId(name))
		return rankInNums

	def addRankToRanks(self, rankInNums):
		thisRank = set()
		for netId in rankInNums:
			thisRank.add(netId)
		self.ranks.append(thisRank)

	def addRankToRankBuddies(self, rankInNums):
		for netId in rankInNums:
			self.rankBuddies[netId].update(rankInNums)

	def writeRanksToFile(self, ranksFilename):
		ranksFile = open(ranksFilename, 'w') #Currently overwrites the entire file each time
		for rank in self.ranks:
			rankString = ','.join(map(str, rank))  #Make into a comma-separated string
			ranksFile.write(rankString + "\n")
		ranksFile.close()

	def printRanks(self):
		for rank in self.ranks:
			rankString = ','.join(map(str, rank))
			print rankString

	def printNets(self):
		for net in self.nets:
			netString = ", ".join(map(str, net))
			print netString

	def checkRank(self, potentialRank):
		potentialRankInNums = self.convertRankToNums(potentialRank)
		for net1 in potentialRankInNums:
			for net2 in potentialRankInNums:
				if net1 != net2 and net2 in self.rankBuddies[net1]:
					return False
		return True

if __name__ == '__main__':
	db = rankHelperDb()
	db.loadNets("netFile.csv")
	if db.checkValidName("jen"):
		print db.getNetId("jen")