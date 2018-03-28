cat("\014") 
options(max.print=1000000)
library(ggplot2)
t1 <- Sys.time()

# reff: https://rpubs.com/tgjohnst/cumulative_plotting

# CDF_DAT <- read.csv('/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_moz/LIFETIME.csv')
# CDF_TIT <- 'MOZILLA'
# CDF_COL <- 8

# CDF_DAT <- read.csv('/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_ost/LIFETIME.csv')
# CDF_TIT <- 'OPENSTACK'
# CDF_COL <- 8

# CDF_DAT <- read.csv('/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/plots_v4_new_old_wik/LIFETIME.csv')
# CDF_TIT <- 'WIKIMEDIA'
# CDF_COL <- 8

cdf_plt <- ggplot(CDF_DAT, aes(DUR_MON, fill=SMELL)) + stat_ecdf(geom = "step") + facet_wrap(~ SMELL, , ncol=CDF_COL) + labs(x='Lifetime(Months)', y='Cumulative Distribution Function (CDF)')
cdf_plt <- cdf_plt + ggtitle(CDF_TIT)  + theme(plot.title = element_text(hjust = 0.5), text = element_text(size=12.5), axis.text=element_text(size=12.5))
cdf_plt <- cdf_plt + theme(legend.position="none")

cdf_plt 

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))