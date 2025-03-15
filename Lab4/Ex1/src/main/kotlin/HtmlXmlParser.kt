import org.jsoup.Jsoup
import org.jsoup.nodes.Element

class HtmlXmlParser : Parser {
    override fun parse(text:String):MutableMap<Any?,Any?>{ //voi returna
        val parsedXmlHtmlDocument = Jsoup.parse(text)
        val myMap:MutableMap<Any?,Any?> = mutableMapOf()

        myMap.put(parsedXmlHtmlDocument,"type:Document") //solutie temporara
        return myMap
    }

    override fun print(text: String) {
        val parsedXmlHtmlDocument = Jsoup.parse(text)

        fun printElemsRecursive(root: Element, depth:Int=0){
            if(root.hasText()) println(" ".repeat(depth)+root.tagName()+": " + root.text().trim())
            if(root.hasAttr("href")) println(" ".repeat(depth+2) + " -----> hrefs: "+ root.select("[href]"))
            root.children().forEach(){
                printElemsRecursive(it,depth+1)
            }
        }

        printElemsRecursive(parsedXmlHtmlDocument,0)
    }

    override fun getResources(text: String, searchKey: String): List<String> {
        val myDataStructure=parse(text).keys.first()
        val returnList:MutableList<String> = mutableListOf()

        fun searchRecursive(root: Element){
            if(root.hasAttr("href")) {
                val temp= root.select("[href]").toString()
                searchKey.toRegex().find(temp)?.let{
                    if(!returnList.contains(it.value))
                        returnList.add(it.value)
                }
            }
            root.children().forEach(){
                searchRecursive(it)
            }
        }

        searchRecursive(myDataStructure as Element)

        return returnList
    }

}
