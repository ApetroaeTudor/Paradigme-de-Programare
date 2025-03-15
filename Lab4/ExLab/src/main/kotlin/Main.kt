import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

fun main() {

    val ct1:Content=Content("John","A fost odata ca niciodata","Titluu","Editura A")
    val ct2:Content=Content("Mihai Aurel", "Acest continut nu inseamna nimic","Titlu2","Editura B")

    val bk2:BookWithPrice=BookWithPrice(ct2,120)
    val bk1:Book=Book(ct1)

    val bkSet1:MutableSet<Book> = mutableSetOf()
    bkSet1.add(bk1)
    bkSet1.add(bk2)

    val myLibrary=Library(bkSet1)



    val myHtmlPrinter=HtmlPrinter()
    myHtmlPrinter.printBooks(myLibrary.getBooks())

    val myJsonPrinter=JsonPrinter()
    myJsonPrinter.printBooks(myLibrary.getBooks())

    val myRawPrinter=RawPrinter()
    myRawPrinter.printBooks(myLibrary.getBooks())


}
