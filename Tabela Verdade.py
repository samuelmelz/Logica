import ttg

print('Conjuncao -> and\nDisjuncao -> or\nImplicacao -> =>\nBi-implicacao -> =\nNegacao -> -\nParenteses -> (  )')

while True:
	numProp = int(input("\nNumero de proposicoes: "))
	p=str(input("Digite o radical 1: "))
	if numProp>=2:
		q=str(input("Digite o radical 2: "))
	if numProp>=3:
		r=str(input("Digite o radical 3: "))
	if numProp>=4:
		s=str(input("Digite o radical 4: "))

	if numProp==1:
		table=(ttg.Truths([p], [input("\nDigite a sentenca: ")], ints=False))
	elif numProp==2:
		table=(ttg.Truths([p, q], [input("\nDigite a sentenca: ")], ints=False))
	elif numProp==3:
		table=(ttg.Truths([p, q, r], [input("\nDigite a sentenca: ")], ints=False))
	elif numProp==4:
		table=(ttg.Truths([p, q, r, s], [input("\nDigite a sentenca: ")], ints=False))
	
	print(table)
	print("Esta expressao e uma " + table.valuation())
