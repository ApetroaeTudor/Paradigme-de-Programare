class Birth(val year: Int, val Month: Int, val Day: Int) {
    override fun toString(): String
        = "($Day.$Month.$year)"

    fun checkEquality(b: Birth): Boolean
        = (this.year == b.year && this.Month == b.Month && this.Day == b.Day)
}

class Contact(val Name: String, var Phone: String, val BirthDate: Birth){

    override fun toString():String
        = "Nume: $Name, Nr Telefon: $Phone, DataNastere: $BirthDate"

    fun Print()
        = println("Name: $Name, Mobile: $Phone, Date: $BirthDate")

    fun checkEquality(c:Contact):Boolean
        = this.Name.compareTo(c.Name)==0 && this.Phone.compareTo(c.Phone)==0 && this.BirthDate.checkEquality(c.BirthDate)

}

class Agenda(val agenda: MutableList<Contact> = mutableListOf<Contact>(), var nrOfMembers:Int=0){

    fun addPerson(c:Contact):Unit{
        agenda.add(c)
        nrOfMembers++
    }

    fun removePerson(c:Contact):Unit{
        for (person in agenda){
            if(person.checkEquality(c)){
                agenda.remove(c)
                nrOfMembers--
            }
        }
        throw Exception("Didn't find element!!")
    }

    fun updatePhoneNumber(phoneNr:String,name:String){
        val phoneNrRegex:Regex="^(07|02)\\d{8}$".toRegex()

        if(!phoneNr.matches(phoneNrRegex)) {
            throw Exception("Invalid phone nr!!")
        }

        var foundPerson:Contact = this.findPersonByName(name)
        foundPerson.Phone=phoneNr

    }

    fun findPersonByName(name:String):Contact{
        for(person in agenda){
            if(person.Name.compareTo(name)==0){
                return person;
            }
        }
        throw Exception("There is no person with that name!")
    }

    fun findPersonByPhoneNumber(phone:String):Contact{
        for(person in agenda){
            if(person.Phone.compareTo(phone)==0){
                return person;
            }
        }
        throw Exception("There is no person with that phone number!")
    }

    fun givePersonIndexByName(name:String):Int{
        for((index,person) in agenda.withIndex()){
            if(person.Name.compareTo(name)==0){
                return index
            }
        }
        throw Exception("There is no person with that name!")
    }

    fun printContacts():Unit{
        println()
        for(person in agenda){
            println("$person")
        }
        println()
    }

    fun removeAtIndex(index:Int=-1):Unit{
        if( index<0 || index > nrOfMembers ){
            throw Exception("invalid params given!")
        }

        val temp:Contact = agenda.removeAt(index)
        println("Removed ${temp.Name} successfully")
    }

    fun removeByName(name:String):Unit{
        val index:Int=this.givePersonIndexByName(name)
        val temp:Contact=this.findPersonByName(name)
        this.removeAtIndex(index)
        println("Successfully removed $name")
    }





}

