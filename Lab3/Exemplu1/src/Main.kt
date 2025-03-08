fun printAllRegexMatches(regex: Regex, searchString: String) {
    for(item in regex.findAll(searchString)) {
        println(item.value)
    }
    println("-".repeat(100))
}

fun main() {
    val testString = "link/ether a0:b1:c2:d3:e4:f5 brd ff:ff:ff:ff:ff:ff\n" +
            "inet 192.168.0.2/24 brd 192.168.0.255 scope global eno1\n" +
            "Hi,\n You can contact me at john.smith@gmail.com\n" +
            "You should use a search engine like www.duckduckgo.com\n" +
            "I'll meet you at 08:00 AM tomorrow"


    val stringWithDuplicates = "one two two three three three four four four four"

    val ipRegex = Regex("((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" )
    val emailRegex = Regex("\\w+[+.\\w-]*@([\\w-]+.)*\\w+[\\w-]*.([a-z]{2,4}|\\d+)")

    val urlRegex = Regex("(https?:\\/\\/)?www\\.[-a-zA-Z0-9@:%._\\+~#=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&//=]*)")

    val timeRegex = Regex("(0?[1-9]|1[0-2]):[0-5][0-9]")
    val duplicatesRegex = Regex("(\\b\\w+\\b)(?=.*\\b\\1\\b)")

    // Find all matches
    for(regex in listOf(ipRegex, emailRegex, urlRegex, timeRegex)) {
        printAllRegexMatches(regex, testString)
    }

    // Match string:
    println("'08:00' matchEntire: ${timeRegex.matchEntire("08:00")?.value.orEmpty()}")
    println("'Tomorrow at 09:15' matchEntire: ${timeRegex.matchEntire("Tomorrow at 09:15")?.value.orEmpty()}")
    println("'Tomorrow at 09:16' matches: ${timeRegex.matches("Tomorrow at 09:16")}")
    println("'Tomorrow at 09:17' containsMatchIn: ${timeRegex.containsMatchIn("Tomorrow at 09:17")}")

    // Remove duplicates:
    println("Without duplicates: ${duplicatesRegex.replace(stringWithDuplicates, "")}")

    // Find first match:
    println("First duplicate: ${duplicatesRegex.find(stringWithDuplicates)?.value.orEmpty()}")

    // Split by regex:
    println("Regex split: ${Regex("\\d+").split("This10text20is30splitted40by50regex")}")
}