import java.time.LocalDate

class NotesManager(val myNoteRepo:LocalNoteRepository) {
    private val myMenuPrinter:NoteMenusPrinter=DisplayPrinter()

    fun manage(){
        var userInput:Int
        do{
            myMenuPrinter.printMainMenu()
            userInput= readLine()?.toInt() ?:0
            when(userInput){
                1->myNoteRepo.showNoteList()
                2->{
                    println("\nPlease Input Note Data: ")
                    println("Input Title: ")
                    val title:String = readlnOrNull() ?:"InvalidTitle"
                    println("Input Author: ")
                    val author:String = readlnOrNull() ?:"InvalidAuthor"

                    val currentDate=LocalDate.now()

                    val year:Int = currentDate.year
                    val month:Int= currentDate.monthValue
                    val day:Int= currentDate.dayOfMonth

                    println("Input Content: ")
                    val content:String= readlnOrNull()?:"InvalidContent"

                    myNoteRepo.addNote(title,author,Date(year,month,day),content)

                }
                3->{
                    myNoteRepo.showNoteList()
                    println("Please specify the index of the note to delete:")
                    val index:Int= readlnOrNull()?.toIntOrNull()?:throw Exception("Invalid Index chosen")
                    myNoteRepo.removeNote(index)
                }
                4->{
                    myNoteRepo.showNoteList()
                    println("Pick which note to modify: ")
                    val noteChoiceIndex:Int=readlnOrNull()?.toIntOrNull()?:throw Exception("Invalid Index chosen")
                    myMenuPrinter.printModifyNoteMenu()
                    val modifyIndex:Int= readlnOrNull()?.toIntOrNull()?:throw Exception("Invalid Index chosen")
                    when(modifyIndex){
                        1->{
                            println("Input new Title:")
                            val title:String = readlnOrNull() ?:"InvalidTitle"
                            myNoteRepo.myIOMaster.writeTitle(title,noteChoiceIndex)
                        }
                        2->{
                            println("Input new Author:")
                            val author:String= readlnOrNull()?:"InvalidAuthor"
                            myNoteRepo.myIOMaster.writeTitle(author,noteChoiceIndex)
                        }
                        3->{
                            println("Input new Content:")
                            val content:String = readlnOrNull()?:"InvalidContent"
                            myNoteRepo.myIOMaster.writeContent(content,noteChoiceIndex)
                        }
                    }

                }
                5->{
                    myNoteRepo.showNoteList()
                    println("Pick which note to view: ")
                    val myChoice:Int= readlnOrNull()?.toIntOrNull()?:throw Exception("Invalid index chosen")
                    println(myNoteRepo.myIOMaster.readWholeFile(myChoice))
                }
                6-> println("exiting..")
                else -> println("invalid input, choose again")
            }


        }while (userInput!=6)
    }
}

class DisplayPrinter() : NoteMenusPrinter{
    override fun printMainMenu(){
        println("\nMENU:\n" +
                "     ---- 1 ---- Show All Notes\n" +
                "     ---- 2 ---- Create a Note\n" +
                "     ---- 3 ---- Delete a Note\n" +
                "     ---- 4 ---- Modify a note\n" +
                "     ---- 5 ---- View a Note\n"+
                "     ---- 6 ---- Exit\n")
    }

    override fun printModifyNoteMenu(){
        println("MODIFY A NOTE:\n" +
                "    ---- 1 ---- Change Title\n" +
                "    ---- 2 ---- Change Author\n" +
                "    ---- 3 ---- Change Content")
    }


}

