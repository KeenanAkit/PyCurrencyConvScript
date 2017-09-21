import requests,json
validCheck = requests.get('http://api.fixer.io/latest')
validCheckDict = validCheck.json()['rates']
while True:
	baseCurrency = input("Enter starting currency: ")
	currencyCount = input("Enter ammount of currency: ")
	if baseCurrency in validCheckDict:
		break
	else:
		print("Thats not a valid currency")
response = requests.get('http://api.fixer.io/latest?base=%s' % (baseCurrency))
currencyDict = response.json()['rates'] 
while True:
	targetCurrency = input("Enter desired transfer currency: ")
	if targetCurrency in currencyDict:
		break
	elif targetCurrency == baseCurrency:
		print("You cannot exchange the same currency")
	else:
		print("Thats not a valid currency")
while True:
	exchangeRate = currencyDict[targetCurrency]
	print (exchangeRate)
	total = int(currencyCount) * exchangeRate
	print (total)
	break