# Load the H2O library and start up the H2O cluter locally on your machine
import h2o
import numpy as np
import os
import sys
from h2o.estimators import H2ORandomForestEstimator

# Number of threads, nthreads = -1, means use all cores on your machine
# max_mem_size is the maximum memory (in GB) to allocate to H2O
h2o.init(nthreads=-1, max_mem_size=8)

loan_csv = "{}/data/loan.csv".format("" if len(sys.argv) == 0 else sys.argv[1])
# Alternatively, you can import the data directly from a URL
# loan_csv = "https://raw.githubusercontent.com/h2oai/app-consumer-loan/master/data/loan.csv"
loans = h2o.import_file(loan_csv)

print ("Import approved and rejected loan requests...")

loans["bad_loan"] = loans["bad_loan"].asfactor()
n_lines = len(loans)
rand = np.random.rand(n_lines)

# train = loans[rand <= 0.8, :]
# valid = loans[rand > 0.8, :]

train, valid, test = loans.split_frame([0.79, 0.2], seed=1234)

# Prepare predictors and response columns
# myX = loans.col_names[:-1]     #last column is Cover_Type, our desired response variable
# myY = loans.col_names[-1]

myY = "bad_loan"
myX = ["loan_amnt", "longest_credit_length", "revol_util", "emp_length",
       "home_ownership", "annual_inc", "purpose", "addr_state", "dti",
       "delinq_2yrs", "total_acc", "verification_status", "term"]

model = H2ORandomForestEstimator(
  ntrees=100,
  # learn_rate=0.05,
  max_depth=5,
  stopping_tolerance=0.01,  # 10-fold increase in threshold as defined in rf_v1
  stopping_rounds=2,
  score_each_iteration=True,
  model_id="BadLoanModel",
  seed=2000000
)
model.train(myX, myY, training_frame=train, validation_frame=valid)

print(model)

# Download generated POJO for model
output_directory = "build"
if not os.path.exists(output_directory):
  os.makedirs(output_directory)

h2o.download_pojo(model, path=output_directory)

# Interest rate model
myY = "int_rate"
myX = ["loan_amnt", "longest_credit_length", "revol_util", "emp_length",
       "home_ownership", "annual_inc", "purpose", "addr_state", "dti",
       "delinq_2yrs", "total_acc", "verification_status", "term"]

model = H2ORandomForestEstimator(
  ntrees=100,
  # learn_rate=0.05,
  max_depth=5,
  stopping_tolerance=0.01,  # 10-fold increase in threshold as defined in rf_v1
  stopping_rounds=2,
  score_each_iteration=True,
  model_id="InterestRateModel",
  seed=2000000
)
model.train(myX, myY, training_frame=train, validation_frame=valid)

print(model)

# Download generated POJO for model
if not os.path.exists(output_directory):
  os.makedirs(output_directory)

h2o.download_pojo(model, path=output_directory)
