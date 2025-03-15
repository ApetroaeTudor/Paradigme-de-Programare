import org.jsoup.Jsoup
import org.jsoup.nodes.Document

class Crawler(val url:String,val max_depth:Int=0,val printContents:Boolean=false,val visitedUrls:ArrayList<String> = ArrayList()) {

        fun getResource(url:String):Document{
            val myResource=Jsoup.connect(url).ignoreContentType(true).get()
            return myResource
        }

        fun processContent(){

            fun recursiveCrawl(baseUrl:String,depth:Int=0){
                if(depth>max_depth) return
                    val fileType=checkFileType(baseUrl)
                    val myParser:Parser = ParserFactory.getParser(fileType)
                    var textToParse:String=""

                    var content:Document=Jsoup.parse("")
                    try {
                        content = getResource(baseUrl)
                    }
                    catch (e:Exception){
                        println("bad connection")
                    }

                    textToParse= when(fileType){
                        "yaml","yml","json"->content.select("body").text()
                        else ->content.html()
                    }

                    if(printContents){
                        myParser.print(textToParse)
                    }
                    println("\t".repeat(depth)+baseUrl)


                    val urls: List<String> = myParser.getResources(textToParse,RegexConstants.URLREGEX)

                    if(!visitedUrls.contains(baseUrl)){
                        visitedUrls.add(baseUrl)
                    }

                    urls.forEach(){ newUrl->
                        if (!visitedUrls.contains(newUrl)) {
                            recursiveCrawl(newUrl, depth + 1)
                        }
                    }

                }

            recursiveCrawl(url,0)

        }
}

