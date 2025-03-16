import java.io.File
import java.nio.file.Files
import kotlin.io.path.Path

class LocalStorageManager(override val localDirName:String) : StorageManager{

    private val storageInitializer=StorageInitializer(localDirName)
    private val indexManager=IndexManager(storageInitializer.getIndexFile())
    private val noteManager=NoteManager(localDirName,indexManager)

    override fun initStorage() {
        storageInitializer.initStorage()
    }

    override fun createNumberedFileToDisk() {
        noteManager.createNumberedFileToDisk()
    }

    override fun removeNumberedFileFromDisk(index: Int) {
        noteManager.removeNumberedFileFromDisk(index)
    }

    override fun printAllNoteNames() {
        noteManager.printAllNoteNames()
    }

    override fun increaseCounter() {
        indexManager.increaseCounter()
    }

    override fun decreaseCounter() {
        indexManager.decreaseCounter()
    }

    override fun getCounter(): Int {
       return indexManager.getCounter()
    }


}


class StorageInitializer(private val localDirName:String){
    private val indexFile:File=File("$localDirName/noteIndexer")

    init {
        initStorage()
    }

    fun initStorage() {
        val mydir= File(localDirName)
        if(!(mydir.exists() && mydir.isDirectory)){
            Files.createDirectory(Path(localDirName))
        }

        val myFile= File("$localDirName/noteIndexer")
        if(!myFile.exists()){
            Files.createFile(Path("$localDirName/noteIndexer"))
        }
    }

    fun getIndexFile() : File = indexFile

}

class IndexManager(private val indexFile:File){

    fun increaseCounter() {
        val indexText=indexFile.readText() + "a"
        indexFile.writeText(indexText)
    }


    fun decreaseCounter() {
        var indexText=indexFile.readText()
        var currentCounter:Int=indexText.length
        if(currentCounter==0){
            throw Exception("can't decrease counter. it's 0")
        }
        else{
            currentCounter--
        }

        indexText ="a".repeat(currentCounter) //nr de caractere va fi nr de notite create pana acum
        indexFile.writeText(indexText)
    }

    fun getCounter(): Int = indexFile.readText().length

}

class NoteManager(private val localDirName: String,private val indexManager:IndexManager){
    fun createNumberedFileToDisk() {
        val currentIndex=indexManager.getCounter()
        val fileName="Note$currentIndex"

        val newFile:File=File("$localDirName/$fileName")
        if(!newFile.exists()){
            Files.createFile(Path("$localDirName/$fileName"))
        }
        indexManager.increaseCounter()
    }

    fun reIndexFiles(){
        val allFiles=File(localDirName).listFiles()?.sortedBy { it.name }
        var index=0
        allFiles?.forEach {
            if(it.name.compareTo("noteIndexer")!=0){
                val temp=File("${localDirName}/Note${index}")
                it.renameTo(temp)
                index++
            }
        }
    }

    fun removeNumberedFileFromDisk(index: Int) {
        val currentMaxIndex=indexManager.getCounter()
        if(index>currentMaxIndex || index<0) throw Exception("invalid index")

        try{
            Files.deleteIfExists(Path("$localDirName/Note$index"))
            indexManager.decreaseCounter()
            reIndexFiles()
        }
        catch (e: java. io. IOException){
            println("file was either removed already or didnt exist")
        }

    }

    fun printAllNoteNames() {
        val allFiles=File(localDirName).listFiles()?.sortedBy { it.name }
        allFiles?.forEach {
            if(it.name.compareTo("noteIndexer")!=0){
                println(it.name)
                if(it.readText().lines().size>0){
                    println("   --->Title: "+it.readText().lines()[0]+"\n")
                }
            }
        }
    }

}
