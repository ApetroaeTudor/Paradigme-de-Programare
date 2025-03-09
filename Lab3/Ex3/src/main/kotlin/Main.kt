
fun main() {
    val url:String="https://github.com/"
    //val url:String="https://annas-archive.org/"

    try {

        val root=deserializeTree(url)
        serializeTreeToFile(root)

    }
    catch (e:java.io.IOException){
        println("failed to submit the get() request")
    }
    catch (e:Exception){
        println(e.message)
    }














}