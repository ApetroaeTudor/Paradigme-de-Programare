import kotlin.jvm.Throws

interface NoteContainer {
    fun addNote(noteName:String,noteAuthor:String,noteCreationDate:Date,noteContent:String)
    fun removeNote(noteNumber:Int)
}

interface NoteDisplayer {
    fun showNoteList()
}


interface StorageIndexManager{
    fun increaseCounter()

    @Throws(Exception::class)
    fun decreaseCounter()
    fun getCounter():Int

}

interface StorageManager : StorageIndexManager{
    val localDirName:String

    @Throws(Exception::class)
    fun initStorage()
    fun createNumberedFileToDisk()
    fun removeNumberedFileFromDisk(index:Int)

    fun printAllNoteNames()
}



interface StorageReader {
    val localDirName:String

    @Throws(Exception::class)
    fun readWholeFile(index:Int):String

    @Throws(Exception::class)
    fun readTitle(index:Int):String

    @Throws(Exception::class)
    fun readDate(index: Int):String

    @Throws(Exception::class)
    fun readAuthor(index: Int):String

    @Throws(Exception::class)
    fun readContent(index: Int):String
}

interface StorageWriter {
    val localDirName:String
    @Throws(Exception::class)
    fun writeTitle(title:String,index:Int)

    @Throws(Exception::class)
    fun writeDate(date:Date,index:Int)

    @Throws(Exception::class)
    fun writeAuthor(author:String,index:Int)

    @Throws(Exception::class)
    fun writeContent(content:String,index:Int)
}

interface StorageIO :StorageReader,StorageWriter {
    override val localDirName: String
}

interface NoteMenusPrinter{
    fun printMainMenu()
    fun printModifyNoteMenu()
}

interface WelcomeScreenPrinter{
    fun welcomeScreen()
}



