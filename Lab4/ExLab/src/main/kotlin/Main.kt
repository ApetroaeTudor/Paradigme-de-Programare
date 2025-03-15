import org.yaml.snakeyaml.Yaml
import java.io.File
import org.yaml.snakeyaml.parser.*

fun main() {

    val jsonFile:File=File("file.json")
    val yamlFile:File=File("file.yaml")

    var jsonString=jsonFile.reader().readText()
    var yamlString=yamlFile.reader().readText()


}
