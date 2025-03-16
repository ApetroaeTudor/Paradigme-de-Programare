import java.io.File

class StorageIOMaster(override val localDirName: String) : StorageIO{

    private val myIOReader=StorageIOReader(localDirName)
    private val myIOWriter=StorageIOWriter(localDirName)
    override fun readWholeFile(index: Int): String = myIOReader.readWholeFile(index)

    override fun readTitle(index: Int): String = myIOReader.readTitle(index)

    override fun readDate(index: Int): String = myIOReader.readDate(index)

    override fun readAuthor(index: Int): String = myIOReader.readAuthor(index)

    override fun readContent(index: Int): String = myIOReader.readContent(index)

    override fun writeTitle(title: String, index: Int) = myIOWriter.writeTitle(title,index)

    override fun writeDate(date: Date, index: Int) = myIOWriter.writeDate(date,index)

    override fun writeAuthor(author: String, index: Int) = myIOWriter.writeAuthor(author,index)

    override fun writeContent(content: String, index: Int) = myIOWriter.writeContent(content,index)

}



class StorageIOReader(override val localDirName: String) : StorageReader{
    override fun readWholeFile(index: Int): String {
        val currentFile= File("$localDirName/Note${index}")
        if (currentFile.exists()){
            return currentFile.readText()
        }
        throw Exception("could not read file")
    }

    override fun readTitle(index: Int): String {
        val currentFile= File("$localDirName/Note${index}")
        if(currentFile.exists()){
            val text=currentFile.readText()
            if(text.lines().size==0){
                throw Exception("No title")
            }
            else{
                return text.lines()[0]
            }
        }
        throw Exception("could not read file")
    }

    override fun readAuthor(index: Int): String {
        val currentFile= File("$localDirName/Note${index}")
        if(currentFile.exists()){
            val text=currentFile.readText()
            if(text.lines().size<=1){
                throw Exception("No author")
            }
            else{
                return text.lines()[1]
            }
        }
        throw Exception("could not read file")
    }

    override fun readDate(index: Int): String {
        val currentFile= File("$localDirName/Note${index}")
        if(currentFile.exists()){
            val text=currentFile.readText()
            if(text.lines().size<=2){
                throw Exception("No date")
            }
            else{
                return text.lines()[2]
            }
        }
        throw Exception("could not read file")
    }

    override fun readContent(index: Int): String {
        val currentFile= File("$localDirName/Note${index}")
        if(currentFile.exists()){
            val text=currentFile.readText()
            if(text.lines().size<=3){
                throw Exception("No content")
            }
            else{
                val returnString=StringBuilder("")
                for(i in 4..text.lines().size){
                    returnString.append(text.lines()[i]+"\n")
                }
                return returnString.toString()
            }
        }
        throw Exception("could not read file")
    }
}


class StorageIOWriter(override val localDirName: String) : StorageWriter{
    override fun writeTitle(title: String, index: Int) {
        val currentFile= File("$localDirName/Note${index}")
        if(currentFile.exists()){
            val tempTextLines = currentFile.readLines().toMutableList()
            if (tempTextLines.size==0) {
                tempTextLines.add(title)
                currentFile.writeText(tempTextLines.joinToString("\n"))
            }
            else{
                tempTextLines[0]=title
                currentFile.writeText(tempTextLines.joinToString("\n"))
            }

        }
        else{
            throw Exception("Can't write. File doesn't exist")
        }
    }

    override fun writeAuthor(author: String, index: Int) {
        val currentFile= File("$localDirName/Note${index}")
        if(currentFile.exists()){
            val tempTextLines = currentFile.readLines().toMutableList()
            if (tempTextLines.size<=1) {
                tempTextLines.add("Author: $author")
                currentFile.writeText(tempTextLines.joinToString("\n"))
            }
            else{
                tempTextLines[1]="Author: $author"
                currentFile.writeText(tempTextLines.joinToString("\n"))
            }
        }
        else{
            throw Exception("Can't write. File doesn't exist")
        }
    }
    override fun writeDate(date: Date, index: Int) {
        val currentFile= File("$localDirName/Note${index}")
        if(currentFile.exists()){
            val tempTextLines = currentFile.readLines().toMutableList()
            if (tempTextLines.size<=2) {
                tempTextLines.add("Creation Date: ${date.toString()}")
                currentFile.writeText(tempTextLines.joinToString("\n"))
            }
            else{
                tempTextLines[2]="Creation Date: ${date.toString()}"
                currentFile.writeText(tempTextLines.joinToString("\n"))
            }
        }
        else{
            throw Exception("Can't write. File doesn't exist")
        }
    }
    override fun writeContent(content: String, index: Int) {
        val currentFile= File("$localDirName/Note${index}")
        if(currentFile.exists()){
            val tempTextLines = currentFile.readLines().toMutableList()
            if (tempTextLines.size<=3) {
                tempTextLines.add("Content: \n$content")
                currentFile.writeText(tempTextLines.joinToString("\n"))
            }
            else{
                tempTextLines[3]="Content: $content"
                currentFile.writeText(tempTextLines.joinToString("\n"))
            }
        }
        else{
            throw Exception("Can't write. File doesn't exist")
        }
    }

}