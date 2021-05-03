def SimpleSegSiev(n, Delta, M):
    S = zeros(Delta+1)
    S.setall(True)  # Set all bits in S to '1'
    if n <= 1: S[0:2-n] = False  # Set 0 and 1 to '0' if present
    Primes = SimpleSiev(M)  # Get list of primes up to M
    for p in Primes.itersearch(bitarray('1')):  # Iterate through primes
        S[max(-(n//-p), 2)*p - n::p] = False  # Set multiples of p to '0'
    return S
