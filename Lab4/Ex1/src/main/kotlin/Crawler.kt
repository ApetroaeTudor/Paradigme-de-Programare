import org.jsoup.Jsoup
import org.jsoup.nodes.Document

class Crawler(private val url:String) {

    object NuStiuSaFacAltfel {
        fun getResource(url:String):Document{
            val myResource=Jsoup.connect(url).get()
            return myResource
        }

        fun processContent(url:String){
            val fileType=checkFileType(url)
            var myParser:Parser = ParserFactory.getParser(fileType)
            val content= getResource(url)

        }
    }

}

