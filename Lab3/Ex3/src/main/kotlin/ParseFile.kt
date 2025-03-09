import org.jsoup.Jsoup

fun parseFile(url:String):List<String>{

        val elemsElements = Jsoup.connect(url).get().select("a")
        val httpRegex="^https?.*$"
        var refs=ArrayList<String>()
        for(elem in elemsElements){
            refs.add(elem.attr("href"))
        }
        val removeElems=ArrayList<String>()

        for (elem in refs){
            if(httpRegex.toRegex().matches(elem)){
                removeElems.add(elem)
            }

        }

        for (it in removeElems){
            refs.remove(it)
        }

        refs.removeIf { it=="/" }
        refs.removeIf{ it=="#"}
        return refs.distinct()
}




