
fun main() {
    val fileName = "CrimeAndPunishment.epub"
    val fileHtmlName="intermediaryHtml.txt"
    val fileIntermediateStory="intermediaryStory.txt"
    val fileFinalStory="finalStory.txt"

    val fileBackup="backupStory.txt"

    val multipleWhitespaceRegex="[ ]{2,}"
    val whitespaceAfterNewline="\\n[ ]+"
    val multipleNewlineRegex="\\n{2,}"
    val contentsRegex="(?s)[A-ZĂÂÎŞŢ]{3,10}.*?(?=\\n[A-ZĂÂÎŞŢ ]+[ .])" // verifica daca incepe cu ceva in caps CONTENTS sau CAPITOLE, dupa care optional verifica daca pe urmatoarea linie e ceva din mai multe litere de tipul CONTENT
    val chapterRegex="(?s)[IVX]{1,10}?.*?" // face ca .* sa trateze si \n
    val numberLineRegex="(?m)^\\s*\\d+\\s*$" //multiline ca ^ si $ sa se aplice pe fiecare linie

    val authorNameRegex="[A-Z]{1}[a-z]{2,10}\\b(?:\\s+[A-Z]{1}[a-z]{2,10})?" //daca am un cuvant care incepe in CAPS dupa care dupa un separator de cuvant am optional alt cuvant

    writeToIntermediaryHtml(fileHtmlName,fileName)
    writeToIntermediaryStory(fileFinalStory,fileName,fileBackup)

    eliminateByRegex(fileFinalStory,multipleWhitespaceRegex,"")
    eliminateByRegex(fileFinalStory,whitespaceAfterNewline,"")
    eliminateByRegex(fileFinalStory,contentsRegex,"")
    eliminateByRegex(fileFinalStory,chapterRegex,"")
    eliminateByRegex(fileFinalStory,numberLineRegex,"")

    eliminateByRegex(fileFinalStory,multipleNewlineRegex,"\n")

    replaceRomanianCharacters(fileFinalStory)


    replaceAuthorName(fileFinalStory,authorNameRegex,"[XXXXX]")
    
}