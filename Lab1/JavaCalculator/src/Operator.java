public class Operator {
    private char symbol;
    private int priority;

    Operator(char symbol){
        switch (symbol){
            case '(':
                this.symbol='(';
                priority=0;
                break;
            case ')':
                this.symbol=')';
                priority=0;
                break;
            case '+':
                this.symbol='+';
                priority=1;
                break;
            case '-':
                this.symbol='-';
                priority=1;
                break;
            case '*':
                this.symbol='*';
                priority=2;
                break;
            case '/':
                this.symbol='/';
                priority=2;
                break;
            case '^':
                this.symbol='^';
                priority=3;
                break;
            default:
                this.symbol=' ';
                priority=-1;
                break;
        }
    }



    public void setSymbol(char symbol){
        this.symbol=symbol;
    }
    public void setPriority(int priority){
        this.priority=priority;
    }
    public int getPriority(){
        return this.priority;
    }
    public char getSymbol(){
        return this.symbol;
    }

}
