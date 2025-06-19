#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter, MultipleLocator


def convert_suffixed_num(num: str) -> float:
    """
    Converts population strings with 'M', 'k' and 'B' suffixes to its numeric value.

    Parameters:
        num: numeric string with or without 'M', 'k' or 'B'.

    Returns:
        float.
    """

    if isinstance(num, str):
        if num.endswith('M'):
            return float(num.replace('M', '')) * 1e6
        elif num.endswith('k'):
            return float(num.replace('k', '')) * 1e3
        elif num.endswith('B'):
            return float(num.replace('B', '')) * 1e9
    return pd.to_numeric(num, errors='coerce')


def format_numeral_tick(str_val: float, pos=None) -> str:
    """
        Formatter for the matplotlib FuncFormatter,
        formats numeric values to strings with suffix 'B', 'M' or 'k'.

        Parameter:
            str_val: float number.
            pos: no usage, just for the FuncFormatter.

        Returns:
            str.
    """

    if str_val >= 1e9:
        return f"{str_val * 1e-9:.0f}B"
    elif str_val >= 1e6:
        return f"{str_val * 1e-6:.0f}M"
    elif str_val >= 1e3:
        return f"{str_val * 1e-3:.0f}k"
    else:
        return f"{str_val:.0f}"


def scatter(life_expectancies: pd.DataFrame, gdp_income_pp: pd.DataFrame) -> None:
    """
    Creates and displays a graph of life expectancy in relation
    to the gross national product of the year 1900 from the given DataFrames.

    Does nothing when either DataFrames are empty.

    Parameters:
        life_expectancies: A DataFrame containing life expectancies by year and by country.
        gdp_income_pp: A DataFrame containing gdp income per person by country.

    Returns:
        None.
    """

    life_expectancies['1900'] = pd.to_numeric(
        life_expectancies['1900'], errors='coerce'
    )
    gdp_income_pp['1900'] = gdp_income_pp['1900'].apply(convert_suffixed_num)
    df_merged: pd.DataFrame = life_expectancies.merge(
        gdp_income_pp, how='inner', on='country', suffixes=('_age', '_gdp')
    )
    
    ax = df_merged.plot.scatter(x='1900_gdp', y='1900_age')

    ax.set_xlabel("Gross Domestic product")
    ax.set_ylabel("Life Expectancy")
    ax.set_title("1900")
    # ax.legend()

    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.xaxis.set_major_formatter(FuncFormatter(format_numeral_tick))

    plt.tight_layout()
    plt.savefig("./life_gdp_relation_graph.png", bbox_inches="tight")
    # plt.show()


def main():
    life_expectancies: pd.DataFrame = load("../resources/life_expectancy_years.csv")
    gdp_income_pp: pd.DataFrame = load(
        "../resources/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    if gdp_income_pp is None or life_expectancies is None:
        return

    scatter(life_expectancies, gdp_income_pp)


if __name__ == "__main__":
    main()
