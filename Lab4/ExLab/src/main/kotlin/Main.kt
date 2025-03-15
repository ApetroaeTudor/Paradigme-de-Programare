import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import org.jsoup.safety.Safelist
import org.jsoup.select.Elements
import org.yaml.snakeyaml.Yaml
import java.io.File

import org.jsoup.nodes.Element
import javax.print.Doc

fun main() {

    val jsonFile:File=File("file.json")
    val yamlFile:File=File("file.yaml")
    val htmlFile:File=File("file.html")
    val xmlFile:File=File("file.xml")


    var jsonString=jsonFile.reader().readText()
    var yamlString=yamlFile.reader().readText()
    var htmlString=htmlFile.reader().readText()
    var xmlString=xmlFile.reader().readText()

    printXmlHtml(htmlString)


}
