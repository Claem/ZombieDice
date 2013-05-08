#!/usr/bin/env python
import random

"""Zombie Dice.  Create and make playable a game of zombie dice.
Die - A single die
Hand - a set of three die
Cup - a set, which holds all the dice currently in play
Pull - A function to pull a hand of dice from the cup
roll - a function to roll a hand of die"""

class Die(object):
	"""
	Roll a die and return the side it landed on
	"""
	def roll(self):
		return self.color + " " + random.choice(self.sides)

class GreenDie(Die):
	"""
	Define the sides on a Green Die
	"""
	def __init__(self):
		self.sides = ['brains', 'brains', 'brains', 'runner', 'runner', 'shotgun']
		self.color = "Green"

class YellowDie(Die):
	"""
	Define the sides on a Yellow Die
	"""
	def __init__(self):
		self.sides = ['brains', 'brains', 'runner', 'runner', 'shotgun', 'shotgun']
		self.color = "Yellow"

class RedDie(Die):
	"""
	Define the sides on a Red Die
	"""
	def __init__(self):
		self.sides = ['brains', 'runner', 'runner', 'shotgun', 'shotgun', 'shotgun']
		self.color = "Red"

class DieCup(object):
	"""
	Set up the cup with all the dice
	"""
	def __init__(self):
		self.dice = [GreenDie(), GreenDie(), GreenDie(),
		             GreenDie(), GreenDie(), GreenDie(),
					 YellowDie(), YellowDie(), YellowDie(),
					 YellowDie(), RedDie(), RedDie(), RedDie()]
		self.newturn()
					 
	def newturn(self):
		self.dicepool = self.dice
		random.shuffle(self.dicepool)
		
	def roll(self):
		print self.dicepool[0].roll()
		print self.dicepool[1].roll()
		print self.dicepool[2].roll()
		

if __name__ == "__main__":
	gd = DieCup()
	gd.roll()