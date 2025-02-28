public class MyHash {
    public static final int M=61;

    public static void initHT(Nod[] HT){
        for(int i=0;i<M;i++){
            HT[i]=null;
        }
    }

    public static Nod find(Nod[] HT, String val, int key){
        Nod p=HT[key];
        while(p!=null){
            if(p.data.equals(val)){
                return p;
            }
            p=p.succ;
        }
        return null;
    }

    public static void insert(Nod[] HT, String val,int key){
        Nod p=new Nod();
        p.data=val;
        Nod q;
        if(HT[key]==null){
            HT[key]=p;
            p.succ=null;
        }
        else{
            q=find(HT,val,key);
            if(q==null){
                p.succ=HT[key];
                HT[key]=p;
            }
            else{
                q.succ=p;
                p.succ=null;
            }
        }
    }

    public static void printHT(Nod[] HT){
        Nod p=null;
        for(int i=0;i<M;i++){
            if(HT[i]!=null){
                System.out.println("valori cu cheia: " + i);
                p=HT[i];
            }
            while(p!=null){
                System.out.print(" "+ p.data+" ");
                p=p.succ;
            }
            if(HT[i]!=null){
                System.out.println();
            }
        }
    }
}
