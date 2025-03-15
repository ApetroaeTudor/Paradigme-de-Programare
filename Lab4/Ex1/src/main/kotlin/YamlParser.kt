import org.yaml.snakeyaml.Yaml

class YamlParser : Parser {

    override fun parse(text:String):MutableMap<Any?,Any?>{
        val myYamlParser=Yaml()
        return myYamlParser.load(text)
    }
}



fun printYamlFromString(text:String){
    val myParser:YamlParser = YamlParser()
    val textToParse=myParser.parse(text)

    fun recursivePrint(myMap:Map<Any?,Any?>,depth:Int=0){
        myMap.forEach(){ (key,value)->
            print("\t".repeat(depth)+key+": ")
            when(value){
                is List<*>->{
                    value.forEach(){ listElem->
                        when(listElem){
                            is Map<*,*> -> {
                                println()
                                recursivePrint(listElem as Map<Any?,Any?>,depth+1)
                            }
                            else -> print(listElem.toString()+" ")
                        }
                    }
                    println()
                }
                is Map<*,*>->{
                    println()
                    recursivePrint(value as Map<Any?, Any?>, depth+1)
                }
                else-> println(value.toString())
            }
        }
    }

    recursivePrint(textToParse,0)

}
