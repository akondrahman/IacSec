t1 <- Sys.time()
cat("\014") 
options(max.print=1000000)
# import likert package
require(likert)

# I want to send output to PDF; uncomment nex line if you're working with TikZ
#pdf("liket.bar.plot.dat")
#
dataset <- read.csv("test_stack.csv", header=TRUE, sep=",")

#colnames(dataset)[which(names(dataset)=="It.helps.me.be.more.effective")] <- "Helps me be more effective"
#colnames(dataset)[which(names(dataset)=="It.feels.unnecessary.to.use.the.system")] <- "Feels unnecessary to use system"

# create colored plot
plotlevels <- c('Agree', 'Disagree')

tryCatch({
  lbad <- likert(dataset)
}, error=function(e) {
  print("This is good that an error was thrown!")
  print(e)
})

sapply(dataset, class)
sapply(dataset, function(x) { length(levels(x)) } )

for(i in seq_along(dataset)) {
  dataset[,i] <- factor(dataset[,i], levels=plotlevels)
}

experimentdataset <- likert(dataset)

likert.bar.plot(experimentdataset, plot.percent.high=FALSE, plot.percent.low=FALSE,plot.percent.neutral=FALSE) +
  theme_gray() +
  theme(legend.title=element_blank(),
        legend.position="bottom",
        legend.text=element_text(size=8),
        legend.key.height=unit(0.15,"cm"),
        plot.margin=unit(c(0.1,0.1,0,0),"cm"),
        strip.text = element_text(size=8),
        axis.title.x = element_text(vjust=-0.8,size=8),
        axis.title.y = element_text(vjust=-0.2,size=8),
        axis.text = element_text(size=8),
        #plot.text = element_text(size=8),
        axis.text.x = element_text(angle=0,vjust=0.5)) 