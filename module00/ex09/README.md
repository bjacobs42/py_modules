# ft_package
A python library for counting values in iterables, nothing too special

## Installation
This library can be installed directly from PyPI:
```bash
pip install ft_package
```

### usage
```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
```
