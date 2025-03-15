import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

interface JsonLibraryPrinter{
    fun printBooks(bookSet:MutableSet<Book>):Unit
}

class JsonPrinter() : JsonLibraryPrinter{
    override fun printBooks(bookSet: MutableSet<Book>) {
        var myMap:MutableMap<String,String>
        var myJson:String
        bookSet.forEach(){ book ->
            myMap=book.getAttributesAsMap()
            myJson= Json.encodeToString(myMap)
            println(myJson)
            println()
        }
    }
}