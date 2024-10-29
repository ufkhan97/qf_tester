## QF TESTER
This codebase is designed to implement various Quadratic Funding (QF) algorithms. It includes functions for data preparation, calculation of matching funds, and testing of different QF strategies.

## Key Files
- fundingutils.py: Contains utility functions for data preparation and QF calculations.
- qf_tester.py: Contains functions to run QF calculations on a given dataset and save the results.

## Usage
- If you run 'python qf_tester.py' in the terminal, the code will run a QF calculation on the sample dataset provided. The results will be saved in a new file. 
- You can also import the functions from qf_tester.py and use them in your own code.
- You can use any votes file as long as it has the following columns: 
  - voter
  - amountUSD
  - payoutAddress
  - project_name
  - score

The score column is intended for gitcoin passport protected rounds. If you aren't using passport then you can set the score to 100 for all votes and completely ignore passport. Otherwise, a score below 15 means the vote is ignored and a score above 15 means the vote is included in the calculation; with the score determining the weight of the vote. 15 gets half weight, 25 or above gets full weight.

