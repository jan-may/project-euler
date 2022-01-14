import eulerlib

print(
    sum(
        1
        for n in range(1, 101)
        for k in range(n + 1)
        if eulerlib.numtheory.nCr(n, k) > 1000000
    )
)