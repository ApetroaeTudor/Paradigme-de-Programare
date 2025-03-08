//utilizam File din Java.io pentru a deschide fisierul text
import org.jetbrains.kotlinx.dataframe.api.add
import org.jetbrains.kotlinx.dataframe.api.concat
import java.io.File
import java.util.*

import org.jetbrains.kotlinx.dataframe.api.dataFrameOf
import org.jetbrains.kotlinx.kandy.dsl.categorical
import org.jetbrains.kotlinx.kandy.dsl.plot
import org.jetbrains.kotlinx.kandy.letsplot.export.save
import org.jetbrains.kotlinx.kandy.letsplot.feature.layout
import org.jetbrains.kotlinx.kandy.letsplot.layers.*
import org.jetbrains.kotlinx.kandy.util.color.Color

import org.jetbrains.kotlinx.*


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

fun SortByHitCount(items : MutableMap<Char, Int>, how: Boolean) : Map<Char,Int>{ //how==false -> descrescator
    //functia de sortare a caracterelor, dupa valoare (frecventa), atat crescator cat si descrescator, in functie de how

    val result:Map<Char,Int>
    when(how){
        false->result= items.toList().sortedBy { (_,freq) -> freq }.toMap()
        true->result= items.toList().sortedBy { (_,freq) -> -freq }.toMap()
    }
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

    val UniqueWords=GetUniqueWordCount(trim_words)
    val SortedUniqueWordsByFrequencyAscending= UniqueWords.toList().sortedBy { (_,freq) -> freq }.toMap()
    val SortedUniqueWordsByFrequencyDescending= UniqueWords.toList().sortedBy { (_,freq)-> -freq }.toMap()

    val UniqueChars=GetUniqueCharCount(trim_words)
    val UniqueCharsSortedByFrequencyAscending= SortByHitCount(UniqueChars,false)
    val UniqueCharsSortedByFrequencyDescending= SortByHitCount(UniqueChars,true)

    println(SortedUniqueWordsByFrequencyAscending)
    println(SortedUniqueWordsByFrequencyDescending)
    println()
    println(UniqueCharsSortedByFrequencyAscending)
    println(UniqueCharsSortedByFrequencyDescending)

    val averageCharFreq = dataFrameOf(
        "CharactersAscending" to UniqueCharsSortedByFrequencyAscending.keys.toList(),
        "AverageFrequencyAscending" to UniqueCharsSortedByFrequencyAscending.values.toList(),

        "CharactersDescending" to UniqueCharsSortedByFrequencyDescending.keys.toList().reversed(),
        "AverageFrequencyDescending" to UniqueCharsSortedByFrequencyDescending.values.toList()
    )

//    val dfAscending = dataFrameOf(
//        "Character" to UniqueCharsSortedByFrequencyAscending.keys.toList(),
//        "Frequency" to UniqueCharsSortedByFrequencyAscending.values.toList()
//    ).add("Order") { "Ascending" } // Add a grouping column
//
//    val dfDescending = dataFrameOf(
//        "Character" to UniqueCharsSortedByFrequencyDescending.keys.toList().reversed(),
//        "Frequency" to UniqueCharsSortedByFrequencyDescending.values.toList()
//    ).add("Order") { "Descending" } // Add a grouping column

// Combine into a single DataFrame
    //val combinedDf = dfAscending.concat(dfDescending)

   averageCharFreq.plot {
       points {
           x("CharactersDescending")
           y("AverageFrequencyDescending")
           color= Color.BLUE

       }
       points {
           x("CharactersAscending")
           y("AverageFrequencyAscending")
           color=Color.RED
       }

   }.save("CharacterFreqAscendingDescending-Points.png")




}
