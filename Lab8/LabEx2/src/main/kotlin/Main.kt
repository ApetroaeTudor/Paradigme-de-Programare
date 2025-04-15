import java.io.File
import kotlin.system.exitProcess

fun main() {
    val loremFile= File("src/main/LoremIpsum.txt")
    if(!loremFile.exists()){
        println("Error opening file")
    }
    else{
        val text=loremFile.readText()
        val tokens=text.replace(",","").replace(".","").split(" ")

        val myCaretaker=Caretaker()
        val myOriginator=Originator()
        myOriginator.add(SmallWordConsumer(myOriginator,myCaretaker))
        myOriginator.add(LargeWordConsumer(myOriginator,myCaretaker))
        tokens.forEach(){
            myCaretaker.addMemento(myOriginator.setMessage(it))
        }
    }

}