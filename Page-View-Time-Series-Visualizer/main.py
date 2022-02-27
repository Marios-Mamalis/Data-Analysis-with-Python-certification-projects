import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[(df['value']>df['value'].quantile(0.025))&(df['value']<df['value'].quantile(0.975))]
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x='date', y='value', ax=ax)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel("Date")
    plt.ylabel("Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df.date.dt.month
    df_bar['year'] = df.date.dt.year
    df_bar.groupby([df_bar['year'], df_bar['month']]).agg({'value': 'mean'})
    # Draw bar plot
    fig, ax = plt.subplots()
    sns.barplot(data=df_bar, x='year', hue='month', y='value', ci=None, ax=ax)
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    ax.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['a'] = [d.strftime('%m') for d in df_box.date]
    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    sns.boxplot(data=df_box, x='year', y='value', hue='year', ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set(xlabel='Year', ylabel='Page Views')
    sns.boxplot(data=df_box.sort_values(by='a'), x='month', y='value', hue='month', ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set(xlabel='Month', ylabel='Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
