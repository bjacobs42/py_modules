#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter, MultipleLocator


def convert_population(pop_str:  str) -> float:
    """
    Converts population strings with 'M', 'k' and 'B' suffixes to its numeric value.

    Parameters:
        pop_str: numeric string with or without 'M', 'k' or 'B'.

    Returns:
        float.
    """

    if isinstance(pop_str, str):
        if pop_str.endswith('M'):
            return float(pop_str.replace('M', '')) * 1e6
        elif pop_str.endswith('k'):
            return float(pop_str.replace('k', '')) * 1e3
        elif pop_str.endswith('B'):
            return float(pop_str.replace('B', '')) * 1e9
    return pd.to_numeric(pop_str, errors='coerce')


def format_population_tick(pop: float, pos=None) -> str:
    """
        Formatter for the matplotlib FuncFormatter,
        formats numeric values to strings with suffix 'B', 'M' or 'k'.

        Parameter:
            pop: float number.

        Returns:
            str.
    """

    if pop >= 1e9:
        return f"{pop * 1e-9:.0f}B"
    elif pop >= 1e6:
        return f"{pop * 1e-6:.0f}M"
    elif pop >= 1e3:
        return f"{pop * 1e-3:.0f}k"
    else:
        return f"{pop:.0f}"


def plot_population(
        df: pd.DataFrame, country1="Netherlands", country2="Belgium"
) -> None:
    """
    Creates and displays a population graph from the given DataFrame.

    Does nothing when both country are not found.

    Parameters:
        df: A DataFrame containing total population by year and by country.
        country1: Chosen country to be displayed on the figure.
        country2: Other chosen country to be displayed on the figure.

    Returns:
        None.
    """

    country_df = df[df["country"].isin([country1, country2])]
    if country_df.empty:
        print(f"Error: No data found for '{country1}' and '{country2}'")
        return

    df_melted = pd.melt(
        country_df,
        id_vars=['country'],
        var_name='year',
        value_name='population'
    )

    df_melted['year'] = pd.to_numeric(df_melted['year'], errors='coerce')
    df_melted = df_melted[(df_melted['year'] >= 1800) & (df_melted['year'] <= 2050)]
    df_melted['population'] = df_melted['population'].apply(convert_population)

    fig, ax = plt.subplots(figsize=(10, 6))

    for country in df_melted['country'].unique():
        country_data = df_melted[df_melted['country'] == country]
        ax.plot(country_data['year'], country_data['population'], label=country)

    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    ax.set_title(f"Population Projections ({country1} and {country2})")
    ax.legend()

    ax.xaxis.set_major_locator(MultipleLocator(40))
    ax.yaxis.set_major_formatter(FuncFormatter(format_population_tick))

    plt.tight_layout()
    plt.savefig("./population_graph.png", bbox_inches="tight")
    # plt.show()


def main():
    total_pop: pd.DataFrame = load("../resources/population_total.csv")
    if total_pop is None:
        return

    plot_population(total_pop)


if __name__ == "__main__":
    main()
