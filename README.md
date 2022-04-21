# Martingale vs. Anti-Martingale Strategies

This program is made to analyze the performance of the Martingale and Anti-Martingale strategies.


## Martingale
Martingale is a betting strategy that is used to increase the odds of winning.
Assuming that you have an infinite amount of money, you are able to gain net profits by doubling your bet every time you lose, until you win. That way, you will always have a profit of at least 1.
This strategy is used to minimize the risk of losing.

## Anti-Martingale
Anti-Martingale is a betting strategy opposite to Martingale.
Basically you double your bet every time you win, but if you lose, you have to divide your bet by 2.
This strategy is used to increase the amount of money you have, granted a winning streak.
There is a risk of losing all money in one shot granted too many wins and sudden loss.


## How to use the program
You need Python 3.6 or higher to run this program.
Create a virtual environment and install the required packages.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then run the program.

```bash
python main.py
```

## Dependencies
The program requires the following packages:

- tabulate
- matplotlib

