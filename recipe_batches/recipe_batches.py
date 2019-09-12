#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

    #check if keys are in both recipe and ingredients
    #diff is a list of keys that are not in both arrays
    diff = set(recipe) - set(ingredients)

    #if a key is missing from one of the dictionaries, return 0
    if len(diff) > 0:
        return 0

    #maximum number of batches from current ingredients vs recipe
    max_batches = None
    #loop through recipe
    for key in recipe:

        #amount of ingredients per key in recipe
        recipe_ingredient_count = recipe[key]
        #amount of ingredients per key in ingredients
        ingredient_count = ingredients[key]

        #number of batches current ingredient is able to make
        batches_from_ingredient = int(ingredient_count / recipe_ingredient_count)

        if not max_batches:
            max_batches = batches_from_ingredient
        elif batches_from_ingredient < max_batches:
            max_batches = batches_from_ingredient

    return max_batches



if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
