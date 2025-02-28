import java.nio.DoubleBuffer;
import java.util.Stack;

public abstract class PostfixEvaluator {

    public static double EvaluatePostfix(String postfix_form){
        double res=0;
        double op1=0;
        double op2=0;
        Stack<Double> st=new Stack<Double>();
        for(int i=0;i<postfix_form.length();i=i+2){

                if(PostfixFactory.CheckIfIsOperator(postfix_form.charAt(i))){ //verific daca elem curent e operator

                    if(!st.empty()){ //daca elem curent e operator atunci dau pop la primele 2 nr dp stiva pentru a face o operatie cu ele
                        op1=st.pop();
                        if(!st.empty()){
                            op2=st.pop();
                        }
                        else{
                            return -1;
                        }
                    }
                    else{
                        return -1;
                    }
                    st.push( PostfixEvaluator.DoOperation(postfix_form.charAt(i),op2,op1) );
                }
                else{ //partea de push pe stack de nr
                    boolean InsertedOnStack=false;
                    double nr=0;
                    if(i+1<postfix_form.length()){
                        if(postfix_form.charAt(i+1)!=' ') {
                            while (postfix_form.charAt(i)!=' ') {
                                nr = nr * 10 + Double.valueOf(postfix_form.charAt(i)) - 48;
                                i++;
                            }
                            i--;
                            st.push(nr);
                            InsertedOnStack = true;
                        }
                    }

                    if(!InsertedOnStack){
                        st.push(Double.valueOf(postfix_form.charAt(i))-48);
                    }

                }

            }

        res= Double.valueOf(st.pop());
        return res;
    }





    public static double DoOperation(char operator, double op1, double op2){
        double returnval=-1;
        if(!PostfixFactory.CheckIfIsOperator(operator)){
            return returnval;
        }
        switch (operator){
            case '+':
                returnval=op1+op2;
                break;
            case '-':
                returnval=op1-op2;
                break;
            case '*':
                returnval=op1*op2;
                break;
            case '/':
                if(op2!=0){
                    returnval=op1/op2;
                }
                break;
            case '^':
                returnval=1;
                for(int i=0;i<op2;i++){
                    returnval=returnval*op1;
                }
                break;
        }
        return returnval;
    }
}
