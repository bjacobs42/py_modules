ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


def update_tuple(src: list, index: int, value: str) -> tuple:
    src_list = list(src)
    src_list[index] = value

    new_tuple = tuple(src_list)

    return (new_tuple)


ft_list[1] = 'World!'
ft_tuple = update_tuple(ft_tuple, 1, 'Netherlands')
ft_set.remove('tutu!')
ft_set.add('Amsterdam')
ft_dict['Hello'] = 'Codam'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
