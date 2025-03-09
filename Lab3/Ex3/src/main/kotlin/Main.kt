
fun main() {
    val url:String="https://annas-archive.org/"

    try {
        val finalRefs:List<String> = parseFile(url)
        val tagList=makeTagList(finalRefs,url)
        println(tagList)
        Tag.linkChildrenByDepth(1,tagList,url)
        Tag.linkChildrenByDepth(2,tagList)

        tagList.sortBy { it.depth } //primul element e capul arborelui

        tagList.forEach {
            it.printTagWithChildrenAndParent()
        }


    }
    catch (e:Exception){
        println(e.message)
    }














}