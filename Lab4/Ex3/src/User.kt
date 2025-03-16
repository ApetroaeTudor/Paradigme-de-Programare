import java.io.File
import java.nio.file.Files
import kotlin.io.path.Path

class User {
    private val myDisplayer:WelcomeScreenPrinter=WelcomePrinter()
    private val loginFile=File("loginFile")
    init{
        if(!loginFile.exists()){
            Files.createFile(Path("loginFile"))
        }
    }

    fun start(){
        myDisplayer.welcomeScreen()

        do{
            var userInput:Int= readlnOrNull()?.toIntOrNull()?:throw Exception("Invalid Index")

            when(userInput){
                1->{
                    println("\nAttempting Log-In:")
                    println("Username: ")
                    val username:String= readlnOrNull()?:"InvalidUser"
                    println("Password: ")
                    val password:String= readlnOrNull()?:"InvalidPassword"
                    if(!login(username,password)){
                        println("Wrong User or Password. Try again!")
                    }
                    else{
                        userInput=4
                    }
                    myDisplayer.welcomeScreen()


                }
                2->{
                    println("\nRegister: ")
                    println("UserName: ")
                    val username:String= readlnOrNull()?:"InvalidUser"
                    println("Password: ")
                    val password:String= readlnOrNull()?:"InvalidPassword"
                    registerUser(username,password)

                    myDisplayer.welcomeScreen()


                }
                3->{
                    throw Exception("exiting..")
                }
            }

        }while (userInput!=4)



    }

    fun registerUser(user:String,password:String){
        var loginData=loginFile.readText()
        if(loginData.contains("$user:$password")){
            println("User already exists!")
        }
        else{
            loginFile.writeText("$loginData$user:$password\n")
        }
    }

    fun login(user:String,password:String):Boolean{
        val loginData=loginFile.readText()
        return loginData.contains("$user:$password")
    }

}

class WelcomePrinter() : WelcomeScreenPrinter {
    override fun welcomeScreen(){
        println("WELCOME! Please select a choice:\n" +
                "    ---- 1 ---- Log-In\n" +
                "    ---- 2 ---- Register\n" +
                "    ---- 3 ---- Exit")
    }
}