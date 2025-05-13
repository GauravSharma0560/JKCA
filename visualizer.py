import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def generate_all_plots(df):
    plot_dir = 'static/plots'
    os.makedirs(plot_dir, exist_ok=True)

    # Match result distribution
    plt.figure(figsize=(7,5))
    sns.countplot(x='Match_Result', data=df, palette='Set2')
    plt.title("Match Outcomes")
    plt.savefig(f"{plot_dir}/match_results.png")
    plt.close()

    # Top 5 Run Scorers
    top_runs = df.groupby("Player_Name")["Runs"].sum().nlargest(5)
    top_runs.plot(kind='bar', color='skyblue', figsize=(7,5), title="Top 5 Run Scorers")
    plt.ylabel("Total Runs")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/top_runs.png")
    plt.close()

    # Top 5 Wicket Takers
    top_wickets = df.groupby("Player_Name")["Wickets"].sum().nlargest(5)
    top_wickets.plot(kind='bar', color='coral', figsize=(7,5), title="Top 5 Wicket Takers")
    plt.ylabel("Total Wickets")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/top_wickets.png")
    plt.close()

    # Role distribution
    plt.figure(figsize=(6,5))
    sns.countplot(y="Role", data=df, order=df["Role"].value_counts().index, palette="viridis")
    plt.title("Player Role Distribution")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/role_distribution.png")
    plt.close()

    # Performance by role (Runs vs Wickets average)
    perf = df.groupby("Role")[["Runs", "Wickets"]].mean()
    perf.plot(kind="barh", figsize=(8,5), colormap="Accent")
    plt.title("Average Performance by Role")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/performance_by_role.png")
    plt.close()

    # Scatter: Wickets vs Runs
    plt.figure(figsize=(7,5))
    sns.scatterplot(x="Runs", y="Wickets", hue="Role", data=df, palette="Set1", s=80)
    plt.title("Wickets vs Runs by Players")
    plt.tight_layout()
    plt.savefig(f"{plot_dir}/wickets_vs_runs.png")
    plt.close()
