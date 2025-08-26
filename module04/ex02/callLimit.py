def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        nonlocal count
        count += 1
        def limit_function(*args, **kwds):
            nonlocal function

            if count <= limit:
                return function(*args, **kwds)
            print(f"Error: {function} called too many times")

    return (callLimiter)
