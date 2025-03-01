library(lattice)
XLINE  <- readLines("./intermediary.txt",n=1)
YLINE  <- readLines("./intermediary.txt",n=2)[2]
XLINE  <- as.integer(unlist(strsplit(XLINE, " ")))
YLINE  <- as.integer(unlist(strsplit(YLINE, " ")))


dataFrame <- data.frame(X=XLINE,Y=YLINE)
model <- lm(Y ~ X, data=dataFrame)

PctColor <- readLines("./intermediary.txt",n=3)[3]
LineColor <- readLines("./intermediary.txt",n=4)[4]
ImgPathAndName <- readLines("./intermediary.txt",n=5)[5]

png(ImgPathAndName, width = 800, height = 600)
xyplot(Y ~ X, data = dataFrame,
       main = "Regresie liniara cu lattice",
       xlab = "XLINE",
       ylab = "YLINE",
       panel = function(x, y, ...) {
       panel.xyplot(x, y, col = PctColor, pch = 19, ...)
       panel.abline(model, col = LineColor, lwd = 2)
       })
dev.off(); print("DONE")