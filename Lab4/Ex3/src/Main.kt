import java.time.LocalDate

fun main() {
    try{
        val mainUser:User=User()
        mainUser.start()
        val myStorageManager:StorageManager=LocalStorageManager("myDir")
        val myStorageIOMaster:StorageIO=StorageIOMaster("myDir")
        val myLocalNoteRepository:LocalNoteRepository=LocalNoteRepository(myStorageManager,myStorageIOMaster)

        val myNoteManager=NotesManager(myLocalNoteRepository)
        myNoteManager.manage()

    }
    catch (e:Exception){
        println(e.message)
    }

}