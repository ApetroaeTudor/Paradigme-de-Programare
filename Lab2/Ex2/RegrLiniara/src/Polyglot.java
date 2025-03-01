import org.graalvm.polyglot.*;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Polyglot {

    public static String ReadFileLine(String filePath, int nrLine){
       String line=new String();


       try {
           BufferedReader br = new BufferedReader(new FileReader(filePath));
           while( (line=br.readLine())!=null && nrLine!=0){
               nrLine--;
           }
       }
       catch(Exception e){
           System.err.println("Error " + e.getMessage());
       }
       return line;
    }

    public static ArrayList<Integer> ParseLine(String line){
        ArrayList<Integer> arr=new ArrayList<>();

        String[] stringArr=line.split(" ");
        for(String s:stringArr){
            arr.add(Integer.parseInt(s));
        }

        return arr;
    }

    public static void R_RegresieLiniara(String filePath, String CuloarePct, String CuloareLinie, String NumeImagine, String Path ) {
        ArrayList<Integer> XLINE=ParseLine(ReadFileLine(filePath,0));
        ArrayList<Integer> YLINE=ParseLine(ReadFileLine(filePath,1));

        Context polyglot=Context.newBuilder().allowAllAccess(true).build();
        String SaveImg=Path+"/"+NumeImagine+".png";
        try {
            BufferedWriter bw = new BufferedWriter(new FileWriter("./intermediary.txt"));
            bw.write("");
            for(int i=0;i<XLINE.size();i++){
                bw.append(XLINE.get(i).toString());
                bw.append(' ');
            }
            bw.append("\n");
            for(int i=0;i<YLINE.size();i++){
                bw.append(YLINE.get(i).toString());
                bw.append(' ');
            }
            bw.append("\n");
            bw.append(CuloarePct).append("\n");
            bw.append(CuloareLinie).append("\n");


            bw.append(SaveImg).append("\n");

            bw.close();
        }
        catch(Exception e){
            System.err.println("Error: "+e.getMessage());
        }


        polyglot.eval("R","system('Rscript ./src/rubyscript.R')");
        String syscommand="system('xdg-open " +SaveImg+" ')";
        polyglot.eval("R",syscommand);

        polyglot.close();


    }

    public static void main(String[] args) {
        String filePath="./dataset.txt";


        Scanner myScanner=new Scanner(System.in);

        String plotColorPuncte=new String();
        System.out.println("Se citeste culoarea de plot pentru punctele de date: ");
        plotColorPuncte=myScanner.nextLine();

        String plotColorLinieRegresie=new String();
        System.out.println("Se citeste culoarea de plot pentru linia de regresie: ");
        plotColorLinieRegresie=myScanner.nextLine();

        String numeImagineSalvata=new String();
        System.out.println("Se citeste numele imaginii ce va fi salvate: ");
        numeImagineSalvata=myScanner.nextLine();

        String pathImagineSalvata=new String();
        System.out.println("Se citeste calea imaginii ce va fi salvate: ");
        pathImagineSalvata=myScanner.nextLine();


        R_RegresieLiniara(filePath,plotColorPuncte,plotColorLinieRegresie,numeImagineSalvata,pathImagineSalvata);


        myScanner.close();

    }
}