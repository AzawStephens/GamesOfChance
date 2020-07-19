import random

money = 100

def flip(whichSide,betAmount):
	headsOrTails = random.randint(1,2)
	global money
	side = ""
	message =""
	if headsOrTails == 1:
		side = "Heads"
	else:
		side = "Tails"
	if betAmount > money or betAmount < 0:
		message = "You don't have enough money to bet that much OR you've betted a negative number mate"
		return message
			
	if whichSide == side:
		money += betAmount
		message = "You got it! And you've won $"+str(betAmount)
		
	else:
		money-= betAmount
		message = "You got it WRONG! And you've LOST $"+str(betAmount)
		
	return message	
def choHan(userGuess, waiger):
	global money
	diceOne = random.randint(1,6)
	diceTwo = random.randint(1,6)
	total = diceOne + diceTwo
	answer =""
	message =""
	if waiger > money or waiger <0:
		message = "You don't have enough money to bet that much OR you've betted a negative number mate"
		return message
	if total % 2 == 0:
		answer = "Even"
	else:
		answer ="Odd"
	if userGuess == answer:
		money += waiger
		message = "YOU GOT IT! AND YOU EARNED $"+str(waiger)+"! FOR A TOTAL MONEY AMOUNT OF $"+str(money)
	else:
		money -= waiger
		message = "You got it WRONG and you lost -$"+str(waiger)+" unfourtunetly."
	return message
def cardGame(waiger):
	global money
	pulledCard = random.randint(1,10)
	message = ""
	cards = [1,2,3,4,5,6,7,8,9,10]
	removeCard = cards.remove(pulledCard)
	cardNumber = cards[random.randint(0,8)]
	if waiger > money or waiger <0:
		message = "You don't have enough money to bet that much OR you've betted a negative number mate"
		return message
	if cardNumber > pulledCard:
		money-= waiger
		message = "Your card number is "+str(pulledCard)+ " and is lower than other player's card of "+str(cardNumber)+ ". You lost and gave $"+str(waiger)+" to the other player."
	elif pulledCard > cardNumber:
		money += waiger
		message = "YOUR CARD RULES CAUSE IT WAS  "+str(pulledCard)+" AND THE OTHER PLAYERS CARD NUMBER WAS ONLY "+str(cardNumber)+"! YOU WIN $"+str(waiger)+" FROM THE OTHER PLAYER!"

	return message

def roulette(guess, waiger):
	global money
	randomNumber = random.randint(0,36)
	winningAmount = random.randint(300,1000)
	message = ""
	if waiger > money or waiger <0:
		message = "You don't have enough money to bet that much OR you've betted a negative number mate"
		return message
	if randomNumber <= 18 and str.lower(guess) == "lower" and randomNumber != 0:
		money += 5
		message = "CONGRATULATIONS THE BALL LANDED ON "+str(randomNumber)+" Which qualifies as a Lower number! YOU WIN $5.00!!"
	elif randomNumber >=19 and str.lower(guess) == "higher":
		money += 5
		message = "CONGRATULATIONS THE BALL LANDED ON "+str(randomNumber)+" Which qualifies as a Higher number! YOU WIN $5.00!!"
	elif randomNumber == 0:
		money -= waiger
		message = "OH! Sorry buddy, not this time! the ball landed on "+str(randomNumber)+"!!! You LOSE $"+str(waiger)+"! Better luck next time"
	elif str.lower(guess) == "odd" and randomNumber % 2 !=0 and randomNumber != 0:
		money += 1
		message = "CONGRATULATIONS!! THE BALL LANDED ON "+str(randomNumber)+" WHICH IS ODD! YOU WIN $1.00!!!"
	elif str.lower(guess) == "even" and randomNumber % 2 ==0 and randomNumber != 0:
		money += 1
		message = "CONGRATULATIONS!! THE BALL LANDED ON "+str(randomNumber)+" WHICH IS EVEN! YOU WIN $1.00!!!"
	elif guess == randomNumber and randomNumber != 0:
		money += winningAmount
		message = "CONGRATULATIONS!! THE BALL LANDED ON "+str(randomNumber)+" WHICH IS YOUR GUESSED NUMBER! YOU WIN $"+str(winningAmount)+"!!!"
	else: 
		money -= waiger
		message = "The ball landed on "+str(randomNumber)+" you LOST $"+str(waiger)+" better luck next time."
	return message


#Call your game of chance functions here	
print(flip("Heads",20)+" MONEY BALANCE: $"+str(money))
print(choHan("Odd",50)+" MONEY BALANCE: $"+str(money))
print(cardGame(30)+" MONEY BALANCE: $"+str(money))
print(roulette("even",20)+" MONEY BALANCE: $"+str(money))
