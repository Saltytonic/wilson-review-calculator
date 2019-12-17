# Summary
Trying to take the information in [this article](https://www.evanmiller.org/how-not-to-sort-by-average-rating.html) and fix it to work for a 5 star rating system. Uses a [binomial proportion confidence interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval), specifically a [Wilson score interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval), to normalize your positive votes propotional to the quantity of votes received. My thoughts are that each rating should have a specific weight and you can take the confidence for each vote quantity to calculate a "true" rating.

There's some mathy stuff I don't understand, so just organizing my thoughts here to look into this later. 

# To Do
- [ ] Add to the review_handler module:
  - [ ] A way to generate a real review-like distrbution. Increased 1 and 5 votes
  - [ ] Different average modes, low, medium, high
  - [ ] Handling of different review files possibly. Maybe make a JSON directory of reviews
- [ ] Actually add the Wilson score interval code
- [ ] Maybe make it run from command line with user input?