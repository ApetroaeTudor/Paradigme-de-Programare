import nl.siegmann.epublib.domain.Book
import nl.siegmann.epublib.epub.EpubReader
import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import java.io.File
import java.io.FileInputStream

fun epubToHtml(fileName:String):String{
    val filePath = System.getProperty("user.dir") + "/" + fileName
    val myEpubReader: EpubReader = EpubReader()
    val book: Book = myEpubReader.readEpub(FileInputStream(filePath))
    val resources = book.contents

    val htmlContents: StringBuilder = StringBuilder()
    for (res in resources) {
        htmlContents.append(String(res.data))
    }

    return htmlContents.toString()
}

fun writeToIntermediaryHtml(fileNameHtml:String,fileName:String):Unit{
    val htmlContents=epubToHtml(fileName)
    val fileIntermediar: File = File(fileNameHtml)
    if (fileIntermediar.isFile) {
        fileIntermediar.writer().write(htmlContents)
    }
    else{
        println("File doesn't exist")
    }
}

fun writeToIntermediaryStory(fileNameFinalStory:String,fileName:String,fileBackup:String):Unit{
    val htmlContents=epubToHtml(fileName)
    val filePath = System.getProperty("user.dir") + "/" + fileNameFinalStory

    val fisier:File=File(filePath)
    val backupFisier:File=File(fileBackup)

    if(!fisier.exists() || !backupFisier.exists() ){
        throw Exception("File doesn't exist")
    }

    val doc: Document = Jsoup.parse(htmlContents.toString())
    val writeBuffer:StringBuilder=StringBuilder()
    doc.select("p").forEach{
        writeBuffer.append(it.text()).append("\n")
    }

    fisier.writer().write(writeBuffer.toString())
    backupFisier.writer().write(writeBuffer.toString())
}

fun eliminateByRegex(fileName:String,reg:String,replaceWith:String):Unit{
    val fisierCitireScriere:File=File(fileName);

    if(!fisierCitireScriere.exists()){
        throw Exception("Can't open file to read intermediateStory")
    }

    var intermediateStory=fisierCitireScriere.reader().readText()
    intermediateStory=intermediateStory.replace(reg.toRegex(),replaceWith)

    fisierCitireScriere.writer().write(intermediateStory)

}

fun replaceAuthorName(fileName: String,reg:String,replaceWith: String):Unit{
    val fisierCitireScriere:File=File(fileName);
    if(!fisierCitireScriere.exists()){
        throw Exception("Can't open file to read intermediateStory")
    }
    var intermediateStory=fisierCitireScriere.reader().readText()

    val matches=reg.toRegex().findAll(intermediateStory) //caut toate match-urile care se leaga de Cuvant [optional](Cuvant2)
    val matchesMapRange= mutableMapOf< String, ArrayList< Pair<Int,Int> >? >() //voi tine datele intr-un map cu cheia string, unde fiecarui string ii coreleaza o lista ce contine [pozitie inceput,pozitie final]

    matches.forEach{ //pun in map-ul meu
        if(!matchesMapRange.containsKey(it.value)){
            var arr=ArrayList<Pair<Int,Int>>()
            arr.add( Pair<Int,Int>(it.range.first,it.range.last) )
            matchesMapRange.put(it.value,arr)
        }
        else{
            var arr=matchesMapRange[it.value]
            arr?.add(Pair<Int,Int>(it.range.first,it.range.last))
            matchesMapRange.put(it.value,arr)
        }
    }

    val cutoff=Pair<Int,Int>( (intermediateStory.length*0.01).toInt(), (intermediateStory.length*0.99).toInt()) //definesc o regiune de cutoff pentru ca numele autorului este de obicei ori
                                                                                                                //la inceputul cartii de multe ori, ori la sfarsit de cateva ori


    for(key in matchesMapRange.keys){ //pentru fiecare cheie fac verificari
        var isAuthor:Boolean=true
        for(apparition in matchesMapRange.get(key)!!){ //pentru fiecare cheie analizez perechile de pozitii
            if(apparition.first>cutoff.first && apparition.first<cutoff.second){ //daca Key incepe inauntrul cutoff region atunci nu e valid ca autor
                isAuthor=false
            }
            if(apparition.second>cutoff.first && apparition.second<cutoff.second){ //daca Key se sfarseste inauntrul cutoff region atunci nu e valid ca autor
                isAuthor=false
            }

        }
        if(isAuthor){ //ca sa fie considerat evident autor trebuie sa apara de mai multe ori, asta presupune existenta unei prefete unde sunt puse date despre autor
                      // de obicei intr-o carte autorul nu este neaparat separat de whitespaces sau altele, in cartile epub descarcate de mine nu era asa niciodata
            var checkFrequency:Int=0
            val matchesAuthor=key.toRegex().findAll(intermediateStory).count()
            if(matchesAuthor>5){
                intermediateStory=intermediateStory.replace(key,replaceWith)
                println(key)
                println(matchesMapRange.get(key))
            }


        }
    }


    fisierCitireScriere.writer().write(intermediateStory)

}


fun replaceRomanianCharacters(fileName:String):Unit{
    val fisierCitireScriere:File=File(fileName);
    if(!fisierCitireScriere.exists()){
        throw Exception("Can't open file to read intermediateStory")
    }
    var intermediateStory=fisierCitireScriere.reader().readText()

    for(char in intermediateStory){
        when(char){
            'ă'->intermediateStory=intermediateStory.replace("ă","a")
            'ă'.uppercaseChar()->intermediateStory=intermediateStory.replace("ă".uppercase(),"a".uppercase())

            'â'->intermediateStory=intermediateStory.replace("â","a")
            'â'.uppercaseChar()->intermediateStory=intermediateStory.replace("â".uppercase(),"a".uppercase())

            'î'->intermediateStory=intermediateStory.replace("î","i")
            'î'.uppercaseChar()->intermediateStory=intermediateStory.replace("î".uppercase(),"i".uppercase())

            'ș'->intermediateStory=intermediateStory.replace("ș","s")
            'ș'.uppercaseChar()->intermediateStory=intermediateStory.replace("ș".uppercase(),"s".uppercase())

            'ş'->intermediateStory=intermediateStory.replace("ş","s")
            'ş'.uppercaseChar()->intermediateStory=intermediateStory.replace("ş".uppercase(),"s".uppercase())

            'ț'->intermediateStory=intermediateStory.replace("ț","t")
            'ț'.uppercaseChar()->intermediateStory=intermediateStory.replace("ț".uppercase(),"t".uppercase())

            'ţ'->intermediateStory=intermediateStory.replace("ţ","t")
            'ţ'.uppercaseChar()->intermediateStory=intermediateStory.replace("ţ".uppercase(),"t".uppercase())

        }
    }

    fisierCitireScriere.writer().write(intermediateStory)

}