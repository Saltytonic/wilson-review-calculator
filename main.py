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

non_zero_values = 0.0
for score in ci_scores:
    if score != 0:
        non_zero_values += 1

score_normalizer = []
for score in ci_scores:
    if score == 0:
        score_normalizer.append(0)
    else:
        expected = 1/non_zero_values
        score_normalizer.append(score/expected)

normalizer = 1/sum(ci_scores)
#normalizer = -2.1638*(sum(ci_scores)**4) + 5.5309*(sum(ci_scores)**3) - 5.0173*(sum(ci_scores)**2) + 2.0072*sum(ci_scores) + 0.6347

normal_scores = []
for i in range(0,len(ci_scores)):
    normal_scores.append(score*(i+1)*score_normalizer[i])

print("Global normalization value: %.3f" % normalizer)
print("Non-zero scores: %d\n" % non_zero_values)
n = 1
for i in score_normalizer:
    print("%d-score normal: %.3f" % (n, i))
    n += 1
print("")
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


