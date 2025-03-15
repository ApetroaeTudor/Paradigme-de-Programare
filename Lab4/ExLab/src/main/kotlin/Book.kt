open class Book(private val data:Content) {
    override fun toString(): String {
        var buffer:StringBuilder= StringBuilder("")
        buffer.append("Book info: \n")
        buffer.append("Author: "+data.getAuthor()+"\n")
        buffer.append("Text: "+data.getText()+"\n")
        buffer.append("Name: "+data.getName()+"\n")
        buffer.append("Publisher: "+data.getPublisher()+"\n")
        return buffer.toString()
    }

    fun getName():String{
        return data.getName()
    }
    fun getAuthor():String{
        return data.getAuthor()
    }
    fun getPublisher():String{
        return data.getPublisher()
    }
    fun getContent():String{
        return data.getText()
    }
    fun hasAuthor():Boolean{
        return data.getAuthor().isNotBlank()
    }
    fun hasTitle():Boolean{
        return data.getName().isNotBlank()
    }
    fun isPublishedBy(publisher:String):Boolean{
        return data.getPublisher().compareTo(publisher)==0
    }

    open fun getAttributesAsMap():MutableMap<String,String>{
        val myMap:MutableMap<String,String> = mutableMapOf()
        myMap.put("titlu",data.getName()) //titlu //head
        myMap.put("autor",data.getAuthor()) //autor //head
        myMap.put("publisher",data.getPublisher()) //publisher //head
        myMap.put("text",data.getText()) //in body
        return myMap
    }

}


class BookWithPrice(private val data:Content, private val price:Int) : Book(data) {
    override fun getAttributesAsMap():MutableMap<String,String>{
        val myMap:MutableMap<String,String> = mutableMapOf()
        myMap.put("titlu",data.getName()) //titlu //head
        myMap.put("autor",data.getAuthor()) //autor //head
        myMap.put("publisher",data.getPublisher()) //publisher //head
        myMap.put("price",price.toString()) //head

        myMap.put("text",data.getText()) //in body
        return myMap
    }
}