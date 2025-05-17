package lab.pp

val myTestMap:MutableMap<Int,String> = mutableMapOf(1 to "hey", 2 to "hello from map", 3 to "third key")


fun appendTest(source:String ):String{
    return "${source} Test"
}

fun String.toPascalCase() : String{
    val components = this.split(" ")
    var result = StringBuilder("")
    components.forEach { component->
        result.append(component.replaceFirstChar { it.uppercase() })
    }
    return result.toString()
}

class MapFunctor(val value: MutableMap<Int,String>){
    fun map1(function: (String) -> String):MapFunctor{
        value.forEach{ elem->
            value.put(elem.key,function(elem.value))
        }
        return MapFunctor(value)
    }
    fun map2():MapFunctor{
        value.forEach(){ elem->
            value.put(elem.key,elem.value.toPascalCase())
        }
        return MapFunctor(value)
    }
}

fun main(){
    println(MapFunctor(myTestMap).map1(::appendTest).value)
    println(MapFunctor(myTestMap).map1(::appendTest).map2().value)

}