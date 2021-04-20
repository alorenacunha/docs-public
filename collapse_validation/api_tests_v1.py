# importing the requests library 
#%%
import pandas as pd
import os
import requests 
import math
from pandas import DataFrame

#working directory
os.chdir("C:/Users/lorena.ferreira/Desktop/Lorena/api_tests/api_tests")
#os.chdir("C:/Users/pedro.filgueiras/OneDrive - Vallourec/RDPE/Internal Support/IS008 - QAQC/2020.02 Rath 16.25'' 10,000psi")

#data loading

data_wt = pd.read_excel('WT_data_condensed.xlsx')
data_od = pd.read_excel('OD_data_condensed.xlsx')

#constantes
averaging_length_collapse = 4

##########################################################
#Verify API
##########################################################

# api-endpoint 
#%%
URL = "http://10.34.17.102:8000/pp2020/verify_ndt_data/300"

# create the units dictionary
dict_units = {"position_WT": "in", #unit
              "position_OD" : "ft",
              "WT" : "in",
              "OD" : "mm",
              "blind_length_end_OD" : "mm",
              "blind_length_end_WT" : "mm",
              "drift_length" : "mm",
              "min_pipe_length" : "mm",
              "max_pipe_length" : "mm",
              "cut_off_length" : "mm",
              "WTnom" : "in",
              "ODnom" : "mm",
              "output_position":"mm",
              "output_WT":"mm",
              "output_OD":"mm"}
              
#body
body_dict = {"input" : {
                "df_segments_OD": data_od.to_dict('record'),
                "df_segments_WT" : data_wt.to_dict('record'),
                "blind_length_end_WT" : 300,
                "blind_length_end_OD" : 300,
                "averaging_length_collapse" : averaging_length_collapse,
                "drift_length" : 300,
                "min_pipe_length" : 11580,
                "max_pipe_length" : 13720,
                "cut_off_length" : 100,
                "od_limit_min" : -0.5,
                "od_limit_max" : 1,
                "RBW" : 0.9,
                "WTnom" : 0.82,
                "ODnom" : 357,
                "dict_units" : dict_units}
              }
              
# sending post request and saving response as response object 
ans = requests.post(url = URL, json = body_dict)
ans_dict = ans.json() 
data_new = pd.DataFrame.from_dict(ans_dict[0])
print("verify ok")

data_new.to_excel("verify_pipe_original.xlsx")

collapse_length = 4 * 357
              
##########################################################
#Collapse API MC Correlated - Aramis
##########################################################
#%%
URL = "http://10.34.17.102:8000/pp2020/collapse_calc_aramis/30000"



#eng. units
dict_units = {"wt": "mm",
              "od": "mm",
              "ys": "psi",
              "rs": "psi",
              "collapse_length" : "mm"}

#input json
body_dict = {"input" : {"data" : data_new.dropna().to_dict('records'),
                        "collapse_dict_input" : { "num_sims1" : 100,
                                                  "num_sims2" : 100,
                                                  "ys_mean_sample_of_mean" : 105000,
                                                  "ys_sd_sample_of_mean" : 110,
                                                  "ys_n_sample_of_mean" : 20,
                                                  "ys_sd_sample_of_sd" : 100,
                                                  "ys_n_sample_of_sd" : 10,
                                                  "rs_mean_sample_of_mean" : -10500,
                                                  "rs_sd_sample_of_mean" :  -10500/math.sqrt(10),
                                                  "rs_n_sample_of_mean" : 10,
                                                  "rs_sd_sample_of_sd" : 2900,
                                                  "rs_n_sample_of_sd" : 10,
                                                  "mu_mean_sample_of_mean" : 1.0,
                                                  "mu_sd_sample_of_mean" : 0.06,
                                                  "mu_n_sample_of_mean" : 10,
                                                  "mu_sd_sample_of_sd" : 0.06/math.sqrt(10),
                                                  "mu_n_sample_of_sd" : 10,
                                                  "mu_corr" : 0.96,
                                                  "collapse_length" : collapse_length},
                               "dict_units" : dict_units}}
             
# sending post request and saving response as response object 
ans = requests.post(url = URL, json = body_dict)
collapse_data_aramis = ans.json() 
print("collapse_aramis: ",collapse_data_aramis)

data_collapse = DataFrame (collapse_data_aramis,columns=['Collapse Value'])

data_collapse.to_excel("collapse_data_aramis_original.xlsx")
