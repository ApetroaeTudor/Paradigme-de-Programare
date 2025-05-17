# Laborator PP

## Lab1
**Ex1** - Calculator Java completat cu forma postfixata<br>
**Ex2** - Server local git folosind Docker<br>

## Lab2
**Ex1** - Polyglot GraalVM, Exercitii Laborator + Hash pentru a afisa toate cuvintele cu aceeasi suma de control<br>
**Ex2** - Polyglot GraalVM, citeste un set de date dintr-un fisier, aplica o regresie liniara intr-un script R, genereaza o imagine PNG si o afiseaza<br>
**Ex3** - Polyglot GraalVM, citeste in python 2 nr intregi, nr de repetitii a experientei si nr de succese urmarite. Afiseaza prin R Repartitia binomiala si cdf.<br>  

## Lab3
**LabEx1** - Kotlin: Agenda Telefonica + diagramaUML<br>
**LabEx2** - Kotlin + epublib-core + JSoup: Dictionar cu posibilitatea citirii din fisier epub si optiunea de a alege in ce limba se traduce<br>
**LabEx3** - Kotlin + Kandy: Analizarea frecventelor de caractere/cuvinte. Plotare grafica a frecventelor<br>
**Ex1** - Kotlin + JSoup: Analizarea unui RSS feed. Se extrag titlurile si linkurile corespunzatoare<br>
**Ex2** - Kotlin + epublib-core + JSoup: Deschiderea unui epub si prelucrarea textului din el. Folosind regex se elimina/modifica anumite elemente<br> 
**Ex3** - Kotlin + JSoup: Accesarea unui url. Cu un get request se obtin datele. Se face un arbore cu linkurile care pastreaza acelasi base url<br>

## Lab4
**LabEx** - Kotlin + JSoup + kotlinx-serialization-json: Accesarea si printarea in mai multe feluri a unei biblioteci de carti. Se respecta principiile Single Responsability, Interface segregation si Open/Closed. Se da print la datele despre carti in 3 feluri: Html, Json si .txt<br>
**Ex1** - Kotlin + JSoup + snakeyaml: WebCrawler, poate da parse la fisiere html,xml,yaml si json. Filtreaza datele parsate si stocheaza url-urile, pe care le viziteaza recursiv. Se pot adauga alte chei de cautare si datele se pot salva eventual intr-o baza de date(inca nu fac asta). Se poate alege adancimea crawl-ului.<br> 
**Ex2** - Kotlin: Aplicatie simpla de achizitii/managing bilete. Respecta principiile SOLID. Diagrame UML(Clasa si UseCase) incluse.<br> 
**Ex3** - Kotlin: Aplicatie NoteManager. Are un serviciu simplu de register-login, un meniu ce permite: crearea de note-uri, vizualizarea lor, modificarea si stergerea. Notitele sunt salvate pe disk. Schema UML.<br>

## Lab5
**LabEx1** - Python + tkinter: Aplicatie cu interfata grafica in care introduc niste numere si le filtrez intr-un camp text. Basic error handling<br>
**LabEx2** - Python + PyQt5: Aplicatie jurnal cu interfata grafica. Acces la o baza de date, scriere si citire din ea.<br>
**Ex2** - Python + PyQt5: Joc TicTacToe peer-to-peer. Deschid un server care da manage la datele despre joc si trebuie sa se conecteze 2 jucatori pentru a incepe. Autentificare cu baza de date sqlite. Se tine scorul tot in baza de date.<br>

## Lab6
**LabEx1** - Python: Utilizare super()<br>
**LabEx2** - Python: Method Resolution Order<br>
**LabEx3** - Python: Polimorfism<br>
**LabEx4** - Python: UML + niste clase<br>
**Ex1** - Python: Un script care parcurge un director si in functie de anumite criterii determina felul fisierelor: ASCII, XML, UNICODE, Binary si BMP. Se incarca intr-o lista si se afiseaza cele mai importante date.<br>


## Lab7
**LabEx1** - Kotlin: Parsing de date din journalctl.<br>
**Ex1** - Kotlin: Parsing de date din /var/log/apt/history.log.<br>

## Lab8
**LabEx1** - Kotlin: Lant dublu de responsabilitati.<br>
**LabEx2** - Kotlin: Memento+Observer.<br>
**Ex1** - Kotlin: AND gate cu bridge, builder si FSM.<br>

## Lab9
### Python
**LabEx1** - Factory + Prototype.<br>
**LabEx2** - Pipeline de generatoare.<br>
**Ex1** - Lant de responsabilitati + Command.<br>
**Ex2** - Vending machine cu State machine + Observer.<br>
**Ex3 + Bonus** - Proxy + Command + Strategy. Procesare a cererilor de tip GET, cu proxy pentru caching in forma unor fisiere text. MainApp care implementeaza prin Strategy pattern un algoritm de load balancing bazat pe cuante de timp. Cand se detecteaza intr-o cuanta de timp de 2 ori mai multe requesturi decat in cea anterioara se lanseaza un nou proces care primeste o parte din requesturi.<br>

## Lab10
###  Kotlin:
**LabEx1** - Evitare a race-ului cu mutex. Scriere concurenta pe disc.<br>
**LabEx2** - Implementare semafor pentru acces thread-safe la un fisier.<br>
**Ex1** - Lant de responsabilitati dublu.<br>
**Ex2** - Pipeline pentru procesare ADT.<br>
**Ex3** - Suma a unor nr pentru valori luate dintr-o coada.<br>
**Ex4** - Acces simultan la mai multe fisiere.<br>
**Bonus** - Pipeline pentru descarcarea, parsarea si afisarea unei pagini web<br> 

## Lab11
### Python:
**LabEx1** - Operatii in paralel pe colectii simple.<br>
**LabEx2** - Comunicare intre threaduri cu o coada.<br>
**LabEx3** - Pipeline de procesare a unui ADT cu threaduri si cozi.<br>
**Ex1** - asyncio - Se realizeaza patru sume simultan folosind corutine.<br>
**Ex2** - Se proceseaza comenzi unix de tip pipe folosind pipe-ul din modului subprocessing.<br>
**Ex3** - Implementare a unui ThreadPool care e auto-closable, implementeaza functia map ce primeste mai multe taskuri cu argumente si implementeaza un mecanism de load balancing ce imparte aceste taskuri intre threadurile componente.<br>

## Lab12
### Kotlin:
**ExercitiiLab** - Aplicatii calcul functional pe colectii. Delegates. Secvente. Functii extensie.<br>
**Ex1** - Operatii pe o lista: filter, grupare, map, fold.<br>
**Ex2** - Cifru Caesar pe cuvinte dintr-un fisier.<br>
**Ex3** - Se dau mai multe puncte care trebuie sa formeze un poligon. Ele sunt ordonate in sens trigonometric si se calculeaza perimetrul poligonului.<br>
**Ex4** - Functor pentru prelucrarea unui Map. 2 prelucrari in lant.<br>