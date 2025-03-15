import org.jsoup.Jsoup

interface Parser {
    fun parse(text:String):MutableMap<Any?,Any?>
}


object ParserFactory{
    fun getParser(contentType:String):Parser{
        return when(contentType){
            "yaml" -> YamlParser()
            "yml" -> YamlParser()
            "json" -> JsonParser()
            else -> HtmlXmlParser()
        }
    }
}


fun checkFileType(url:String):String{
    var returnedString=""
    try{
        val myResponse= Jsoup.connect(url).ignoreContentType(true).execute()
        myResponse.contentType()?.let{ type->
            if(type.contains("html")){
                returnedString="html"
            } else if(type.contains("yaml")|| type.contains("yml")){
                returnedString="yaml"
            } else if(type.contains("json")){
                returnedString="json"
            } else{
                returnedString="xml"
            }
        }
        return returnedString

    }
    catch (e:java.io.IOException){
        println(e.message)
    }

    throw IllegalArgumentException("Response from url does not match any defined types")
}