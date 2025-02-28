import java.util.Stack;

public abstract class PostfixFactory {
    public static String CreatePostfix(String infix_form){
        infix_form=infix_form.replaceAll("\\s+","");
        StringBuffer postfix_form=new StringBuffer();
        Stack<Operator> st=new Stack<Operator>();
        int nrOfOpenParantheses=0;

        for(int i=0;i<infix_form.length();i++){

            if(CheckIfIsOperator(infix_form.charAt(i))){ //verific daca e operator ca sa il pun pe stiva
                //trebuie sa verific si daca operatorul adaugat ar schimba stiva
                switch (infix_form.charAt(i)){
                    case '(':
                        nrOfOpenParantheses++;
                        st.push(new Operator(infix_form.charAt(i)));
                        break;
                    case '+', '-':
                        while(!st.empty()) {
                            if (st.peek().getPriority() >= 1) {
                                postfix_form.append(st.pop().getSymbol());
                                postfix_form.append(' ');
                            }
                            else{
                                break;
                            }
                        }
                        st.push(new Operator(infix_form.charAt(i)));

                        break;
                    case '*','/':
                        while(!st.empty()) {
                            if (st.peek().getPriority() >= 2) {
                                postfix_form.append(st.pop().getSymbol());
                                postfix_form.append(' ');
                            }
                            else{
                                break;
                            }
                        }
                        st.push(new Operator(infix_form.charAt(i)));
                        break;
                    case '^':
                        st.push(new Operator(infix_form.charAt(i)));
                        break;
                    case ')':
                        if(nrOfOpenParantheses>0){
                            nrOfOpenParantheses--;
                            while(st.peek().getSymbol()!='('){
                                postfix_form.append(st.pop().getSymbol());
                                postfix_form.append(' ');
                            }
                            st.pop();
                        }
                        break;

                }
            }

            else{
                int nr=0;
                boolean inserted=false;


                if(i+1<infix_form.length()){
                    if(!PostfixFactory.CheckIfIsOperator(infix_form.charAt(i+1))) {
                        while (!PostfixFactory.CheckIfIsOperator(infix_form.charAt(i))) {
                            nr = nr * 10 + Integer.valueOf(infix_form.charAt(i))-48;
                            i++;
                            if(i==infix_form.length()){
                                i--;
                                break;
                            }
                        }
                        if(i!=infix_form.length()-1)
                            i--;
                        postfix_form.append(String.valueOf(nr));
                        postfix_form.append(' ');
                        inserted=true;
                    }

                }
                if(!inserted) {
                    postfix_form.append(infix_form.charAt(i));
                    postfix_form.append(' ');
                }



//                if(!PostfixFactory.CheckIfIsOperator(infix_form.charAt(i+1))) {
//                    while (i + 1 < infix_form.length() && !PostfixFactory.CheckIfIsOperator(postfix_form.charAt(i+1))) { //e un nr din mai multe cifre
//                        nr = nr * 10 + infix_form.charAt(i);
//                        i++;
//                    }
//                }
//                else {
//                    postfix_form.append(infix_form.charAt(i));
//                }
//                postfix_form.append(' ');
            }


        }

        while(!st.empty()){
            postfix_form.append(st.pop().getSymbol());
            postfix_form.append(' ');
        }

        return postfix_form.toString();
    }




    static boolean CheckIfIsOperator(char c){
        return c == '+' || c == '-' || c == '*' || c == '/' || c == '(' || c == ')' || c=='^';
    }

}
