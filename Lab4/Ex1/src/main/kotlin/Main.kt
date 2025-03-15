
fun main() {

    val myCrawler = Crawler("https://annas-archive.org/",2,true)
    myCrawler.processContent()
    println(myCrawler.visitedUrls.count())

}
