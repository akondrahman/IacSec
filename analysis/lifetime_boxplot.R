cat("\014") 
options(max.print=1000000)
library(ggplot2)
t1 <- Sys.time()

BOXPLOT_FILE <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_new_old_berg/LIFETIME.csv"
BOXPLOT_DATA <- read.csv(BOXPLOT_FILE)

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))