t1 <- Sys.time()
cat("\014") 
options(max.print=1000000)


library(reshape2)
library(ggplot2)


yes_vec     <- c(7.70, 36.55, 6.45, 17.02, 2.33, 10.03, 1.97, 9.49)
no_vec      <- c(7.70, 36.55, 6.45, 17.02, 2.33, 10.03, 1.97, 9.49)
unknown_vec <- c(7.70, 36.55, 6.45, 17.02, 2.33, 10.03, 1.97, 9.49)

df     <- data.frame(Smell = c("DFLT_ADMN(10)", "EMPT_PASS", "HARD_CODE_SECR", "HTTP_USAG", "INVALID_IP", "WEAK_CRYP", "SUSP_COMM", "TOTAL"),  Agreed = yes_vec, Disagreed = 
                       no_vec,  Unknown = unknown_vec)
value_name <- "Percentage" 

data.m <- melt(df, id.vars='Smell', value.name = value_name )
data.m

pdf('/Users/akond/Documents/AkondOneDrive/OneDrive/SecurityInIaC/output/fig-res-feedback.pdf', width=6, height=2.5)

the_plot <- ggplot(data.m, aes(Smell, Percentage))     ### need to change this based on y-axis variable 
the_plot <- the_plot + geom_bar(aes(x = factor(Smell, levels=unique(Smell)), fill = variable), width = 0.4, position = position_dodge(width=0.5), 
stat="identity") 
the_plot <- the_plot + theme(legend.title = element_blank(), text = element_text(size=11), axis.title.x = element_text(face='bold'), axis.title.y = 
element_text(face='bold')) 
the_plot <- the_plot + theme(text = element_text(size=11), axis.text.x = element_text(angle=45, hjust=1), plot.title = element_text(hjust = 0.5), legend.position="top") +
            ylim(c(0, 100)) 
the_plot 

dev.off()

t2 <- Sys.time()
print(t2 - t1)  
rm(list = setdiff(ls(), lsf.str()))
