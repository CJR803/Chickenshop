class menu():
	def __init__(self,chicken,fries,burgers,finished):
		self.chicken = chicken
		self.fries = fries
		self.burgers =burgers
		self.finished = finished
		self.total_items = chicken + fries + burgers
import datetime

menu_dict ={'chicken':1.85,'fries':0.89,'burgers':1.00}

day = datetime.datetime.today().weekday()
order_1 = menu(1,2,9,True)
# order_1 is what you woukld use for input
print('Enter None if you dont want to order an item \n eneter the amount of each number')
# print(day)
prices =[menu_dict['chicken'],menu_dict['fries'],menu_dict['burgers']]
print(prices)

total = 0

if order_1.chicken == None:
	print('i assume youre vegan then')

elif order_1.chicken > 1 and order_1.burgers > 1 and order_1.fries > 1 and order_1.finished == True:

	total = order_1.chicken * prices[0] + order_1.burgers * prices[2] + order_1.fries * prices[1]
	print('Amount Due')
	print(total)
elif order_1.chicken > 1 or order_1.fries > 1 or order_1.burgers > 1:

	total = order_1.chicken * prices[0] + order_1.burgers * prices[2] + order_1.fries * prices[1]
	print('Amount Due:')
	print(total)


elif order_1.chicken > 0 and order_1.burgers > 0 and order.fries > 0 and order_1.finished == True:

	total = order1.chicken * prices[0] + order_1.burgers * prices[2] + order_1.fries * prices[1]
	print('Amount Due:')
	print(total)

elif order_1.chicken > 0 and order_1.burgers > 0 and order.fries > 0 and order_1.finished == True and day == 1:

	total = order1.chicken * prices[0] + order_1.burgers * prices[2] + order_1.fries * prices[1]

	total = total * 0.75
	print('Amount Due:')
	print(total)

elif order_1.chicken > 0 and order_1.burgers > 0 and order.fries > 0 and order_1.finished == True and day == 1 and total_items >= 8:
	total =total * 0.50
	print(total)
elif order_1.finished == False:
	print('take your sweet time')

else:
	print('i get it youre not hungry yet please dont hesitate to come back next time')
