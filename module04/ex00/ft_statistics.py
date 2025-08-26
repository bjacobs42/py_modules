def get_mean(nums: list, number_count: int) -> float:
    return (sum(nums) / number_count)

    
def get_median(args: list, argc: int) -> float:
    mid: int = (argc - 1) // 2
    value: float
    
    if argc % 2 == 0:
        value = args[mid] + args[mid + 1] // 2
    else:
        value = args[mid]
    return (value)


def get_quartile(args: list, argc: int) -> list:
    argc -= 1
    quartile25_index: float = 0.25 * argc
    quartile75_index:float = 0.75 * argc

    def interlopate(index: float) -> float:
        lower = int(index)
        upper = lower + 1
        if upper > argc:
            return args[lower]
        return args[lower] + (args[upper] - args[lower]) * (index - lower)

    quartile25: float = interlopate(quartile25_index)
    quartile75: float = interlopate(quartile75_index)
    return ([quartile25, quartile75])


def get_variance(numbers: list, argc: int) -> float:
    mean: float = get_mean(numbers, argc)
    variance = sum((num - mean) ** 2 for num in numbers) / argc
    return (variance)


def get_standard_deviation(numbers, number_count) -> float:
    variance: float = get_variance(numbers, number_count)
    deviation: float = variance ** 0.5
    return (deviation)


def ft_statistics(*args, **kwargs) -> None:
    argc: int = len(args)
    try:
        args = sorted(args)
    except Exception:
        print("ERROR")
        return

    for key in kwargs:
        try:
            match kwargs[key]:
                case "mean":
                    print(f"mean : {get_mean(args, argc)}")
                case "median":
                    print(f"median : {get_median(args, argc)}")
                case "quartile":
                    print(f"quartile : {get_quartile(args, argc)}")
                case "std":
                    print(f"standard deviation : {get_standard_deviation(args, argc)}")
                case "var":
                    print(f"variance : {get_variance(args, argc)}")
        except Exception:
            print("ERROR")
