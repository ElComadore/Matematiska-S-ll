def NewSegSievTwins(n, Delta, K):  # Sieve for twin primes, small mod of NewSegSiev
    if n**(1/3)>=Delta or Delta>n:
        raise Exception("Delta should be between n^(1/3) and n.")
    if K < 2.5:
        raise Exception("K must be at least 2.5")
    if n+Delta < 16:
        raise Exception("n + Delta must be at least 16")
    upper = n+Delta
    lower = n-Delta
    f = sqrt(Delta/(4*n))
    bound1 = sqrt(upper)
    M = floor(K*Delta) + 1
    S = SubSegSievTwins(lower, 2*Delta, M-1)
    while M <= bound1:
        R = floor(M*f)
        m0 = M + R
        alpha0 = n/m0 % 1
        alpha1 = -n/(m0*m0) % 1
        ainv, q = DiophAppr(alpha1, 2*R)
        c = floor(alpha0*q + 0.5)       
        k = floor(5*Delta*q/(4*M))
        bound2 = M + 2*R + 1
        for j in range(-k-1, k+2):
            r0 = -ainv*(c+j) % q
            for m in range(m0+r0-((m0+r0-M)//q)*q, bound2, q):
                n_s = (upper//m)*m
                if n_s >= lower+2:  # both n_s and its twin n_s-2 is in the interval
                    S[n_s - lower] = False
                    S[n_s-2 - lower] = False
                elif n_s >= lower:  # n_s is in the interval but not n_s-2
                    S[n_s - lower] = False
                    if n_s+m-2 <= upper:  # the twin to the next multiple of m is in the interval
                        S[n_s+m-2 - lower] = False
        M = bound2
    return S
