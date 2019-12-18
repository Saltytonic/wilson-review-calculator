import review_handler as rh
import math

# Generate a list of reviews between 1 and 5 equal to
# length and store the generated input in "input.txt"
# Can change filename. Writing to file allows custom input
length = 100
#rh.generate(length)

# Get the reviews from the generated file and return
# the content as a list of ints
reviews = rh.get_reviews("input.txt")

# Summing the totals of each score
total_reviews = sum(reviews)
qty_of_each_score = [reviews.count(i) for i in range(1,6)]
z = 1.96 # This gives a confidence of 95%
ci_scores = []
for count in qty_of_each_score:
    if count == 0:
        ci_scores.append(0)
    else:
        phat = 1.0*count/total_reviews
        score = ((phat)+((z**2)/(2*total_reviews))-z*math.sqrt(((phat*(1-phat))+((z**2)/(4*total_reviews)))/total_reviews))/(1 + (z**2/count))
        ci_scores.append(score)
normalizer = 1/sum(ci_scores) + (1-sum(ci_scores))/sum(ci_scores)
normal_scores = []
n = 1
for score in ci_scores:
    normal_scores.append(score*n*normalizer)
    n += 1

print("Normalization value: %.3f\n" % normalizer)
n = 1
for i in qty_of_each_score:
    print("%d-score count: %d" % (n, i))
    n += 1
print("")
n = 1
for i in ci_scores:
    print("%d-score confidence: %.2f%%" % (n, i*100))
    n += 1
print("")
print("Mean average: %.2f" % rh.mean(reviews))
print("Wilson average? %.2f" %sum(normal_scores))


