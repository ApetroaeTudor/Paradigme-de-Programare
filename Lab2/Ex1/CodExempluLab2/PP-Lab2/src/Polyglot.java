//import libraria principala polyglot din graalvm
import org.graalvm.polyglot.*;


import java.util.Hashtable;
import java.util.Scanner;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

//clasa principala - aplicatie JAVA

class Polyglot {
    //metoda privata pentru conversie low-case -> up-case folosind functia toupper() din R
    private static String RToUpper(String token){
        //construim un context care ne permite sa folosim elemente din R
        Context polyglot = Context.newBuilder().allowAllAccess(true).build();
        //folosim o variabila generica care va captura rezultatul excutiei funcitiei R, toupper(String)
        //pentru aexecuta instructiunea I din limbajul X, folosim functia graalvm polyglot.eval("X", "I");
        Value result = polyglot.eval("R", " toupper(\""+token+"\"); ");
        //utilizam metoda asString() din variabila incarcata cu output-ul executiei pentru a mapa valoarea generica la un String
        String resultString = result.asString();
        // inchidem contextul Polyglot
        polyglot.close();

        return resultString;
    }

    //metoda privata pentru evaluarea unei sume de control simple a literelor unui text ASCII, folosind PYTHON
    private static int SumCRC(String token){
        //construim un context care ne permite sa folosim elemente din PYTHON
        Context polyglot = Context.newBuilder().allowAllAccess(true).option("python.ForceImportSite","true").build();
        //folosim o variabila generica care va captura rezultatul excutiei functiei PYTHON, sum()
        //avem voie sa inlocuim anumite elemente din scriptul pe care il construim spre evaluare, aici token provine din JAVA, dar va fi interpretat de PYTHON
        String pyCode="import numpy as np\n"+
                    "coef = [2,1]\n"+
      //              "print('" + token + "')\n"+
                    "Str='"+token+"'\n"+
                    "SliceObj=slice(1,len(Str)-1)\n"+
                    "Str=Str[SliceObj]\n"+
                    "print(Str)\n"+
                    "S=sum(ord(ch) for ch in Str)\n"+
                    "S=S%25\n"+
                    "S";
        Value val= polyglot.eval("python", pyCode);
        int resultInt=val.asInt();

        //utilizam metoda asInt() din variabila incarcata cu output-ul executiei, pentru a mapa valoarea generica la un Int

        //int resultInt = result.asInt();

        // inchidem contextul Polyglot
        polyglot.close();


        //"Sum = sum(ord(ch) for ch in '\" + token + \"')\n"+
        //        "int(np.polyval(coef,Sum))";

        return resultInt;
    }

    private static void LabEx3(){

        Context polyglot= Context.newBuilder().allowAllAccess(true).option("python.ForceImportSite","true").build();
        String pyCode="from random import randint\n" +
                    "List=list()\n"+
                    "for i in range(20):\n"+
                    "\tx=randint(0,100)\n"+
                    "\tList.insert(0,x)\n"+
                    "List";

        String jsCode="console.log(javaListImported)";

        String rCode="SortedList <- sort(javaListImported); print(\"Lista sortata:\"); print(SortedList)\n"+
                    "remove_border_20percent <- function(arr){\n"+
                    "\tn<-length(arr)\n"+
                    "\tcutoff<-ceiling(0.2*n)\n"+
                    "\treturn (arr[(cutoff+1):(n-cutoff-1)])}\n"+
                    "sorted_Cut_Arr<-remove_border_20percent(SortedList); print( \"Lista taiata 20% begin+end: \"); print(sorted_Cut_Arr)\n"+
                    "print(\"Average :\")\n"+
                    "avg<-mean(sorted_Cut_Arr)\n"+
                    "print(avg)\n";
        Value pyList = polyglot.eval("python",pyCode);
        List<Object> javaList=pyList.as(List.class);

        polyglot.getBindings("js").putMember("javaListImported",javaList);
        polyglot.eval("js",jsCode);

        polyglot.getBindings("R").putMember("javaListImported",javaList);
        polyglot.eval("R",rCode);

        //System.out.println(javaList);


        polyglot.close();
    }

    //functia MAIN
    public static void main(String[] args) {

        Context polyglot = Context.create();

        Value array = polyglot.eval("js", "[\"If\",\"we\",\"run\",\"the\",\"java\",\"command\",\"included\",\"in\",\"GraalVM\",\"we\",\"will\",\"be\",\"automatically\",\"using\",\"the\",\"Graal\",\"JIT\",\"compiler\",\"no\",\"extra\",\"configuration\",\"is\",\"needed\",\"I\",\"will\",\"use\",\"the\",\"time\",\"command\",\"to\",\"get\",\"the\",\"real\",\"wall\",\"clock\",\"elapsed\",\"time\",\"it\",\"takes\",\"to\",\"run\",\"the\",\"entire\",\"program\",\"from\",\"start\",\"to\",\"finish\",\"rather\",\"than\",\"setting\",\"up\",\"a\",\"complicated\",\"micro\",\"benchmark\",\"and\",\"I\",\"will\",\"use\",\"a\",\"large\",\"input\",\"so\",\"that\",\"we\",\"arent\",\"quibbling\",\"about\",\"a\",\"few\",\"seconds\",\"here\",\"or\",\"there\",\"The\",\"large.txt\",\"file\",\"is\",\"150\",\"MB\"];");
        String[] arr={"If","we","run", "the","java","command","included","in","GraalVM","we","will","be","automatically","using","the","Graal","JIT","compile","no","extra","configuration","is","needed","I","will","use","the","real","wall","clock","elapsed","time","it","takes","to","run","the","entire","program","from","start","to","finish","rather","than","setting","up","a","complicated","micro","benchmark","and","I","will","use","a","large","input","so","that","we","aren't","quibbling","about","a","few","seconds","here","or","there","The","large.txt","file","is","150MB"};
        //pentru fiecare cuvant, convertim la upcase folosind R si calculam suma de control folosind PYTHON

        Nod[] HT = new Nod[MyHash.M];
        MyHash.initHT(HT);

        int Counter;
        System.out.println("Citeste cate elem din vector se vor citi: ");
        Scanner s=new Scanner(System.in);
        Counter=s.nextInt();

        for (int i = 0; i < arr.length;i++){
            String element = arr[i];
            String upper = RToUpper(element);
            int crc = SumCRC(upper);
            System.out.println(upper + " -> " + crc);
            MyHash.insert(HT,arr[i],crc);
            if(i+1==Counter) break;
        }

        MyHash.printHT(HT);

        //LabEx3();


        // inchidem contextul Polyglot
        polyglot.close();
    }
}

