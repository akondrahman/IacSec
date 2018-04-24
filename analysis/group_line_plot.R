cat("\014") 
options(max.print=1000000)
t1 <- Sys.time()
library(ggplot2)

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_berg/BLOOMBERG.csv"
# THE_LIMIT   <- 30
# THE_DS_NAME <- "BLOOMBERG"

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_cdat/CASKDATA.csv"
# THE_LIMIT   <- 65
# THE_DS_NAME <- "CASKDATA"

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_expr/EXPRESS42.csv"
# THE_LIMIT   <- 75
# THE_DS_NAME <- "EXPRESS42"

### ======================================================================================== ###

# THE_FILE    <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_moz/MOZILLA.csv"
# THE_LIMIT   <- 101
# THE_DS_NAME <- "MOZILLA"

# THE_FILE   <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_ost/OPENSTACK.csv"
# THE_LIMIT  <- 104
# THE_DS_NAME <- "OPENSTACK"

# THE_FILE   <- "/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v6_wik/WIKIMEDIA.csv"
# THE_LIMIT  <- 300
# THE_DS_NAME <- "WIKIMEDIA"

### ======================================================================================== ###

# Y_LABEL     <- "Count of Smells per File"  .... not used 
# Y_LABEL     <- "Smell Density (KLOC)"
# Y_LABEL     <- "Script (%)"

LINE_DATA <- read.csv(THE_FILE)

### remove BASE 64 stuff , if any 
LINE_DATA <- LINE_DATA[!LINE_DATA$TYPE == "BASE_64", ]
### rename binding to INAVLID_IP , this is tricky, so slightly different code 
LINE_DATA$TYPE <- as.character(LINE_DATA$TYPE)
LINE_DATA$TYPE[LINE_DATA$TYPE == "BIND_USAG"] <- "INVALID_IP"
print(tail(LINE_DATA))

## rename the total column name to 'at least one', for RQ2 part 2 only , comment it for smell density 
# LINE_DATA$TYPE <- as.character(LINE_DATA$TYPE)
# LINE_DATA$TYPE[LINE_DATA$TYPE == "TOTAL"] <- "ATLEAST_ONE"
# print(head(LINE_DATA))

#SMELL_DENSITY  ,  CNT_PER_FIL , UNI_FIL_PER

the_plot  <- ggplot(data=LINE_DATA, aes(x=MONTH, y=UNI_FIL_PER, group=1)) + 
  geom_point(size=0.1) + scale_x_discrete(breaks = LINE_DATA$MONTH[seq(1, length(LINE_DATA$MONTH), by = THE_LIMIT)]) + 
  geom_smooth(size=0.5, aes(color=TYPE), method='loess') +   
  facet_grid( . ~ TYPE) +
  labs(x='Month', y=Y_LABEL) +
  theme(legend.position="none") +
  ggtitle(THE_DS_NAME) + theme(plot.title = element_text(hjust = 0.5)) +
  theme(text = element_text(size=11), axis.text.x = element_text(angle=45, hjust=1, size=11), axis.text.y = element_text(size=12.5), axis.title=element_text(size=11, face="bold"))  

the_plot

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))