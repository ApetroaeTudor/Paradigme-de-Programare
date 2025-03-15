class JsonParser() : Parser {

    override fun parse(text:String):MutableMap<Any?,Any?>{
        var jsonStr=text.replace("\\s+".toRegex(),"")
        var myMap = mutableMapOf<Any?,Any?>()
        myMap.put(parseReturnPair(jsonStr,0).first,"type:JsonObj")
        return myMap
    }

    override fun print(text:String) {
        val parser:Parser=JsonParser()
        val a = parser.parse(text)
        a.forEach(){ (key,value) ->
            if(key is JsonObj)
                recursivePrintJsonTree(key)
        }
    }

    override fun getResources(text: String, searchKey: String): List<String> {
        val myDataStructure=parse(text).keys.first()
        val returnList:MutableList<String> = mutableListOf()

        fun recursiveSearch(root:JsonObj,){
            root.jsonMap.forEach(){ (key,value) ->

                when(value){
                    is String -> {
                        if(searchKey.toRegex().matches(value)){
                            returnList.add(value)
                        }
                    }
                    is JsonObj -> {
                        recursiveSearch(value,)
                    }
                    is List<*> -> {
                        for(it in value){
                            when(it){
                                is String -> {
                                    if(searchKey.toRegex().matches(it)){
                                        returnList.add(it)
                                    }
                                }
                                is JsonObj -> {
                                    recursiveSearch(it)
                                }
                            }
                        }
                    }
                }
            }
        }

        recursiveSearch(myDataStructure as JsonObj)


        return returnList
    }



    fun parseReturnPair(text:String,position:Int=0):Pair<JsonObj,Int>{ // se presupune ca textul primit nu are whitespaces
        var newNode = JsonObj() //nodul de baza
        var index=position

        text.forEach { ch->
            when(ch){
                '{' -> { //fisierul json incepe cu {
                    index++ //sar peste primul {

                    while(text[index]!='}'){ //citeste caracter cu caracter pana se termina obiectul deschis initial cu {
                        var (key,indx) = parseKey(text,index)
                        index=indx+1 //sar peste :
                        val (value,updatedIndex) = parseValue(text,index)
                        newNode.jsonMap.put(key,value)
                        index=updatedIndex

                        if(text[index]==',') index++
                    }
                    return newNode to index +1 //+1 ca sa sar peste }
                }
                else -> index ++
            }
        }
        return newNode to index
    }


    //nu pot fi accesate pentru ca se va lucra prin interfete


    fun parseKey(text:String,index:Int):Pair<String,Int>{
        val indexFirst=text.indexOf('"',index) +1
        val indexLast=text.indexOf('"',indexFirst)
        return text.substring(indexFirst,indexLast) to indexLast + 1 //aici returnez cheia gasita si un index
        //de la care sa continui parsarea in main parser
    }



    fun parseValue(text: String, position: Int): Pair<Any?, Int> { //perechea e de tip Any pentru ca pot avea mai multe lucruri drept value
        var index = position

        return when {
            text[index] == '"' -> { //value ca string
                val startIndex = index + 1 //+1 ca sa sar peste "
                val endIndex = text.indexOf('"', startIndex)
                text.substring(startIndex, endIndex) to endIndex + 1
            }

            text[index] == '{' -> { //inca un json obj
                parseReturnPair(text, index) //main parse function
            }

            text[index].isDigit() -> {
                var end = index
                while (end < text.length && (text[end].isDigit() || text[end] == '.')) {
                    end++
                }
                text.substring(index, end).toDouble() to end // se returneaza perechea (double,index)
            }

            text[index] == '[' -> {
                index++ //sar peste [

                val list = mutableListOf<Any?>() // voi returna perechea (list,index)
                //lista poate contine elemente de orice fel

                while (index < text.length && text[index] != ']') {
                    val (value, newIndex) = parseValue(text, index) //dau parse separat la toate valorile din lista. Daca se gaseste un jsonObject atunci se va intra pe cazul text[index] == '{' in cadrul apelului recursiv
                    list.add(value)
                    index = newIndex
                    if (text[index] == ',') index++ //sar peste virgula
                }
                index++ //sar peste ]
                list to index //perechea returnata
            }

            text.drop(index).startsWith("true") -> true to index + 4
            text.drop(index).startsWith("false") -> false to index + 5
            text.drop(index).startsWith("null") -> null to index + 4
            else -> throw IllegalArgumentException("token ilegal")
        }
    }
}

