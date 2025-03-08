//utilizam File din Java.io pentru a deschide fisierul text
import java.io.File
import java.util.*

fun GetUniqueWordCount(all_words : List<String>) : MutableMap<String, Int> {
    //functia pentru calculul cuvintelor unice
    val result = mutableMapOf<String, Int>()
    all_words.forEach {
        if(!result.containsKey(it)){
            result.put(it,1);
        }
        else{
            val freq=result.get(it)
            if (freq != null) result.put(it,freq+1)

        }
    }
    return result
}

fun GetUniqueCharCount(all_chars : List<String>) : MutableMap<Char, Int> {
    //functia pentru calculul caracterelor unice
    val result = mutableMapOf<Char, Int>()
    all_chars.forEach{
        it.forEach {
            if(!result.containsKey(it)){
                result.put(it,1)
            }
            else{
                val freq=result.get(it)
                if(freq!=null) result.put(it,freq+1)
            }
        }
    }
    return result
}

fun SortByHitCount(items : MutableMap<Char, Int>, how: Boolean) : MutableMap<Int, Char>{
    //functia de sortare a caracterelor, dupa valoare (frecventa), atat crescator cat si descrescator, in functie de how
    val result = mutableMapOf<Int, Char>()
    return result
}





//functia main()
fun main(args : Array<String>){
    //citim liniile din fisier
    val lines = File("Fisier.txt").reader().readText()
    //construim un array de cuvinte, seprand prin spatiu
    val words = lines.split(" ")

    //eliminam semnele de punctuatie de pe marginile cuvintelor
    val trim_words = mutableListOf<String>()

    words.forEach {
        val filter = it.trim(',','.','"','?', '!')
        trim_words += filter.lowercase(Locale.getDefault())
        print(filter + " ")
    }
    println("\n") //trim_words contine cuvintele

    //construim o lista cu toate caracterele folosite 'A..Z'
    val chars = mutableListOf<String>()
    trim_words.forEach {
        for (c in it){
            if (c in 'a'..'z' || c in 'A'..'Z') {
                chars += c.uppercaseChar().toString()
                print(c.uppercaseChar())
            }
        }
    }
    println("\n")

    //Pentru constructia histogramelor, R foloseste un mecanism prin care asociaza caracterelor unice, numarul total de aparitii (frecventa)
    // 1. Construiti in Kotlin acelasi mecanism de masurare a frecventei elementelor unice si afisati cuvintele unice din trim_words (x)

    // 2. Construiti in Kotlin acelasi mecanism de masurare a frecventei elementelor unice si afisati caracterele unice din chars (x)

    // 3. Pentru frecventele caracterelor unice calculate anterior
    //      A. Afisati perechile (frecventa -> Caracter) sortate crescator si descrescator (x)
    //      B. afisati graficele variatiei de frecventa sortate anterior crescator si descrescator si concatenati-le intr-un grafic de puncte

    //construim histograma pentru cuvinte
    //RHistogram.BuildHistogram(trim_words.toTypedArray(), "Words", true)
    //construim histograma pentru caractere
    //RHistogram.BuildHistogram(chars.toTypedArray(), "Chars", true)

    val UniqueWords=GetUniqueWordCount(trim_words)
    val SortedUniqueWordsByFrequencyAscending= UniqueWords.toList().sortedBy { (_,freq) -> freq }.toMap()
    val SortedUniqueWordsByFrequencyDescending= UniqueWords.toList().sortedBy { (_,freq)-> -freq }.toMap()

    val UniqueChars=GetUniqueCharCount(trim_words)
    val UniqueCharsSortedByFrequencyAscending= UniqueChars.toList().sortedBy { (_,freq) -> freq }.toMap()
    val UniqueCharsSortedByFrequencyDescending= UniqueChars.toList().sortedBy { (_,freq) -> -freq }.toMap()
    println(SortedUniqueWordsByFrequencyAscending)
    println(SortedUniqueWordsByFrequencyDescending)
    println()
    println(UniqueCharsSortedByFrequencyAscending)
    println(UniqueCharsSortedByFrequencyDescending)
}
