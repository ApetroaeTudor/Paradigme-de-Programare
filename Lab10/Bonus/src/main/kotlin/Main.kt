package lab.pp

import kotlinx.coroutines.*
import kotlinx.coroutines.channels.ReceiveChannel
import kotlinx.coroutines.channels.produce
import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import org.jsoup.nodes.Element

val webURL = "https://github.com/"

fun printElemTree(element:Element,indent:String=""){
    println("$indent<${element.tagName()}>")
    //tag name

    for(attr in element.attributes()){
        println("$indent [${attr.key} = ${attr.value}]")
    }
    //attributes - key-val

    if(element.ownText().isNotBlank()){
        println("$indent  Text: ${element.ownText()}")
    }
    //daca are text il printez

    for(child in element.children()){
        printElemTree(child,"$indent ")
    }

    //se inchide tagul
    println("$indent </${element.tagName()}>")
}


fun CoroutineScope.WebPageDownloader() = produce {
    println("Job: Download done on thread: ${Thread.currentThread().name}")
    send(Jsoup.connect(webURL).get().html())
    close()
    //se trimite un Jsoup Document
}

fun CoroutineScope.DOMTreeParser(DOMTree:ReceiveChannel<String>) = produce {
    println("Job: Parse done on thread: ${Thread.currentThread().name}")
    for(elem in DOMTree){
        send(Jsoup.parse(elem))
    }
    close()
}

fun CoroutineScope.DOMTreePrinter(DOMTreeParsed:ReceiveChannel<Document>){
    launch {
        println("Job:Print done on thread: ${Thread.currentThread().name}")
        for(elem in DOMTreeParsed){
            //apel recursiv pentru fiecare element din Jsoup.Document

            //tag name - atribute - text - recursive(children)
            printElemTree(elem)
        }
    }
}

fun main() = runBlocking {
    val job1 = launch(newFixedThreadPoolContext(3,"myCtx")) {
        val channel = WebPageDownloader()
        val channel1 = DOMTreeParser(channel)
        DOMTreePrinter(channel1)
    }

    job1.join()
}