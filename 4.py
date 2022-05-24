'''
potential_number_of_candies = 8
while potential_number_of_candies < 200 :
    potential_number_of_candies +=1
    if ((potential_number_of_candies % 5 == 2) and (potential_number_of_candies % 6 == 3) and (potential_number_of_candies % 7 == 2)): number_of_candies = potential_number_of_candies
print('The number of candies in the box is ', number_of_candies)
'''

potential_number_of_candies = 8
while ((potential_number_of_candies % 5 != 2) or (potential_number_of_candies % 6 != 3) or (potential_number_of_candies % 7 != 2)):
    potential_number_of_candies +=1
print('The number of candies in the box is ', potential_number_of_candies)