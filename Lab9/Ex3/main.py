import Requests as r
import sys
# urls_to_test = ["https://httpbin.org/get","https://catfact.ninja/fact"]


if __name__ == '__main__':
    urls_to_test = []
    for i in range(0,len(sys.argv)):
        if i != 0:
            urls_to_test.append(sys.argv[i])
    
    print("\033[1m\nInitial se apeleaza functia Proxy.read() care verifica existenta in cache, daca nu exista atunci prin RealSubject se fac cererile\n\033[0m")
    r.time.sleep(0.5)

    proxy = r.Proxy()
    
    for url in urls_to_test:
        proxy.read_entry(url)
    

    print("\033[1m\n\nS-au facut cererile initiale, acum se asteapa 2 secunde si se incearca o citire noua din cache. Pentru ca sunt recente, cererile nu se refac\n\n\033[0m")
    r.time.sleep(2)

    for url in urls_to_test:
        proxy.read_entry(url)

    print("\033[1m\n\nAcum se asteapta 5 secunde, cererile sunt considerate invechite, si se fac iar requesturi. Se actualizeaza fisierele din cache cu noi timestamp-uri\n\n\033[0m")
    r.time.sleep(5)

    for url in urls_to_test:
        print()
        proxy.read_entry(url)
        
    print("\033[1m\n\n\nFINALIZARE MAIN.PY\n\n\n\033[0m")
