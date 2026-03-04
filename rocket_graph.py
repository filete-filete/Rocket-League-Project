import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ranked2v2():
    # open txt and convert to a pandas dataframe
    file_path = r"C:\Users\felix\rocket_league_project\rlstats.txt"
    rocket_data = pd.read_csv(file_path)
    
    # obtain unduplicated data for 2v2 ranked games
    ranked2v2_data_unduplicated = rocket_data.drop_duplicates(subset = "2v2matches")
    ranked2v2_series = pd.Series(ranked2v2_data_unduplicated["2v2mmr"]).reset_index(drop = True)
    
    # print a lineplot
    plt.figure(figsize = (8,5))
    sns.lineplot(data = ranked2v2_series, marker = "o", label = "Ranked 2v2 MMR")
    plt.title("Rocket League Competitive Rank: rank after each game")
    plt.figure(1)
    
    plt.show()


