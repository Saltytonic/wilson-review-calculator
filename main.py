import review_handler as rh

# Generate a list of reviews between 1 and 5 equal to
# length and store the generated input in "input.txt"
# Can change filename. Writing to file allows custom input
length = 1
rh.generate(length)

# Get the reviews from the generated file and return
# the content as a list of ints
reviews = rh.get_reviews("input.txt")

qty_of_each_score = [0 for ]

