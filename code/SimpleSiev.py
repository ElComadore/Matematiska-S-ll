def SimpleSiev(N):  # Traditional Sieve of Eratosthenes
    P = zeros(N+1)  # Create bitarray of N+1 '0's, representing numbers 0 to N
    P[2] = True     # Set 2 to '1'
    P[3::2] = True  # Set odd numbers >1 to '1'
    for num in range(3, isqrt(N)+1, 2):
        if P[num]: P[num*num::2*num] = False  # Set odd mult's of num to '0'
    return P
