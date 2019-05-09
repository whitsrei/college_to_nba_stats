Goal
To predict ppg for player in the first round of the draft. 

Currently we have the data that we are running the classifier on in firstRoundPicks_withCollegeStats.csv. This dataset is where we draw all of our conclusions from. 

First we did explotarory data analysis and looked at the 27 different attribute we had to choose from. We chose to go with ones that we saw as indicators towards how players perform in the NBA. Once we cleaned the data we used sci-kit learn to explore some the data set and get the classifier that works best. We found that KNN works best and therefore looked to compare our home made model vs the sci-kit learn model. 

We print our the total error points over the data sets which allows for users to see which performs best.

At the end we printed our the correlation coefficients for the attributes.

Near of the end of the notebook we have predictions for a few players who are supposed to be in the first round this year.
