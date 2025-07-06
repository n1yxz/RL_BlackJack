
# RL_BlackJack – Reinforcement‑Learning Assignment 2

This repo contains everything you need to reproduce the Monte‑Carlo Control and Sarsa(λ)
experiments for the **Modified Black Jack** game.

## Quick start

```bash
git clone <your‑fork‑url>
cd RL_BlackJack
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Open **`mc_control.ipynb`** first to create `mc_Q_star.npy`, then run **`sarsa_lambda.ipynb`**.

## Directory structure

```
RL_BlackJack/
├─ env.py               # the game environment
├─ mc_control.ipynb     # Monte‑Carlo Control notebook
├─ sarsa_lambda.ipynb   # Sarsa(λ) notebook (forward view)
├─ plots/               # figures auto‑saved here
├─ requirements.txt
└─ README.md
```

## Submission checklist ✔️

* Export a single PDF that includes **all plots**.
* Zip the repo (without the virtual‑env) as `source.zip`.
* No Colab notebooks. 100 % forward view (no eligibility traces).

Happy learning!
