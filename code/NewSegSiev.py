def NewSegSiev(n, Delta, K): # Main algorithm
    # Argument parsing:
    if n**(1/3)>=Delta or Delta>n:
        raise Exception("Delta should be between n^(1/3) and n")
    if K < 2.5:
        raise Exception("K must be at least 2.5")
    if n+Delta < 16:
        raise Exception("n + Delta must be at least 16")

    # Calculation of some repeatedly used values:
    upper, lower = n+Delta, n-Delta
    f = sqrt(Delta/(4*n))
    bound1 = isqrt(upper)

    M = floor(K*Delta) + 1
    S = SubSegSiev(lower, 2*Delta, M-1) # SubsegSiev sieves by primes < M
    while M <= bound1: # Sieve by the larger primes not covered by SubSegSiev
        R = floor(M*f)
        m0 = M + R
        alpha0 = n/m0 % 1
        alpha1 = -n/(m0*m0) % 1
        ainv, q = DiophAppr(alpha1, 2*R)
        c = floor(alpha0*q + 0.5)
        k = floor(5*Delta*q/(4*M)) # Need int-type. floor(x/y) is faster than int(x//y)
        bound2 = M + 2*R + 1
        for j in range(-k-1, k+2):
            r0 = -ainv*(c+j) % q
            for m in range(m0+r0-((m0+r0-M)//q)*q, bound2, q): # for m in the intersection
                n_s = (upper//m)*m - lower
                if n_s >= 0: S[n_s] = False # Checking n_s <= n+Delta and n_s > m is redundant
        M = bound2
    return S
