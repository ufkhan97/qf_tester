import pandas as pd
import fundingutils

def run_qf(votes_file, strategy, min_donation_threshold_amount, matching_cap_amount, matching_amount, passport_threshold):
    votes = pd.read_csv(votes_file)

    # Prepare votes data
    votes_prep = fundingutils.prep_donations_data(votes, min_donation_threshold_amount, passport_threshold)
    votes_matrix = fundingutils.pivot_votes(votes_prep)
    votes_qf_matching = fundingutils.get_qf_matching(strategy, votes_matrix, matching_cap_amount, matching_amount, cluster_df = None if strategy == 'qf' else votes_matrix)
    
    # Save the matching data to a csv file
    votes_qf_matching['strategy'] = strategy
    votes_qf_matching.to_csv(f'{votes_file.split(".")[0]}_matching_data.csv')

def run_test():
    # Use a default csv file in the same directory
    votes_file = 'Zuzalu_Events_votes.csv'
    strategy = 'COCM' # can accept: 'qf' or 'COCM' 
    min_donation_threshold_amount = 1
    matching_cap_amount = 50
    matching_amount = 166.5
    passport_threshold = 15

    run_qf(votes_file, strategy, min_donation_threshold_amount, matching_cap_amount, matching_amount, passport_threshold)

def main():
    # Here you can add conditions or user input to decide which function to run
    run_test()

if __name__ == "__main__":
    main()