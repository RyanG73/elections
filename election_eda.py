import pandas as pd
import numpy as np


gov_county = pd.read_csv('/Users/ryangerda/PycharmProjects/elections/us-election-2020/governors_county.csv')


house_candidate = pd.read_csv('us-election-2020/house_candidate.csv')
house_state = pd.read_csv('us-election-2020/house_state.csv')

pres_county_candidate = pd.read_csv('us-election-2020/president_county_candidate.csv')
pres_county = pd.read_csv('us-election-2020/president_county.csv')



ohio = pres_county_candidate[pres_county_candidate['state'] == 'Ohio']