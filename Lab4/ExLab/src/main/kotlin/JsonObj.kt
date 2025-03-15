class JsonObj(val jsonMap: MutableMap<String, Any?> = mutableMapOf()) {
    //acel any poate fi in principiu orice valoare o poate referi o cheie in formatul json
    //deci: String, Numar(int double etc), boolean, null, JsonObj si un Array
    //acel Array poate fi la randul lui cu elemente de tipurile enuntate anterior
    //voi folosi List<> pentru arrays

    //structura va fi arborescenta

    fun addJsonObj(key:String,value:Any?):JsonObj{ //poate fac verificari si exceptii mai tarziu
        val insertedObj = JsonObj()
        this.jsonMap.put(key,value)
        return insertedObj
    }

    fun getJsonObj(key:String):Any?{
        return jsonMap.get(key)
    }

    fun hasKey(key:String):Boolean{
        return jsonMap.containsKey(key)
    }


}



fun recursivePrintJsonTree(root:JsonObj,depth:Int=0){
    root.jsonMap.forEach(){ (key,value) ->
        print("\t".repeat(depth)+"\"$key\": ")

        when(value){
            is String -> println("\"$value\"")
            is Number, null,is Boolean -> println(value)
            is JsonObj -> {
                println()
                recursivePrintJsonTree(value,depth+1)
            }
            is List<*> -> {
                for(it in value){
                    when(it){
                        is String -> print("\"$it\" ")
                        is Number,null,Boolean -> print(it.toString()+ " ")
                        is JsonObj -> {
                            println()
                            recursivePrintJsonTree(it,depth+1)
                        }
                    }
                }
                println()
            }
        }
    }
}

















