
class Tag(var name:String="", var depth:Int=0) {

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


            if(parentDepth==0){
                val children = tagsByDepth[parentDepth + 1] ?: emptyList()

                treeAsTagList.forEach { currentTag->
                    if(currentTag.name.compareTo(url)==0){
                        children.forEach{ child->
                            currentTag.childList.add(child)
                        }
                    }
                }
            }

            val parents = tagsByDepth[parentDepth] ?: return



            if(parentDepth==1){
                parents.forEach{ parent->
                    parent.parentTag=Tag(url,0)
                }
            }


            val children = tagsByDepth[parentDepth + 1] ?: emptyList()


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


fun makeTagList(list:List<String>,url:String=""):ArrayList<Tag>{
    val depthRegex="/"
    val tagList:ArrayList<Tag> = ArrayList<Tag>()
    list.forEach{
        when (depthRegex.toRegex().findAll(it).count()){
            1->tagList.add(Tag(it,1))
            2->tagList.add(Tag(it,2))
            3->tagList.add(Tag(it,3))
            4->tagList.add(Tag(it,4))

        }
    }
    tagList.add(Tag(url,0))
    return tagList
}



fun deserializeTree(url:String):Tag{
    val finalRefs:List<String> = parseFile(url)
    val tagList=makeTagList(finalRefs,url)

    Tag.linkChildrenByDepth(0,tagList,url)
    Tag.linkChildrenByDepth(1,tagList,url)
    Tag.linkChildrenByDepth(2,tagList,url)


    tagList.sortBy { it.depth } //primul element e capul arborelui, se pot accesa toate elementele de la el

//    tagList.forEach {
//        it.printTagWithChildrenAndParent()
//    }
//
    fun recursiveTraverse(root:Tag,dep:Int=0) {

        println("     ".repeat(dep)+root.name)
        root.childList.forEach { recursiveTraverse(it,dep+1) }
    }
    recursiveTraverse(tagList[0])


    return tagList[0]
}


fun serializeTreeToFile(root:Tag){

    fun recursiveAppendToBuffer(root:Tag, currentPath:StringBuilder=StringBuilder(""),buffer:StringBuilder=StringBuilder("")){
        buffer.append("$currentPath: ")

        root.childList.forEach {
            buffer.append(it.name+", ")
        }
        buffer.append("\n")

        root.childList.forEach {

            recursiveAppendToBuffer(it,StringBuilder("$currentPath${it.name}"),buffer)
        }

    }
    val finalBuffer:StringBuilder= StringBuilder()
    recursiveAppendToBuffer(root,StringBuilder(root.name),finalBuffer)

    println(finalBuffer)
}


