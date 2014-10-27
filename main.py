class transaction:
	def __init__(self, buyer, seller, name, price):
		self.buyer = buyer
		self.seller = seller
		self.name = name
		self.price = price
		
	def getBuyer(self):
		return self.buyer
	def getSeller(self):
		return self.seller
	def getName(self):
		return self.name
	def getPrice(self):
		return self.price

class transactions:
	def __init__(self):
		self.log = []
	def clearLog(self):
		self.log = []
	def addTransaction(self, transaction):
		self.log.append(transaction)
	def printTransactions(self):
		for item in self.log:
			print item.seller+" sold "+item.name+" to "+item.buyer+" for $"+str(item.price)
			#print item.seller+ " sold "+item.name+" to "item.buyer+" for "+item.price

class seller:
	def __init__(self, name):
		self.name = name
	def getName(self):
		return self.name
		
class item:
	def __init__(self, name, price, seller):
		self.name = name
		self.price = price
		self.seller = seller.getName()
	def getPrice(self):
		return self.price
	def getSeller(self):
		return self.seller
	def getName(self):
		return self.name
	def printValues(self):
		print "name: "+self.name
		print "price: "+str(self.price)

class buyer:
	def __init__(self, name, bid0=0, bid1=0, bid2=0, bid3=0, bid4=0):
		self.bids = []
		self.bids.extend([bid0, bid1, bid2, bid3, bid4])
		self.name = name
	def printValues(self):
		print "name: "+self.name
		print "bids: "+str(self.bids)
	def getBid(self, index):
		return self.bids[index]
	def getName(self):
		return self.name
		
def main():
	seller1 = seller("Charles")
	seller2 = seller("Samantha")
	seller3 = seller("Louis")
	seller4 = seller("Dharma")
	seller5 = seller("Jess")
	item1 = item("Couch", 100, seller1)
	item2 = item("Television", 120, seller2)
	item3 = item("Printer", 140, seller3)
	item4 = item("Computer", 160, seller4)
	item5 = item("Book", 180, seller5)
	buyer1 = buyer("Greg", 110, 20, 30, 40, 50)
	buyer2 = buyer("Dave", 10, 120, 30, 40, 50)
	buyer3 = buyer("Joe", 10, 20, 130, 40, 50)
	buyer4 = buyer("Susan", 10, 20, 30, 140, 50)
	buyer5 = buyer("Lisa", 10, 20, 30, 40, 200)
	
	items = [item1, item2, item3, item4, item5]
	buyers = [buyer1, buyer2, buyer3, buyer4, buyer5]
	log = transactions()
	
	print "The following items are up for sale:"
	for i in range(0, 5):
		print items[i].getName()+" being offered by "+items[i].getSeller()+" for the starting price of $"+str(items[i].getPrice())
	print
	
	for i in range(0, 5):#5 defined auction items are always assumed!, loop through each
		currentWinner = buyers[0]
		for bidder in buyers:#check all bidders for highest legal bid
			if bidder.getBid(i) > currentWinner.getBid(i):
				currentWinner = bidder
		if currentWinner.getBid(i) >= items[i].getPrice():#add winning bid to transaction log
			#print currentWinner.getName()+" wins bid "+str(i+1)+"!"
			tempTransaction = transaction(currentWinner.getName(), items[i].getSeller(), items[i].getName(), currentWinner.getBid(i))
			log.addTransaction(tempTransaction)
			print currentWinner.getName()+" has won "+items[i].getName()+ " for $"+str(items[i].getPrice())+".",
		else:#no bid was high enough!
			print "Minimum bid not met for "+items[i].getName()+"(item "+str(i+1)+")"+", no winner!",
		
		#print remaining auctions items
		if i < 4:
			print "The following items are still up for auction:[",
			print items[i+1].getName(),
		for j in range(i+2, 5):#print remaining auction items
			print ";"+items[j].getName(),
		if i < 4:
			print "]"
	print "There are no more items to auction."
	
	#log.printTransactions() #prints the transactions which occured, doesn't include unsold items

	print "Auction simulation complete!"

	
main()
