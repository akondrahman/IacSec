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

the_plot <- ggplot(BOXPLOT_DATA, aes(x=SMELL, y=DUR_MON, fill=SMELL)) + geom_boxplot(width=0.5, outlier.shape=16, outlier.size=1) + labs(x='Name', y='Lifetime (Months)') 
the_plot <- the_plot + ggtitle(BOXPLOT_TITL)  + theme(plot.title = element_text(hjust = 0.5), text = element_text(size=12.5), axis.text=element_text(size=12.5))
the_plot <- the_plot + scale_y_continuous(limits=BOXPLOT_LIMI) + theme(legend.position="none")
the_plot <- the_plot +  stat_summary(fun.y=mean, geom="point", colour="black", shape=13, size=1) 

the_plot

print("============================================================")

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))