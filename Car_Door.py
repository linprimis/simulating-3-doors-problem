#!/usr/bin/python3
from random import shuffle

Door=[0,0,1]
def NonSwitch():
	shuffle(Door)
	if Door[0]==1:
		return 1
	else:
		return 0

def Switch():
	shuffle(Door)
	if Door[1]==1 or Door[2]==1:
		return 1
	else:
		return 0
	
if __name__=='__main__':
	nSuccess=0
	sSuccess=0
	for i in range(0,10000):
		nSuccess+=NonSwitch()
	
	for i in range(0,10000):
		sSuccess+=Switch()
		
	print('For 10000 cases:\n')
	print(f'{"Wins when not switching":^30s}',f'{"Ratio to win":^30s}')
	print(f'{nSuccess:^30d}',f'{(nSuccess/10000):^30.5f}')
	print(f'{"Wins when switching":^30s}',f'{"Ratio to win":^30s}')
	print(f'{sSuccess:^30d}',f'{(sSuccess/10000):^30.5f}')
	
	
	
	

		
	
		
		
