
interface RawLibraryPrinter {
    fun printBooks(bookSet:MutableSet<Book>):Unit
}

class RawPrinter : RawLibraryPrinter{
    override fun printBooks(bookSet:MutableSet<Book>):Unit{
        bookSet.forEach(){ book->
            println(book)
        }
    }
}