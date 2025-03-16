
fun main() {

    val myCrawler = Crawler("https://annas-archive.org/",2,false)
    myCrawler.processContent()
    println(myCrawler.visitedUrls.count())

}
