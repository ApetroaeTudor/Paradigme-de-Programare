library(lattice)

                XLINE <- c(1,2,3,4,5,6,7,8,9,10)
                YLINE <- c(50,55,65,70,75,78,85,88,90,95)
                dataFrame <- data.frame(X=XLINE,Y=YLINE)
                model <- lm(Y ~ X, data=dataFrame)
                ImgPathAndName <- "/home/tudor/AN2/PP/LaboratoarePP/pp-1211b-homeworks-ApetroaeTudor/Lab2/Ex2/RegrLiniara/IMGG.png"
                PctColor <-"red"
                LineColor <- "blue"
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