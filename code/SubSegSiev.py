def SubSegSiev(n, Delta, M):
    S = zeros(Delta+1)
    S.setall(True)
    if n <= 1: S[0:2-n] = False
    D_s = isqrt(M)    # Size (-1) of each segment
    for M_s in range(1, M+1, D_s+1):  # Iterate through segments
        Primes = SimpleSegSiev(M_s, min(M-M_s,D_s), isqrt(M_s+D_s))  # Get primes in segment
        for p in Primes.itersearch(bitarray('1')): # Iterate through primes
            p = p+M_s  # shift p to get the actual prime number
            S[max(-(n//-p),2)*p-n::p] = False
    return S
