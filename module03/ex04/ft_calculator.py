class calculator:
    """ A class that holds calculations static methods like dotproduct """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and prints the dot product
        between the arguments `V1` and `v2`.
        """

        dot_product = sum(a * b for a, b in zip(V1, V2))
        print(dot_product)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and prints the addition
        between the arguments `V1` and `v2`.
        """

        vec_sum = [a + b for a, b in zip(V1, V2)]
        print(vec_sum)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculates and prints the subtraction
        between the arguments `V1` and `v2`.
        """

        vec_sum = [a - b for a, b in zip(V1, V2)]
        print(vec_sum)
