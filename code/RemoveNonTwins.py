def RemoveNonTwins(S): # Sieve for twin primes in prime list.
    # If the last or second to last number in the given list is prime,
    #  then that prime won't get removed even though it might not be a twin prime.
    from bitarray import bitarray
    try:  # Removes 2 if present
        # Searches bits 0-3 for occurrence of '11' corresponing to primes 2,3
        #   then replaces '11' with '01'
        two = S.search(bitarray('11'),3)
        S[two[0]] = False
    except:
        pass
    for i in S.itersearch(bitarray('100')): # Replaces strings of 100 to 000 in bitarray S
        S[i:i+3] = False
    if S[-1]|S[-2]:
        print("Warning! The last prime in the list may not be a twin prime.")
    return
