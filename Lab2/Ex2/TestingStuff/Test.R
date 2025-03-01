n <-10
p <- 0.5

NrIncercari <- 0:n

probabilities <-dbinom(NrIncercari,size=n,prob=p)

print(data.frame(Successes=NrIncercari,Probability=probabilities))


#nr incercari din java
n <- 10
#nr succese
x <- 1
#F(X=x)
F=dbinom(x,size=n,prob=p)
print(F)