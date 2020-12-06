import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 14})


def main():
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 5)

    cards = ["P4", "T4", "K80", "P100", "V100", "A100"]
    times = [2.72, 1.97, 4.08, 0.816, 0.824, 0.338]
    x = np.arange(len(cards))
    width = 0.8

    for idx, _ in enumerate(cards):
        ax.bar(x[idx], times[idx], width, label=cards[idx])
    ax.set_xticks(x)
    ax.set_xticklabels(cards)

    ax.set_xlabel("Google Cloud Platform GPU Cards")
    ax.set_ylabel("Approximate fit time (seconds)")
    # ax.legend(loc="best")
    fig.tight_layout()

    fig.savefig("GCP_cards_fit_time.png")


if __name__ == "__main__":
    main()
