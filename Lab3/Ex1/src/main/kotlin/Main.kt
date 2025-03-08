
import org.jsoup.HttpStatusException
import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import org.jsoup.parser.*

fun main() {
    val url:String="http://rss.cnn.com/rss/edition.rss"
    val rssman:RSSManager=RSSManager(url)
    rssman.printRSSInfo()


}