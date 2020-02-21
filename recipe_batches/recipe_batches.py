#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  number_of_batches = -1
  can_cook = True
  
  while can_cook == True:
    for i in recipe:
      if i in ingredients.keys():
        ingredients[i] = ingredients[i] - recipe[i]
        if ingredients[i] < 0:
          can_cook = False
          break
      else:
        can_cook = False
        number_of_batches = -1
        break
        
    number_of_batches = number_of_batches + 1

  return number_of_batches
    





if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))