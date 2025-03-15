import java.io.File

fun main() {

    val jsonFile:File=File("file.json")

    var jsonString=jsonFile.reader().readText()

    jsonString=jsonString.replace("\\s+".toRegex(),"")
    println(jsonString)

    val parser=JsonParser()
    val a = parser.parse(jsonString).first

    recursivePrintJsonTree(a)
}
