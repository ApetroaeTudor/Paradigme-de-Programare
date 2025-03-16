
class LocalNoteRepository(val myStorageManager:StorageManager,val myIOMaster:StorageIO) : NoteContainer, NoteDisplayer {

    override fun addNote(noteName: String, noteAuthor: String, noteCreationDate: Date, noteContent: String) {
        try{
            myStorageManager.createNumberedFileToDisk()
            myIOMaster.writeTitle(noteName,myStorageManager.getCounter()-1)
            myIOMaster.writeAuthor(noteAuthor,myStorageManager.getCounter()-1)
            myIOMaster.writeDate(noteCreationDate,myStorageManager.getCounter()-1)
            myIOMaster.writeContent(noteContent,myStorageManager.getCounter()-1)
        }
        catch (e:Exception){
            println(e.message)
        }
    }

    override fun removeNote(noteNumber: Int) {
        try{
            myStorageManager.removeNumberedFileFromDisk(noteNumber)
        }
        catch (e:Exception){
            println(e.message)
        }
    }

    override fun showNoteList() {
        myStorageManager.printAllNoteNames()
    }

}