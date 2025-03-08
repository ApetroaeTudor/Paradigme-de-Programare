import static java.awt.image.BufferedImage.TYPE_INT_RGB;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.Value;

public class RHistogram {
    //dimensiunea suprafetei in care plotam
    private static final int WIDTH = 1000;
    private static final int HEIGHT = 500;

    public static <E> void WriteImage(Value showPlot, String fname, E[] values){
        //construim o imagine in care vom plota graficul
        BufferedImage image = new BufferedImage(WIDTH, HEIGHT, TYPE_INT_RGB);
        Graphics2D graphics = (Graphics2D) image.getGraphics();
        graphics.setBackground(new Color(255, 255, 255));
        graphics.clearRect(0, 0, WIDTH, HEIGHT);
        //executam functia R, evaluata in showPlot, cu parametrii corecti pentru grafic
        //si array-ul values primit ca parametru in aceasta metoda Java, din Kotlin
        showPlot.execute(graphics, WIDTH, HEIGHT, values);

        //construim fisierul PNG folosind numele dat ca parametru
        try {
            ImageIO.write(image, "png", new File(fname+ ".png"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("SUCCESS : [" + fname + "]");
    }

    //functia care construieste graficul, primeste 2 parametri, un array de cuvinte si un nume de
    //fisier in care scriem imaginea
    public static<E> void BuildHistogram(E[] values, String fname, boolean how) {
        //construim un context Polyglot pentru R
        Context context = Context.newBuilder("R").allowAllAccess(true).build();
        String src;
        if (how) {
            src =
                    "library(lattice); " +                  //GraalVM stie sa foloseasca momentan libraria lattice si grid pentru plotare
                            "function(g, w, h, data) { " +  //functia R primeste 4 parametri : suprafata grafica din java, Width, Height si array-ul de cuvinte
                            "   grDevices:::awt(w,h,g);" +  //folosim Java awt pentru afisare
                            "   B <- c(data);" +            //construim un array R dintr-un array Java
                            "   tab <- table(B);" +         //convertim la table, array-ul B. Operatia va produce o histograma cu perechi val_unica -> frecventa
                            "   print(barchart(tab));" +    //afisam histograma folosind functia barchart(), mai corect ar fi fost barplot() insa nu functioneaza momentan
                            "   dev.off();" +               //inchidem suprafata
                            "}";
        }else{
            src =
                    "library(lattice); " +                  //GraalVM stie sa foloseasca momentan libraria lattice si grid pentru plotare
                            "function(g, w, h, data) { " +  //functia R primeste 4 parametri : suprafata grafica din java, Width, Height si array-ul de cuvinte
                            "   grDevices:::awt(w,h,g);" +  //folosim Java awt pentru afisare
                            "   B <- c(data);" +            //construim un array R dintr-un array Java
                            "   x <- 0:(length(B) - 1);" +  //construim elementele pe axa X
                            "   print(xyplot(B ~ x));" +    //afisam histograma folosind functia barchart(), mai corect ar fi fost barplot() insa nu functioneaza momentan
                            "   dev.off();" +               //inchidem suprafata
                            "}";
        }
        //evaluam functia R
        Value showPlot = context.eval("R", src);

        WriteImage(showPlot, fname, values);
    }
}
