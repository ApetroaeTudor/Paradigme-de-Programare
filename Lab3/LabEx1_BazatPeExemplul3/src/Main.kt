//implementeaza cautare dupa nume/nr telefon


fun main(){

    val agenda:Agenda=Agenda()
    agenda.addPerson(Contact("Mihai", "0744321987", Birth(1900, 11, 25)))
    agenda.addPerson(Contact("George", "0761332100", Birth(2002, 3, 14)))
    agenda.addPerson(Contact("Liviu" , "0231450211", Birth(1999, 7, 30)))
    agenda.addPerson(Contact("Popescu", "0211342787", Birth(1955, 5, 12)))
    agenda.printContacts()

    println("Agenda dupa eliminare contact [George]:")
    try {
        agenda.removeAtIndex(1)
    }
    catch (e:Exception){
        println(e.toString())
    }
    agenda.printContacts()

    println("Agenda dupa eliminare contact [Liviu]:")
    try{
        agenda.removeByName("Liviu")
    }
    catch(e:Exception){
        println(e.toString())
    }
    agenda.printContacts()

    println("Cautare dupa nr de telefon: ")
    try {
        val nume: String = agenda.findPersonByPhoneNumber("0211342787").Name
        agenda.updatePhoneNumber("0218606591",nume)
        agenda.findPersonByName(nume).Print()
    }
    catch (e:Exception){
        println(e.toString())
    }
}

