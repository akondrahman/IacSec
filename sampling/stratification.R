cat("\014") 
library(SDaA)
options(max.print=1000000)
t1 <- Sys.time()

############################################################
###################### DO NOT CHNAGE THIS. SOURCE: https://gist.github.com/mrdwab/6424112 

stratified <- function(df, group, size, select = NULL, 
                       replace = FALSE, bothSets = FALSE) {
  if (is.null(select)) {
    df <- df
  } else {
    if (is.null(names(select))) stop("'select' must be a named list")
    if (!all(names(select) %in% names(df)))
      stop("Please verify your 'select' argument")
    temp <- sapply(names(select),
                   function(x) df[[x]] %in% select[[x]])
    df <- df[rowSums(temp) == length(select), ]
  }
  df.interaction <- interaction(df[group], drop = TRUE)
  df.table <- table(df.interaction)
  df.split <- split(df, df.interaction)
  if (length(size) > 1) {
    if (length(size) != length(df.split))
      stop("Number of groups is ", length(df.split),
           " but number of sizes supplied is ", length(size))
    if (is.null(names(size))) {
      n <- setNames(size, names(df.split))
      message(sQuote("size"), " vector entered as:\n\nsize = structure(c(",
              paste(n, collapse = ", "), "),\n.Names = c(",
              paste(shQuote(names(n)), collapse = ", "), ")) \n\n")
    } else {
      ifelse(all(names(size) %in% names(df.split)),
             n <- size[names(df.split)],
             stop("Named vector supplied with names ",
                  paste(names(size), collapse = ", "),
                  "\n but the names for the group levels are ",
                  paste(names(df.split), collapse = ", ")))
    }
  } else if (size < 1) {
    n <- round(df.table * size, digits = 0)
  } else if (size >= 1) {
    if (all(df.table >= size) || isTRUE(replace)) {
      n <- setNames(rep(size, length.out = length(df.split)),
                    names(df.split))
    } else {
      message(
        "Some groups\n---",
        paste(names(df.table[df.table < size]), collapse = ", "),
        "---\ncontain fewer observations",
        " than desired number of samples.\n",
        "All observations have been returned from those groups.")
      n <- c(sapply(df.table[df.table >= size], function(x) x = size),
             df.table[df.table < size])
    }
  }
  temp <- lapply(
    names(df.split),
    function(x) df.split[[x]][sample(df.table[x],
                                     n[x], replace = replace), ])
  set1 <- do.call("rbind", temp)
  
  if (isTRUE(bothSets)) {
    set2 <- df[!rownames(df) %in% rownames(set1), ]
    list(SET1 = set1, SET2 = set2)
  } else {
    set1
  }
}

######################
############################################################

#######################MY CODE ############################
set.seed(1)
# data_to_sample <- read.csv("test.csv")

# data_to_sample <- read.csv("WIKI.csv")
# out_file       <- "STRATIFIED_WIKI.csv"

# data_to_sample <- read.csv("OSTK.csv")
# out_file       <- "STRATIFIED_OSTK.csv"

# data_to_sample <- read.csv("MOZI.csv")
# out_file       <- "STRATIFIED_MOZI.csv"

# data_to_sample <- read.csv("EXPR.csv")
# out_file       <- "STRATIFIED_EXPR.csv"

# data_to_sample <- read.csv("CLCR.csv")
# out_file       <- "STRATIFIED_CLCR.csv"

# data_to_sample <- read.csv("CDAT.csv")
# out_file       <- "STRATIFIED_CDAT.csv"

# data_to_sample <- read.csv("BERG.csv")
# out_file       <- "STRATIFIED_BERG.csv"

print("===============HEAD=============")
head(data_to_sample) 
print("================================")
print("===============SUMMARY=============")
summary(data_to_sample)
print("================================")
print("===============RESULTS=============")
# out_df <- stratified(data_to_sample, "MONTH", 0.0025)  # 0.0025 means 0.25%, used for Puppet 
out_df <- stratified(data_to_sample, "MONTH", 0.01)  # 0.01 means 1%, used for Chef 
print(head(out_df))
write.csv(out_df, file = out_file, row.names=FALSE)
print("================================")
t2 <- Sys.time()
print(t2 - t1)  # 
rm(list = setdiff(ls(), lsf.str()))