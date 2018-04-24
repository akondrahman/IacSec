cat("\014") 
options(max.print=1000000)
library(ggplot2)
t1 <- Sys.time()

# BAR_FIL <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_berg/LIFETIME.csv"
# BAR_DAT <- read.csv(BAR_FIL)
# BAR_TIT <- "BLOOMBERG"
# BAR_LIM <- c(0, 40)
# BAR_COL <- 8
# BAR_BIN <- 20

# BAR_FIL <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_cdat/LIFETIME.csv"
# BAR_DAT <- read.csv(BAR_FIL)
# BAR_TIT <- "CASKDATA"
# BAR_LIM <- c(0, 25)
# BAR_COL <- 8
# BAR_BIN <- 20

# BAR_FIL <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_expr/LIFETIME.csv"
# BAR_DAT <- read.csv(BAR_FIL)
# BAR_TIT <- "EXPRESS"
# BAR_LIM <- c(0, 10)
# BAR_COL <- 8
# BAR_BIN <- 10

### ======================================================================================== ###

# BAR_FIL <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_new_old_moz/LIFETIME.csv"
# BAR_DAT <- read.csv(BAR_FIL)
# BAR_TIT <- "MOZILLA"
# BAR_LIM <- c(0, 40)
# BAR_COL <- 8
# BAR_BIN <- 20

# BAR_FIL <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_new_old_ost/LIFETIME.csv"
# BAR_DAT <- read.csv(BAR_FIL)
# BAR_TIT <- "OPENSTACK"
# BAR_LIM <- c(0, 500)
# BAR_COL <- 8
# BAR_BIN <- 30

# BAR_FIL <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_new_old_wik/LIFETIME.csv"
# BAR_DAT <- read.csv(BAR_FIL)
# BAR_TIT <- "WIKIMEDIA"
# BAR_LIM <- c(0, 50)
# BAR_COL <- 8
# BAR_BIN <- 25

### ======================================================================================== ###

### remove BASE 64 stuff , if any 
BAR_DAT <- BAR_DAT[!BAR_DAT$SMELL == "BASE_64", ]

### same file , one occurence, if all occurences for the same file is considered then ti systematically overshoots 
BAR_DAT  <- BAR_DAT[!duplicated(BAR_DAT), ]

BAR_DAT$SMELL <- as.character(BAR_DAT$SMELL)
BAR_DAT$SMELL[BAR_DAT$SMELL == "BIND_USAG"] <- "INVALID_IP"
print(tail(BAR_DAT))

the_plot <- ggplot(BAR_DAT, aes(x = DUR_MON)) + geom_histogram(fill='#CC79A7', color = "black", bins=BAR_BIN, stat='bin')  + labs(x='Lifetime (Months)', y = 'Count of Smells')
the_plot <- the_plot + ggtitle(BAR_TIT)  + theme(plot.title = element_text(hjust = 0.5), text = element_text(size=12.5), axis.text=element_text(size=12.5))
the_plot <- the_plot + scale_y_continuous(limits=BAR_LIM) + theme(legend.position="none") 
the_plot <- the_plot + facet_wrap(~ SMELL, ncol=BAR_COL)

the_plot

print("============================================================")

### for hard coded stats 
# HARD_CODE_INDE <- BAR_DAT$SMELL=='HARD_CODE_SECR'
# HARD_CODE_DATA <- BAR_DAT[HARD_CODE_INDE, ]
# print(summary(HARD_CODE_DATA$DUR_MON))
# print(table(HARD_CODE_DATA$DUR_MON))

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))