from random import choice, random, randint
from math import sqrt
from time import sleep
import sys
import copy

#Test
sudoku=[[0,8,0, 6,0,0, 1,5,0],
		[1,0,5, 0,0,9, 0,0,6],
		[3,0,0, 1,0,0, 0,2,0],
		[0,9,0, 2,0,1, 6,0,5],
		[0,0,0, 0,0,0, 0,0,0],
		[2,0,1, 9,0,7, 0,8,0],
		[0,3,0, 0,0,2, 0,0,7],
		[5,0,0, 7,0,0, 8,0,9],
		[0,6,4, 0,0,3, 0,1,0]]


#Test 2
'''sudoku=[[4,0,7, 0,0,0, 9,0,1],
		[0,9,0, 0,0,0, 0,5,0],
		[2,0,0, 0,6,0, 0,0,7],
		[0,0,0, 7,3,4, 0,0,0],
		[0,0,0, 0,5,0, 0,0,0],
		[0,0,5, 0,0,0, 7,0,0],
		[5,3,0, 9,0,2, 0,6,4],
		[6,0,0, 1,4,5, 0,0,2],
		[0,0,0, 0,0,0, 0,0,0]]
'''

def initialisePop(grid, popNumber):
	"""
	Initialises the population
	@param grid: Is the given grid the program needs to solve to make a population out of
	@param popNumber: Is the given population size
	@return: A list of all the grids in the population
	"""
	return [makeInd(grid) for _ in range(popNumber)]

def calculateFitnessPop(population, generation=0):
	"""
	Calculates the fitness of the population
	@param population: List of all the grids that represent the population
	@param generation: The current generation being handled
	@return: A list of all the fitnesses of the population
	"""
	return [calculateFitness(fitness, generation) for fitness in population]

def selectPop(population, fitness_population, populationSize):
	"""
	Selects the parents for the next generation
	@param population: List of all the grids that represent the population
	@param fitness_population: List of all the fitnessess of the population
	@param populationSize: Is the given population size
	@return: A list of all the parents
	"""
	sortedPopulation = sorted(zip(population, fitness_population), key = lambda ind_fit: ind_fit[1])
	return [ individual for individual, fitness in sortedPopulation[int(populationSize * 0.5):]]

def crossoverPop(population, populationSize):
	"""
	Makes offsprings using a uniform crossover
	@param population: List of all the grids that represent the population
	@param populationSize: Is the given population size
	@return: A list of all the newly made offsprings
	"""
	return [ crossoverInd(choice(population), choice(population)) for _ in range(populationSize) ]

def crossoverInd(individual1, individual2):
	"""
	Applies the crossover operator to make a new offspring
	@param individual1: Parent 1
	@param individual2: Parent 2
	@return: The offspring
	"""
	return [ list(choice(ch_pair)) for ch_pair in zip(individual1, individual2) ]

def mutatePop(population, grid):
	"""
	Mutates each offspring in the population
	@param population: List of all the grids that represent the population
	@param grid: Is the given grid the program needs to solve
	@return: The mutated population
	"""
	return [ mutateInd(individual, grid) for individual in population ]

def mutateInd(individual, grid):
	"""
	Mutates a given grid
	@param individual: The grid that needs to be mutated
	@param grid: Is the given grid the program needs to solve
	@return: The mutated grid
	"""
	for i in range(9):
		if (random() < 0.1):
			hasMutated = False
			while(hasMutated == False):
				rand1 = randint(0,8)
				rand2 = randint(0,8)
				if (grid[i][rand1] == 0 and grid[i][rand2] == 0):
					individual[i][rand1], individual[i][rand2] = individual[i][rand2], individual[i][rand1]
					hasMutated = True
	return list(individual)


def calculateFitness(grid, generation):
	"""
	Calculates the fitness of a grid
	@param grid: The grid whose fitness needs to be calculates
	@param generation: The curent generation
	@return: The grid's fitness
	"""
	fitness = 0

	#Fitness for each column
	for i in range(9):
		L = []
		for j in range(9):
			L.append(grid[j][i])
		for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1

	#Fitness for each box
	L = []
	for i in range(3):
		for j in range(3):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3,6):
		for j in range(3):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(6,9):
		for j in range(3):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3):
		for j in range(3,6):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3,6):
		for j in range(3,6):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(6,9):
		for j in range(3,6):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3):
		for j in range(6,9):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(3,6):
		for j in range(6,9):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1
	L = []
	for i in range(6,9):
		for j in range(6,9):
			L.append(grid[i][j])
	for item in range(9):
			if (L[item] in L[item+1:]) == False:
				fitness += 1

	#Checking whether a solution is found
	if (fitness/162 == 1.0):
		print()
		print("Solution found!")
		printSudoku(grid)
		print("Generations:", generation )
		sys.exit()

	return fitness/162

def makeInd(grid):
	"""
	Creates a new individual
	@param grid: Is the given grid the program needs to solve
	@return: The individual
	"""
	L = []
	for i in range(9):
		possibleInt = [1,2,3,4,5,6,7,8,9]
		L.append(list(grid[i]))
		for j in range(9):
			if (L[i][j] == 0):
				hasFoundInt = False
				while(hasFoundInt == False):
					pickedInt = choice(possibleInt)
					if(pickedInt not in L[i]):
						L[i][j] = pickedInt
						possibleInt.remove(pickedInt)
						hasFoundInt = True
					else:
						possibleInt.remove(pickedInt)
	return L

def printSudoku(grid):
	"""
	Prints a sudoku to make it more readable
	@param grid: Is the grid that needs to be printed out
	"""
	iteration = 0
	for i in grid:
		print(i[0], i[1], i[2], "||", i[3], i[4], i[5], "||", i[6], i[7], i[8])
		iteration += 1
		if (iteration == 3 or iteration == 6):
			print("=======================")
	print("")

def evolve(grid, populationSize):
	"""
	Tries to find the solution to a sudoku by evolving it using genetic algorithm
	@param grid: The given grid that needs to be solved
	@param populationSize: The population size
	"""
	iteration = 0
	minimaFixer = 0
	population = initialisePop(grid, populationSize)
	fitnessPop = calculateFitnessPop(population)
	while (iteration < 10000):
		iteration += 1
		parentsPop = selectPop(population, fitnessPop, populationSize)
		offspringPop = crossoverPop(parentsPop, populationSize)
		population = mutatePop(offspringPop, grid)
		lastFitness = sorted(fitnessPop)[-1]
		fitnessPop = calculateFitnessPop(population, iteration)
		if (lastFitness == sorted(fitnessPop)[-1]):
			minimaFixer += 1
			if minimaFixer == 25:
				print("Restarting Population...")
				population = initialisePop(grid, populationSize)
				fitnessPop = calculateFitnessPop(population)
				minimaFixer = 0
				iteration = 0
				sleep(1)
		else:
			minimaFixer = 0
		print("Generation:", iteration, "| Best fitness %.3f" % sorted(fitnessPop)[-1])


if __name__ == "__main__":
		print("Input grid:")
		printSudoku(sudoku)
		sleep(1)
		evolve(sudoku, 1000)
