import com.sun.org.apache.xerces.internal.dom.ParentNode
import org.jsoup.Jsoup
import java.security.InvalidKeyException

class Tag(var name:String="",var depth:Int=0) {

    var childList: ArrayList<Tag> = ArrayList<Tag>()
    var parentTag: Tag= this


    override fun toString(): String {
        return "$name: $depth"
    }



    companion object {


        fun linkChildrenByDepth(parentDepth: Int, treeAsTagList: ArrayList<Tag>,url:String="") {
            if (parentDepth < 0) throw Exception("Invalid depth!")


            val tagsByDepth = treeAsTagList.groupBy { tag ->
                tag.name.count { it == '/' }
            }



            val parents = tagsByDepth[parentDepth] ?: return
            if(parentDepth==1){
                parents.forEach{ parent->
                    parent.parentTag=Tag(url,0)
                }
            }


            val children = tagsByDepth[parentDepth + 1] ?: emptyList()
            if(parentDepth==0) {
                parents.forEach{ parent->
                    children.forEach{ child->
                        parent.childList.add(child)
                    }
                }
            }


            parents.forEach { parent ->
                children.forEach{ child->
                    if(child.name.contains(parent.name.toRegex())){
                        parent.childList.add(child)
                        child.parentTag=parent
                    }
                }
            }

        }

    }

    fun printTagWithChildrenAndParent() {
        println(this.toString())
        println("Parent: "+ this.parentTag)
        println("Children: " + this.childList)
        println()
        println()
    }

}



fun parseFile(url:String):List<String>{

        val elemsElements = Jsoup.connect(url).get().select("a")
        val httpRegex="^https?.*$"
        var refs=ArrayList<String>()
        for(elem in elemsElements){
            refs.add(elem.attr("href"))
        }
        val removeElems=ArrayList<String>()

        for (elem in refs){
            if(httpRegex.toRegex().matches(elem)){
                removeElems.add(elem)
            }

        }

        for (it in removeElems){
            refs.remove(it)
        }

        refs.removeIf { it=="/" }
        refs.removeIf{ it=="#"}
        return refs.distinct()
}

fun makeTagList(list:List<String>,url:String=""):ArrayList<Tag>{
    val depthRegex="/"
    val tagList:ArrayList<Tag> = ArrayList<Tag>()
    list.forEach{
        when (depthRegex.toRegex().findAll(it).count()){
            1->tagList.add(Tag(it,1))
            2->tagList.add(Tag(it,2))
            3->tagList.add(Tag(it,3))
        }
    }
    tagList.add(Tag(url,0))
    return tagList
}



