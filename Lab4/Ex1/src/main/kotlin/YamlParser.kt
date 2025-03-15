import org.yaml.snakeyaml.Yaml

class YamlParser : Parser {

    override fun parse(text: String): MutableMap<Any?, Any?> {
        val myYamlParser = Yaml()
        val myMap: MutableMap<Any?, Any?> = mutableMapOf()
        myMap.put(myYamlParser.load(text), "Type:Java Mutable HashMap")
        return myMap
    }

    override fun print(text: String) {
        val myParser:YamlParser = YamlParser()
        val myDataStructure=myParser.parse(text).keys.first()

        fun recursivePrint(myMap:Map<Any?,Any?>,depth:Int=0){
            myMap.forEach(){ (key,value)->
                kotlin.io.print("\t".repeat(depth) + key + ": ")
                when(value){
                    is List<*>->{
                        value.forEach(){ listElem->
                            when(listElem){
                                is Map<*,*> -> {
                                    println()
                                    recursivePrint(listElem as Map<Any?,Any?>,depth+1)
                                }
                                else -> kotlin.io.print(listElem.toString() + " ")
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

        recursivePrint(myDataStructure as Map<Any?,Any?>,0)
    }










    override fun getResources(text: String, searchKey: String): List<String> {
        val myDataStructure = parse(text).keys.first()
        var returnList: MutableList<String> = mutableListOf()


        fun recursiveSearch(myMap: Map<Any?, Any?>) {
            myMap.forEach() { (key, value) ->
                when (value) {
                    is List<*> -> {
                        value.forEach() { listElem ->
                            when (listElem) {
                                is Map<*, *> -> {
                                    recursiveSearch(listElem as Map<Any?, Any?>)
                                }

                                else -> {
                                    if (listElem.toString().matches(searchKey.toRegex())) {
                                        returnList.add(listElem.toString())
                                    }
                                }
                            }
                        }
                        println()
                    }

                    is Map<*, *> -> {
                        recursiveSearch(value as Map<Any?, Any?>)
                    }

                    else -> {
                        if (value.toString().matches(searchKey.toRegex())) {
                            returnList.add(value.toString())
                        }
                    }
                }
            }

        }

        recursiveSearch(myDataStructure as Map<Any?, Any?>)

        return returnList
    }
}
