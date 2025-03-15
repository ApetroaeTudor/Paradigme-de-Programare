import org.jsoup.Jsoup
import org.jsoup.nodes.Document

interface HtmlLibraryPrinter {
    fun printBooks(bookSet:MutableSet<Book>):Unit
}

class HtmlPrinter() : HtmlLibraryPrinter{
    override fun printBooks(bookSet: MutableSet<Book>) {

        fun printParsedHtmlDoc(doc:Document){
            println(doc.html())
        }
        var myDoc:Document
        bookSet.forEach(){ book->
            val mappedContent: MutableMap<String, String> = book.getAttributesAsMap()

            myDoc=Jsoup.parse("")

            mappedContent.forEach(){ (key,value)->
                if(key.compareTo("text")==0){
                    myDoc.body().appendElement("Continut").text(value)
                }
                else{
                    myDoc.head().appendElement(key).text(value)
                }
            }

            println(myDoc.html())
            println()
        }
    }
}