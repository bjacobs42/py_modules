def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            count += 1

            if count <= limit:
                return function(*args, **kwds)
            print(f"Error: {function} called too many times")
        return limit_function
    return (callLimiter)
