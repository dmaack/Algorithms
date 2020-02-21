# Write a function power() thar given value a and exponent b will compute a^b
# it would be silly to have the function say return a^b, we wont learn anything

# def power( value, exponent):    
#     # What is 2 ^ 3?
#     # 2 * 2 * 2 = 8

#     Problem 1
#     if exponent == 1:
#         return value
#     Problem 2
#     if exponent == 2:
#         return Problem1Val * value
#     Problem 3
#     if exponent == 4:
#         return Problem2Val * value
#     Problem 4
#     if exponent == 4:
#         return Problem3Val * value   
    
#     # What about negative? x^-n == 1 / x^n
#     if exponent < 0:
#         exponent == -1
#         value = 1 / value
#     # What about fractions?
#     if not exponent.is_integer():
#         print('Sorry this feature is premium')
#         return 
#     # What about zero 

#     if exponent == 0:
#         return 1

#     return value * power(value, exponent - 1)

# print(power(2, -2))
# print(power(2, 6))
# print(power(3, 4))

# prices = [1050, 270, 1540, 3800, 2]

# def find_max_profit(prices):

#   cur_min_price_so_far = prices[0]
#   max_profit_so_far = 0


#   for price in prices:
#     print(price)
#     if price < cur_min_price_so_far:
#       cur_min_price_so_far = price
     

#     profit = price - cur_min_price_so_far
    
    
#     if profit > max_profit_so_far:
#         max_profit_so_far = profit
       

#   return max_profit_so_far

# print(find_max_profit(prices))
# recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
# ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
# # 

# def recipe_batches(recipe, ingredients):
#   number_of_batches = 0
#   can_cook = True
  
#   while can_cook == True:
#     for i in recipe:
#       if i in ingredients.keys():
#         print(f'ingredient key', i)
#         ingredients[i] = ingredients[i] - recipe[i]
#         print(f'ingredient[i] math', ingredients[i])
#         if ingredients[i] < 0:
#           can_cook = False
#           break
#       else:
#         can_cook = False
#         number_of_batches = 0
#         break
        
#     number_of_batches = number_of_batches + 1
#     print(f'number_of_batches before return', number_of_batches)

#   return number_of_batches
  
# recipe_batches(recipe, ingredients)


# def recipe_batches(recipe, ingredients):
#   number_of_batches = 0
  
 
#   # while ingredients >= recipe:
#   for i in recipe:
#     print(i)
#     if i in ingredients.keys():
#       print(i)

# recipe_batches(recipe, ingredients)

# def recipe_batches(recipe, ingredients):
#   total_batches=float("inf")#of complete recipe
#   for i in recipe:
#     print(f'key in recipe', recipe.keys())
#     if i not in ingredients.keys():
#       return 0
#     batches= ingredients[i]//recipe[i]#per ingredient how many batches
#     print(f'batches', ingredients[i], recipe[i])
#     if batches==0:
#        return 0

#     total_batches=min(batches,total_batches)
#     print(f'total batches', batches, total_batches)
#   return total_batches

def rock_paper_scissors(n):
  result = []
  plays = ['rock', 'paper', 'scissors']

  def rps_helper(n, rounds=[]):
    if n == 0:
      return result.append(rounds)
    else:
      for play in plays:
        # rounds = rounds + [play]
        # print(f'rounds', rounds)
        print(f'play', n, play, rounds)
        rps_helper(n - 1, rounds + [play])
  
  rps_helper(n)
  print(f'result', result)
  return result
print(rock_paper_scissors(3))