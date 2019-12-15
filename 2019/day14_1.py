fname = 'day14.txt'
fname = 'day14example1.txt'
fname = 'day14example2.txt'
fname = 'day14example3.txt'
fname = 'day14example4.txt'
fname = 'day14example5.txt'

with open(fname) as f:
    reactions = [s.strip() for s in f]

recipes = {}
for reaction in reactions:
    in_string, _, out_string = reaction.partition(' => ')
    ingredients = [x.split() for x in in_string.split(', ')]
    ingredients = tuple((ingredient[1], int(ingredient[0])) for ingredient in ingredients)
    out_amount_string, out_chemical = out_string.split()
    recipes[out_chemical] = (int(out_amount_string), ingredients)

import pprint; pp = pprint.PrettyPrinter(indent=4)
pp.pprint(recipes)

required = [*recipes['FUEL'][1]]
print(required)
while any([recipes[chem][1][0][0] != "ORE" for chem, amount in required]):
    new = []
    for chem, required_amount in required:
        recipe_amount, ingredients = recipes[chem]
        if len(ingredients) == 1 and ingredients[0][0] == "ORE":
            new.append((chem, required_amount))
            continue
        # mul = required_amount / recipe_amount
        q, r = required_amount // recipe_amount, required_amount % recipe_amount
        mul = q if r == 0 else q + 1
        for n, a in ingredients:
            new.append((n, mul * a))
    required = new
    pp.pprint(required)

total = {}
for chem, amount in required:
    if chem in total:
        total[chem] += amount
    else:
        total[chem] = amount

total_ore = 0
for chem in total:
    q, r = total[chem] // recipes[chem][0], total[chem] % recipes[chem][0]
    mul = q if r == 0 else q + 1
    total_ore += recipes[chem][1][0][1] * mul

print(total)
print(total_ore)

# counting too much due to lines 32,33 - just start from scratch using objects
# so clearer whats happening, keep list of surplus so dont over count