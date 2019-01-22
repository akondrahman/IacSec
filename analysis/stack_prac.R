t1 <- Sys.time()
cat("\014") 
options(max.print=1000000)

library(ggplot2)
library(ggthemes)
library(extrafont)
library(plyr)
library(scales)


# charts.data <- read.csv("test_stack.csv")
# 
# charts.data <- ddply(charts.data, .(year), transform, pos = cumsum(percentage) - (0.5 * percentage))
# 
# 
# the_plot <- ggplot() + geom_bar(aes(y = percentage, x = year, fill = product), data = charts.data, stat="identity")
# 
# color_fill <- c("#5F9EA0", "#E1B378")
# the_plot <- the_plot + scale_fill_manual(values = color_fill)

#HTTP_USAG", "INVALID_IP", "WEAK_CRYP", "SUSP_COMM", "TOTAL

# dat <- read.table(text = "    DFLT_ADMN EMPT_PASS HARD_CODE_SECR HTTP_USG INVA_IP SUSP_COMM WEAK_CRYP
# Agree       1 2 6 8 3 2 3
# Disagree    1 1 2 1 1 1 0
# NoResponse  1 1 2 0 2 2 1", sep = "", header = TRUE)

dat <- read.table(text = "DFLT.ADMN_9 EMPT.PASS_7 HARD.CODE.SECR_60 HTTP.USG_93 INVA.IP_15 SUSP.COMM_15 WEAK.CRYP_13
Agree       5 4 41 72 11  4 11
Disagree    4 3 19 21  4 11  2", sep = "", header = TRUE)

#Add an id variable for the filled regions
library(reshape2)
library(scales)
datm <- melt(cbind(dat, ind = rownames(dat)), id.vars = c('ind'))

#datm <- datm[order(datm[, 1], decreasing=TRUE), ] 

print(head(datm))

pdf('/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/writing/fig-res-feedback-r.pdf', width=6, height=2.5)


the_plot <- ggplot(datm, aes(x = variable, y = value, fill = ind)) + geom_bar(position = "fill", stat = "identity", width = 0.35) 
the_plot <- the_plot + scale_y_continuous(labels = percent_format()) 
the_plot <- the_plot + theme(legend.title = element_blank(), 
                             text = element_text(size=10), 
                             axis.title.x = element_text(face='bold'), 
                             axis.title.y = element_text(face='bold'), 
                             legend.position="top", 
                             legend.direction="horizontal") 

#the_plot <- the_plot + scale_fill_discrete(guide = guide_legend(reverse=TRUE))
the_plot <- the_plot + labs(x="Security Smell", y="Percentage") 
the_plot <- the_plot + coord_flip() 
the_plot <- the_plot + scale_fill_manual(breaks = c( "Disagree", "Agree"),  values=c("green", "red"))


the_plot

dev.off()

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))