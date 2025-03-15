class Library(private val books:MutableSet<Book> = mutableSetOf()) {
    fun getBooks():MutableSet<Book>{
        return this.books
    }
    fun addBook(book:Book){
        books.add(book)
    }

    fun findAllByAuthor(author:String):MutableSet<Book>{
        val mySet:MutableSet<Book> = mutableSetOf()
        books.forEach(){ book->
            if(book.getAuthor().compareTo(author)==0){
                mySet.add(book)
            }
        }
        return mySet
    }

    fun findAllByName(name:String):MutableSet<Book>{
        val mySet:MutableSet<Book> = mutableSetOf()
        books.forEach(){ book ->
            if(book.getName().compareTo(name)==0){
                mySet.add(book)
            }
        }
        return mySet
    }

    fun findAllByPublisher(publisher:String):MutableSet<Book>{
        val mySet:MutableSet<Book> = mutableSetOf()
        books.forEach(){ book ->
            if(book.getPublisher().compareTo(publisher)==0){
                mySet.add(book)
            }
        }
        return mySet
    }

    

}