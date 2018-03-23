cat("\014") 
options(max.print=1000000)
library(ggplot2)
t1 <- Sys.time()

# reff: https://rpubs.com/tgjohnst/cumulative_plotting

#head(EuStockMarkets)
lol <- read.csv('/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/lol.csv')

# plot(ecdf(lol$count))


ggplot(lol, aes(density)) + stat_ecdf(geom = "step")

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))