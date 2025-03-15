import org.jsoup.Jsoup
import java.io.File

fun main() {
    val yamlFile: File = File("test.yaml")
    val yamlText=yamlFile.reader().readText()

    val htmlFile:File=File("test.html")
    val htmlText=htmlFile.reader().readText()

    val jsonFile:File=File("test.json")
    val jsonText=jsonFile.reader().readText()


//
    val myYamlParser:Parser=YamlParser()
//    val myDataStructure=myYamlParser.parse(yamlText).keys.first()
    //myYamlParser.print(yamlText)

    val myHtmlParser:Parser=HtmlXmlParser()
//    myHtmlParser.print(htmlText)
//    println(myHtmlParser.getResources(htmlText,RegexConstants.URLREGEX))

    val myJsonParser:Parser=JsonParser()
//    println(myJsonParser.getResources(jsonText,RegexConstants.URLREGEX))

//    println(myParser.getResources(yamlText,RegexConstants.URLREGEX))

//    val jsonUrl="https://randomuser.me/api/"
//    val httpUrl="https://github.com"

    //println(myResponse.select("body").text().startsWith('{'))
}