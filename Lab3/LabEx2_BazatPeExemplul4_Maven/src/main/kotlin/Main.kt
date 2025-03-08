import java.nio.file.Paths

/**
 * @DeImplementat
 * 1. Adaugare de cuvinte in dictionar (x)
 * 2. Salvarea intr-un fisier a povestii traduse (x)
 * 3. Initializarea dictionarului prin citirea din alt fisier
 * 4. Extragerea unui dictionar dintr-un fisier ebook (*)
 */
fun main(args : Array<String>){

    val DICTIONAR:Dictionar = Dictionar(5)
    try {
        DICTIONAR.initDictionaryFromAFile("sourceText")
    }
    catch (e:Exception){
        println(e.toString())
    }

    val Poveste = "Once upon a time there was an old woman who loved baking gingerbread. She would bake gingerbread cookies, cakes, houses and gingerbread people, all decorated with chocolate and peppermint, caramel candies and colored ingredients."

    try {
        FileManaging.printStringToAFile(
            "TranslatedStory",
            DICTIONAR.translateText(FileManaging.readTextFromEpub("PovesteOriginal.epub"))
        )
    }
    catch (e:Exception){
        println(e.toString())
    }

}