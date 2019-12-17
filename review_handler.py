import random

def generate(qty: int, filename: str = "input.txt"):
    min_scale, max_scale = 1, 5

    random.seed()

    review_list = [random.randint(min_scale, max_scale) for i in range(0, qty)]

    with open(filename, "w") as fo:
        fo.writelines("%s\n" % str(review) for review in review_list)

def get_reviews(filename: str) -> list:
    output = []
    with open(filename, "r") as fo:
        temp = fo.read().splitlines()
        output = [int(i) for i in temp]
    return output

def mean(review_list: list) -> float:
    return sum(review_list) / len(review_list)

    
