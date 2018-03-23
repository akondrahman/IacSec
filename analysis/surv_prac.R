cat("\014") 
options(max.print=1000000)
library(survival)
library(dplyr)
library(OIsurv) 
library(ranger)
library(ggplot2)
t1 <- Sys.time()

data(bmt)

# reff: https://en.wikipedia.org/wiki/Survival_analysis
# reff: https://en.wikipedia.org/wiki/Kaplan%E2%80%93Meier_estimator
# reff: https://www.r-bloggers.com/survival-analysis-with-r/ 

# Prepare new data frame for modeling

head(bmt)

y_bmt <- Surv(bmt$t1, bmt$d1)
y_bmt



# Kaplan Meier Survival Curve
# y_bmt <- Surv(bmt$t1, bmt$d1), d1 is a factor , and must be a factor 

y_bmt

fit1_bmt <- survfit(y_bmt ~ 1)
summary(fit1_bmt)


t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))