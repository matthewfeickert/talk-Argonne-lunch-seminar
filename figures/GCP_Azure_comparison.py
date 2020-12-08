import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 14})


def plot_times(cards, GCP_times, Azure_times, precision_type, max_time):
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 5)

    x = np.arange(len(cards))
    width = 0.35

    ax.bar(x, GCP_times, width, label="GCP")
    ax.bar(x + width, Azure_times, width, label="Azure")
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(cards)
    ax.set_ylim(top=max_time)

    ax.set_title(f"{precision_type} precision")
    ax.set_xlabel("GPU Cards")
    ax.set_ylabel("Approximate fit time (seconds)")
    ax.legend(loc="best", frameon=False)
    fig.tight_layout()

    fig.savefig(f"GCP_Azure_comparison_{precision_type.lower()}_precision.png")


def main():

    # Single precision
    cards_single = ["M60", "P4", "P40", "T4", "K80", "P100", "V100", "A100", "TPU2-8"]
    GCP_times_single = [0, 1.06, 0, 0.685, 0.968, 0.328, 0.279, 0.159, 3.73]
    Azure_times_single = [1.09, 0, 0.595, 0, 0.962, 0.348, 0.204, 0, 0]

    cards_double = cards_single[:-1]  # Drop TPU2-8
    GCP_times_double = [0, 2.72, 0, 1.97, 4.08, 0.816, 0.824, 0.383]
    Azure_times_double = [2.18, 0, 1.37, 0, 4.07, 0.761, 0.820, 0]

    time_lists = [
        GCP_times_single,
        GCP_times_double,
        Azure_times_single,
        Azure_times_double,
    ]
    max_time = np.max([np.max(list) for list in time_lists]) * 1.05

    plot_times(cards_single, GCP_times_single, Azure_times_single, "Single", max_time)
    plot_times(cards_double, GCP_times_double, Azure_times_double, "Double", max_time)


if __name__ == "__main__":
    main()
