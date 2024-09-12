# enchance a string. Add data

# % (+, *)
#format()
# f string

# %

# takes a string on the left woth some formattings tags
# takes a group of data on the right, these are usually put in a tuple (,)

# 'some tag' % (data1, data2, data3)
# the number of format tags the left must be equal to the number of data on the right

#tags
# tags are placeholders in your string for data or information
# %s strings
# %d digits
# %g for floats

# sentence: str = "that is 1 hell of a movie."
# customer: str = "i will like to have 4 glasses of wine."
# customer: str = "i will like to have %s glasses of %s"
# customer = template % (4, "wine")
# customer2 = template % (2, "water")
# print(template % (56, "beer"))

# accout_template: str = "Icurrently have a account balance of %f in EUR" %
# user_1: str = account_template % (845.78)
# print(user_1)

# more advansed (additional) tagging
# %[(keyname)][flags][width][.precision] letter(typecode)

# flags is user to test justification (-, +, 0) zero fills

# width give us a total minimum witdth of text

# precision gives specification on the number of digits ofter the decimal point

# wall_street_number: int = 12345
# number_template: str = "integers: ...%d...%-10d....%06d"

# print(number_template % (wall_street_number, wall_street_number, wall_street_number))


# format method

#1. {}
#2. {0} {2} {3}
#3. {named_keywords}

# template: str = "i will like to have a {0} and a plate of {0}"
# my_meal = template.format("salmon",food="salad")
# print(my_meal)


# F strings f""

# meal_name: str = "salad"
# animal_name: str = "salmon"
# my_meal: str = f"i will like to have a {animal_name} and a plate of {meal_name}."
# print(my_meal)

word: str = "cake"
print(word.find("o"))
print("o" in word) # boolean 

if "o" in word:
    print("Found the character")
else:
    print("Can't find the character")
       



