def SubSegSievTwins(n, Delta, M):  # Sieve for twin primes, small mod of SubSegSiev, needed in NewSegSievTwins
    S = zeros(Delta+1)
    S.setall(True)
    S[0:2-n] = False
    D_s = isqrt(M)
    for M_s in range(1, M+1, D_s+1):
        Primes = SimpleSegSiev(M_s, D_s, isqrt(M_s+D_s))
        for p in Primes.itersearch(bitarray('1')):
            p = p+M_s
            start = max(-(n//-p),2)*p-n
            S[start::p] = False
            if start-2<0:
                start = start+p
            S[start-2::p] = False
    return S
