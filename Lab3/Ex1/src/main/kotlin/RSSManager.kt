import org.jsoup.HttpStatusException
import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import org.jsoup.nodes.Element
import org.jsoup.select.Elements

class RSSManager(var url:String) {
    var doc: Document?=null
    var mainChannel: Elements?=null
    var items: ArrayList<Element> = ArrayList<Element>()



    private fun tryToOpen(): Unit {
        try {
            doc = Jsoup.connect(url).get()
        } catch (hte: HttpStatusException) {
            println(hte.message)
        }
    }

    private fun extractElementsFromDoc():Unit{
        doc?.let{ nonNullDoc ->
            mainChannel=nonNullDoc.select("channel")
            mainChannel?.let{
                for(elem in it.select("item")){
                    items.add(elem)
                }
            }

        }
    }

    private fun returnLinkFromItem(elem:Element):String {
        return elem.select("link").text()
    }

    private fun returnLinkFromMainChannel():String{
        mainChannel?.let {
            return it.select("link").get(0).text()
        }
        throw Exception("Failed to open MainChannel!")
    }

    private fun returnTitleFromItem(elem:Element):String{
        return elem.select("title").text()
    }

    private fun returnTitleFromMainChannel():String{
        mainChannel?.let {
            return it.select("title").get(0).text()
        }
        throw Exception("Failed to open MainChannel!")
    }


    fun printRSSInfo():Unit{
        tryToOpen()
        extractElementsFromDoc()

        println("\n\nMain Channel Info:"+"\n")

        try{
            println("Channel Title: " + returnTitleFromMainChannel())
            println("Channel Link: " + returnLinkFromMainChannel())
            println()
        }
        catch (e:Exception){
            println(e.message)
        }

        println("Items info:"+"\n")
        try {
            items.forEach{
                println("Title: "+ returnTitleFromItem(it))
                println("Link: "+ returnLinkFromItem(it)+"\n")
            }
        }
        catch (e:Exception){
            println(e.message)
        }

    }




}