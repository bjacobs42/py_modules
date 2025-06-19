import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import MaxNLocator


def plot_life_expectancy(df: pd.DataFrame, country="Netherlands") -> None:
    """
    Creates and displays a life expectancy graph from the given DataFrame.

    Does nothing when country not found.

    Parameters:
        df: A DataFrame containing life expectancies by year and by country,
        country: Chosen country to be shown on the figure

    Returns:
        None
    """

    country_df = df[df["country"] == country]
    if country_df.empty:
        print(f"Error: No data found for country '{country}'")
        return

    df_melted = pd.melt(
        country_df,
        id_vars=['country'],
        var_name='year',
        value_name='life_expectancy'
    )
    df_melted['year'] = pd.to_numeric(df_melted['year'], errors='coerce', downcast='integer')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df_melted['year'], df_melted['life_expectancy'], label="Life Expectancy")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, min_n_ticks=10))
    ax.set_ylabel("Life expectancy")
    ax.set_xlabel("Year")
    ax.set_title(f"{country_df['country'].iloc[0]} Life expectancy Projections")
    plt.savefig("./line_graph")
    # plt.show()


def main():
    life_expectancies: pd.DataFrame = load("../resources/life_expectancy_years.csv")
    if life_expectancies is None:
        return

    plot_life_expectancy(life_expectancies)


if __name__ == "__main__":
    main()
