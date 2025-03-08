import java.io.File
import java.nio.file.Files
import java.nio.file.Paths
import nl.siegmann.epublib.domain.Book
import nl.siegmann.epublib.epub.EpubReader
import org.jsoup.Jsoup
import org.jsoup.parser.*
import java.io.FileInputStream


class Dictionar(var languageOption:Int=0,
                val dictionar:HashMap<String,String> = hashMapOf<String,String>(),
                var nrOfElements:Int=0
                ){ //optiunea 0 e engleza->romana, optiunea 1 e engleza -> franceza, 2= engleza->franceza

    init {
        if (languageOption<0 || languageOption>2){
            languageOption=0
        }
    }

    fun initDictionary(wordsToBeTranslated:Array<String>, translationWords:Array<String>): Unit{
        for( (index, word) in wordsToBeTranslated.withIndex() ){
            dictionar.put(word,translationWords[index])
            if(index>=translationWords.size){ //daca sunt mai multe cuvinte in dictionar decat in sirul de traduceri
                dictionar.put(word,"[Translation Undefined]");
            }
        }
    }

    fun initDictionaryFromAFile(fileName:String):Unit{
        val option:Int=this.languageOption
        val fisier:File=File("./$fileName")

        if(fisier.exists()){
            val text=fisier.readLines()
            val wordsToBeTranslated=text.get(0).split(" ").toTypedArray()
            val translations=text.get(option+1).split(" ").toTypedArray()
            this.initDictionary(wordsToBeTranslated,translations)
        }
        else{
            throw Exception("File doesn't exist!")
        }
    }

    fun insertElementIntoDictionary(word:String, translation:String):Unit{
        dictionar.put(word,translation);
    }

    fun getTranslationForAWord(word:String):String?{
        val retval:String?= dictionar[word]

        if(retval!=null){
            return retval
        }

        return null
    }

    fun contains(word:String):Boolean{
        if(dictionar[word]!=null){
            return true;
        }
        return false;
    }

    fun translateText(sectionToBeTranslated:String):String{
        val words=sectionToBeTranslated.split(" ")
        val wordsTrimmed = mutableListOf<String>()
        for(word in words){
            wordsTrimmed.add(word.trim(',','.'))
        }

        var returnVal:String=""
        for(item in wordsTrimmed){
            if(this.contains(item)){
                returnVal=returnVal+ " "+ this.getTranslationForAWord(item)
            }
            else{
                returnVal=returnVal+ " [NotDefined]"
            }
        }
        return returnVal
    }

}


abstract class FileManaging(){
    companion object{

        fun printStringToAFile(fileName:String, stringToPrint:String):Unit{
            val currentPath=System.getProperty("user.dir") //aici se va crea un fisier

            val fisier:File = File("./$fileName")

            if(fisier.exists()){
                fisier.writeText(stringToPrint)
            }
            else{
                Files.createFile( Paths.get( "$currentPath/$fileName"))
                Files.writeString(Paths.get( "$currentPath/$fileName"),stringToPrint)
            }
        }


        fun readTextFromEpub(filename:String):String{
            val epubFilePath="${System.getProperty("user.dir")}/$filename"
            val fisier:File=File(epubFilePath)

            if(!fisier.exists())
                throw Exception("File doesn't exist!!")

            val inputStream=FileInputStream(epubFilePath)
            val epubReader:EpubReader=EpubReader()
            val book:Book=epubReader.readEpub(inputStream)

            val contents=book.contents
            val ContentString=StringBuilder()
            for(content in contents){
                ContentString.append(content.inputStream.reader().readText())
            }

            val HtmlContent=Jsoup.parse(ContentString.toString())

            val paragraph=HtmlContent.select("p").text()

            return paragraph

        }
    }
}