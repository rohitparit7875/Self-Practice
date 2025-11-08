fib = lambda n: [0,1][:n] + [(__ := [0,1])[0] or (__ := [__[-1], sum(__)]) and __[1] for _ in range(n-2)]
print(fib(10))
