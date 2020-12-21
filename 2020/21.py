# cLx 2020 day 21 (unstable version)

# ~ import operator

def solve(filename, assertPart1=None, assertPart2=None):
	print("Solving:", filename)
	fd = open(filename)
	foodsAllergens = {}
	allergens = set()
	ingredients = set()

	for line in fd:
		line = line.strip()
		line = line.split(" (contains ", 1)
		line_ingredients = tuple(line[0].split())
		line_allergens = set(line[1].replace(")", "").split(", "))

		for allergen in line_allergens:
			allergens.add(allergen)

		for ingredient in line_ingredients:
			ingredients.add(ingredient)

		foodsAllergens[line_ingredients] = line_allergens

	print("All allergens:", allergens)
	print("All ingredients:", ingredients)
	print()

	ingredientsAllergensCandidates = {}
	for ingredient in ingredients:
		ingredientsAllergensCandidates[ingredient] = {}

	for food in foodsAllergens:
		allergensInsideFood = foodsAllergens[food]
		print(food, '=>', allergensInsideFood)
		for ingredient in food:
			for allergen in allergensInsideFood:
				if allergen not in ingredientsAllergensCandidates[ingredient]:
					ingredientsAllergensCandidates[ingredient][allergen] = 0
				ingredientsAllergensCandidates[ingredient][allergen]+=1
	print()

	knownIngredients = {}

	while(True):
		candidateIngredient = None
		candidateAllergen = None
		candidateScore = 0
		for ingredient in ingredientsAllergensCandidates:
			data = ingredientsAllergensCandidates[ingredient]
			data = sorted(data.items(), key=lambda i:i[1], reverse=True)

			if len(data) == 1 or len(data) > 1 and data[0][1] > data[1][1]:
				if data[0][1] >= candidateScore:
					if data[0][1] > candidateScore:
						al = ""
					else:
						al+=candidateIngredient+"="+candidateAllergen+" "
					candidateScore = data[0][1]
					candidateAllergen = data[0][0]
					candidateIngredient = ingredient

		if candidateScore == 0:
			break

		print('ingredient "%s" is candidate for "%s" with score of %d (%s)' % (candidateIngredient, candidateAllergen, candidateScore, str(al)))
		knownIngredients[candidateIngredient] = candidateAllergen
		del ingredientsAllergensCandidates[candidateIngredient]
		for ingredient in ingredientsAllergensCandidates:
			if candidateAllergen in ingredientsAllergensCandidates[ingredient]:
				del ingredientsAllergensCandidates[ingredient][candidateAllergen]

	ingredientsNotContainingAnyAllergen = set()
	ingredientsNotContainingAnyAllergenSum = 0
	for ingredient in ingredientsAllergensCandidates:
		for food in foodsAllergens:
			if ingredient in food:
				ingredientsNotContainingAnyAllergen.add(ingredient)
				ingredientsNotContainingAnyAllergenSum+=1

	print("ingredientsNotContainingAnyAllergen:", ingredientsNotContainingAnyAllergen)
	print("ingredientsNotContainingAnyAllergenSum:", ingredientsNotContainingAnyAllergenSum)
	if assertPart1 != None:
		assert ingredientsNotContainingAnyAllergenSum == assertPart1

	print("knownIngredients:", knownIngredients)

	part2string = ",".join(sorted(knownIngredients, key=knownIngredients.get))
	print("part2 string:", part2string)

	if assertPart2 != None:
		assert part2string == assertPart2
	print()

solve("input/21.input.test", assertPart1=5, assertPart2="mxmxvkd,sqjhc,fvjkl")
solve("input/21.input", assertPart1=1679, assertPart2="lmxt,rggkbpj,mxf,gpxmf,nmtzlj,dlkxsxg,fvqg,dxzq")
print("****** OK *******")
