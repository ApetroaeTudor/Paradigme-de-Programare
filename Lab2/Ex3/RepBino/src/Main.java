import org.graalvm.collections.Pair;
import org.graalvm.polyglot.*;

public class Main {

    public static int[] getNumbers_PolyglotPython(){
        int[] arr=new int[2];

        Context polyglot=Context.newBuilder().allowAllAccess(true).build();

        String pyCode="while True:\n"+
                "    n=(int)(input('Cititi nr de aruncari: '))\n"+
                "    if n>0:\n"+
                "        break\n"+
                "    print('Nr invalid! Cititi din nou: ')\n"+
                "while True:\n"+
                "    x=(int)(input('Cititi x: '))\n"+
                "    if x>=1 and x<=n:\n"+
                "        break\n"+
                "    print('Nr x invalid, x trebuie sa fie 1<=x<=n, cititi din nou:')\n"+
                "arr = [n,x]\n"+
                "arr";

        Value val=polyglot.eval("python",pyCode);

        arr[0]=val.getArrayElement(0).asInt();
        arr[1]=val.getArrayElement(1).asInt();

        polyglot.close();
        return arr;
    }

    public static void binom_PolyglotR(){

        int[] arr=getNumbers_PolyglotPython();
        int n=arr[0];
        int x=arr[1];

        Context polyglot=Context.newBuilder().allowAllAccess(true).build();

        Value RBindings=polyglot.getBindings("R");

        RBindings.putMember("n",n);
        RBindings.putMember("x",x);

        String RCode= "p <- 0.5\n"+
                "NrIncercari <- 0:n\n"+
                "probabilities <-dbinom(NrIncercari,size=n,prob=p)\n"+
                "print(data.frame(Successes=NrIncercari,Probability=probabilities))\n"+
                "F=dbinom(x,size=n,prob=p)\n"+
                "print(F)\n";

        polyglot.eval("R",RCode);

        polyglot.close();
    }


    public static void main(String[] args) {
        binom_PolyglotR();
    }
}