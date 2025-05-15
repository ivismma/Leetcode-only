// https://leetcode.com/problems/count-primes/

int countPrimes(int n) {
    if(n < 3)
        return 0;

    int *primes = (int *) malloc((n+1)*sizeof(int));
    // presumir que todos ímpares são primos
    for(int i = 3; i <= n; ++i)
        primes[i] = 1;
    
    // invalidar pares
    for(int i = 4; i < n; i += 2) primes[i] = 0;
    
    int max = sqrt(n);
    for(int i = 3; i <= max; i += 2){
        if(primes[i])
            for(int j = i*i; j < n; j += i)
                primes[j] = 0;
    }
    
    // contar primos:
    int amount = 1; // 2
    for(int i = 3; i < n; i += 2)
        if(primes[i]) 
            ++amount;
    
    free(primes);
    return amount;
}
