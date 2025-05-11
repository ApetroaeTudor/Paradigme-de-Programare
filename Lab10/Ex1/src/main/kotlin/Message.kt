package lab.pp

interface Message{
    abstract var nrOfMovesDone:Int
    abstract val primitiveFormat:String

    fun getType():String
    fun getContent():String
    fun getPriority():Int
}



class Request(override val primitiveFormat:String) : Message{

    override var nrOfMovesDone = 0;
    private val type = "request"
    private val priority = primitiveFormat.split(".")[0].toInt()
    private val content = primitiveFormat.split(".")[1]

    override fun getType(): String {
        return this.type;
    }

    override fun getContent(): String {
        return this.content;
    }

    override fun getPriority(): Int {
        return this.priority;
    }
}


class Response(override val primitiveFormat:String) : Message{

    override var nrOfMovesDone = 0;
    private val type = "response"
    private val priority = primitiveFormat.split(".")[0].toInt()
    private val content = primitiveFormat.split(".")[1]

    override fun getType(): String {
        return this.type;
    }

    override fun getContent(): String {
        return this.content;
    }

    override fun getPriority(): Int {
        return this.priority;
    }



}





