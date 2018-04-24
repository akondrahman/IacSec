cat("\014") 
options(max.print=1000000)
library(ggplot2)
t1 <- Sys.time()

# BOXPLOT_FILE <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_berg/LIFETIME.csv"
# BOXPLOT_DATA <- read.csv(BOXPLOT_FILE)
# BOXPLOT_TITL <- "BLOOMBERG"
# BOXPLOT_LIMI <- c(0, 50)

# BOXPLOT_FILE <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_cdat/LIFETIME.csv"
# BOXPLOT_DATA <- read.csv(BOXPLOT_FILE)
# BOXPLOT_TITL <- "CASKDATA"
# BOXPLOT_LIMI <- c(0, 40)

# BOXPLOT_FILE <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_expr/LIFETIME.csv"
# BOXPLOT_DATA <- read.csv(BOXPLOT_FILE)
# BOXPLOT_TITL <- "EXPRESS42"
# BOXPLOT_LIMI <- c(0, 60)

### ======================================================================================== ###

# BOXPLOT_FILE <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_new_old_moz/LIFETIME.csv"
# BOXPLOT_DATA <- read.csv(BOXPLOT_FILE)
# BOXPLOT_TITL <- "MOZILLA"
# BOXPLOT_LIMI <- c(0, 70)

# BOXPLOT_FILE <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_new_old_ost/LIFETIME.csv"
# BOXPLOT_DATA <- read.csv(BOXPLOT_FILE)
# BOXPLOT_TITL <- "OPENSTACK"
# BOXPLOT_LIMI <- c(0, 75)

# BOXPLOT_FILE <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_new_old_wik/LIFETIME.csv"
# BOXPLOT_DATA <- read.csv(BOXPLOT_FILE)
# BOXPLOT_TITL <- "WIKIMEDIA"
# BOXPLOT_LIMI <- c(0, 105)

### ======================================================================================== ###

### remove BASE 64 stuff , if any 
BOXPLOT_DATA <- BOXPLOT_DATA[!BOXPLOT_DATA$SMELL == "BASE_64", ]

### same file , one occurence, if all occurences for the same file is considered then it systematically overshoots 
BOXPLOT_DATA <- BOXPLOT_DATA[!duplicated(BOXPLOT_DATA), ]

BOXPLOT_DATA$SMELL <- as.character(BOXPLOT_DATA$SMELL)
BOXPLOT_DATA$SMELL[BOXPLOT_DATA$SMELL == "BIND_USAG"] <- "INVALID_IP"
print(tail(BOXPLOT_DATA))

the_plot <- ggplot(BOXPLOT_DATA, aes(x=SMELL, y=DUR_MON, fill=SMELL)) + geom_boxplot(width=0.35, outlier.shape=16, outlier.size=1) + labs(y='Lifetime (Months)') 
the_plot <- the_plot + ggtitle(BOXPLOT_TITL)  + theme(plot.title = element_text(hjust = 0.5), axis.text.y=element_text(size=12), axis.text.x =element_text(size=12))
the_plot <- the_plot + scale_y_continuous(limits=BOXPLOT_LIMI) + theme(legend.position="none")
the_plot <- the_plot + stat_summary(fun.y=mean, geom="point", colour="black", shape=13, size=1) 
the_plot <- the_plot + coord_flip() + theme(axis.title.y = element_blank())

the_plot

print("============================================================")

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))