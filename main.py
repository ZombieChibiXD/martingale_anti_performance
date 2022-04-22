import random
from tabulate import tabulate


def coinflip():
  return random.randint(0,1) == 1



# Get 2% of 100000
TEN_PERCENT = 100000 * 0.02


# Starting VARIABLES
# You can change these variables to your liking
STARTING_FUNDS = 1 * 10**6
ITERATION = 100000
FUND_INCREMENT_ITERATION = 100
# Starting bet is 0.005 % of your starting funds
MARTINGALE_STARTING_BET = STARTING_FUNDS * 5 // (100000)
ANTI_MARTINGALE_STARTING_BET = STARTING_FUNDS * 100 // (100000)
MARTINGALE_MULTIPLIER = 2
AM_WIN_COUNT = 0
# For the true anti-martingale strategy, you need to set this to INFINITY
AM_MAX_WIN_COUNT = 5
AM_MAX_LOSS_COUNT = 10




# DO NOT MODIFY
MARTINGALE_FUNDS = STARTING_FUNDS
ANTI_MARTINGALE_FUNDS = STARTING_FUNDS
MARTINGALE_BET = MARTINGALE_STARTING_BET
ANTI_MARTINGALE_BET = ANTI_MARTINGALE_STARTING_BET

RESULT = []

for i in range(1, ITERATION+1):
  if MARTINGALE_FUNDS - MARTINGALE_BET < 0:
    MARTINGALE_BET = MARTINGALE_STARTING_BET
  if MARTINGALE_FUNDS - MARTINGALE_BET < 0:
    MARTINGALE_BET = 0

  if ANTI_MARTINGALE_FUNDS - ANTI_MARTINGALE_BET < 0:
    ANTI_MARTINGALE_BET = ANTI_MARTINGALE_STARTING_BET
  if ANTI_MARTINGALE_FUNDS - ANTI_MARTINGALE_BET < 0:
    ANTI_MARTINGALE_BET = 0

  MARTINGALE_FUNDS -= MARTINGALE_BET
  ANTI_MARTINGALE_FUNDS -= ANTI_MARTINGALE_BET
  MARTINGALE_FUNDS += FUND_INCREMENT_ITERATION
  ANTI_MARTINGALE_FUNDS += FUND_INCREMENT_ITERATION

  if ANTI_MARTINGALE_FUNDS <= 0 or MARTINGALE_FUNDS <= 0:
    break

  win = coinflip()
  LAST_MARTINGALE_BET = MARTINGALE_BET
  LAST_ANTI_MARTINGALE_BET = ANTI_MARTINGALE_BET
  if win:
    MARTINGALE_FUNDS += MARTINGALE_BET*2
    ANTI_MARTINGALE_FUNDS += ANTI_MARTINGALE_BET*2
    MARTINGALE_BET = MARTINGALE_STARTING_BET
    ANTI_MARTINGALE_BET *= 2
    AM_WIN_COUNT += 1
    if AM_WIN_COUNT > AM_MAX_WIN_COUNT:
      ANTI_MARTINGALE_BET = ANTI_MARTINGALE_STARTING_BET
      AM_WIN_COUNT = 0
  else:
    MARTINGALE_BET *= MARTINGALE_MULTIPLIER
    ANTI_MARTINGALE_BET //= 2
    if ANTI_MARTINGALE_BET < 1:
      ANTI_MARTINGALE_BET = 1
    AM_WIN_COUNT -= 1
    if 0-AM_WIN_COUNT > AM_MAX_LOSS_COUNT:
      ANTI_MARTINGALE_BET = ANTI_MARTINGALE_STARTING_BET
      AM_WIN_COUNT = 0

  # Print out the results, like a table
  SAVING_FUNDS = STARTING_FUNDS + FUND_INCREMENT_ITERATION * (i-1)
  RESULT.append(
    ( i,
      win and "W" or "L",
      MARTINGALE_FUNDS,
      LAST_MARTINGALE_BET,
      MARTINGALE_FUNDS-SAVING_FUNDS,
      ANTI_MARTINGALE_FUNDS,
      LAST_ANTI_MARTINGALE_BET,
      ANTI_MARTINGALE_FUNDS-SAVING_FUNDS,
      AM_WIN_COUNT,
      # AM_LOSS_COUNT,
    )
  )

print(tabulate(RESULT, headers=['No', 'Win', 'OM Funds', 'OM Bet', 'M Profit', 'AM Funds', 'AM Bet', 'AM Profit', 'AMW', 'AML']))

# Print growth percentage
SAVING_FUNDS = STARTING_FUNDS + FUND_INCREMENT_ITERATION*len(RESULT)
print("Martingale Percentage: %.2f%%" % (100*(MARTINGALE_FUNDS-SAVING_FUNDS)/SAVING_FUNDS),(MARTINGALE_FUNDS-SAVING_FUNDS))
print("Anti-Martingale Percentage: %.2f%%" % (100*(ANTI_MARTINGALE_FUNDS-SAVING_FUNDS)/SAVING_FUNDS), (ANTI_MARTINGALE_FUNDS-SAVING_FUNDS))

# Output the final results to CSV
# import csv


# with open('results.csv', 'w') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerow(['No', 'Win', 'OM Funds', 'OM Bet', 'M Profit', 'AM Funds', 'AM Bet', 'AM Profit', 'AMW', 'AML'])
#   writer.writerows(RESULT)

# Plot graph
import matplotlib.pyplot as plt


plt.plot(range(len(RESULT)), [x[2] for x in RESULT], label='Martingale')
plt.plot(range(len(RESULT)), [x[5] for x in RESULT], label='Modified Anti-Martingale')
plt.plot(range(len(RESULT)), [STARTING_FUNDS+x*FUND_INCREMENT_ITERATION for x in range(len(RESULT))], label='Starting fund + savings')
plt.legend()
plt.show()