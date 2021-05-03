def DiophAppr(alpha, Q):
    b = p = floor(alpha)
    q = p_m = s = 1
    q_m = 0
    while q <= Q:
        if alpha == b:
            return -s*q_m, q
        alpha = 1/(alpha-b)
        b = floor(alpha)
        p, q, p_m, q_m, s = b*p+p_m, b*q+q_m, p, q, -s
    return s*q, q_m
