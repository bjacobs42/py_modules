from ft_filter import ft_filter

values = [0, 1, "", "hello", [], [1, 2], None, True]


print("Built-in filter with None:", list(filter(None, values)))
print("Custom ft_filter with None:", list(ft_filter(None, values)))
