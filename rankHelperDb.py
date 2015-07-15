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
			for net in rank:
				self.rankBuddies[net].update(rank)
				rankSet.add(net)
			ranks.add(rankSet)

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

if __name__ == '__main__':
	db = rankHelperDb()
	db.loadNets("netFile.csv")
	if db.checkValidName("jen"):
		print db.getNetId("jen")