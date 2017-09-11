import h2o
import os
import sys

from .available_models import random_forest_model


def init_h2o():
    """
    Start up H2o
    """
    h2o.init(nthreads=-1)


def get_data():
    """
    Get the training and validation data
    :return:
    """
    loan_csv = "{}/data/loan.csv".format("" if len(sys.argv) == 0 else sys.argv[1])
    loans = h2o.import_file(loan_csv)

    print("Import approved and rejected loan requests...")

    loans["bad_loan"] = loans["bad_loan"].asfactor()

    train, valid, test = loans.split_frame([0.79, 0.2], seed=1234)
    return train, valid


def get_input_variables():
    """
    Get the input variables (predictors) used to train the model
    :return:
    """
    input_variables = ["loan_amnt", "longest_credit_length", "revol_util",
                       "emp_length", "home_ownership", "annual_inc",
                       "purpose", "addr_state", "dti", "delinq_2yrs",
                       "total_acc", "verification_status", "term"]

    return input_variables


def print_gini(model):
    """
    Print out the Gini coefficient for binary classification models
    :param model: Trained H2o model
    """
    gini = model.gini(valid=True)
    print("Gini coefficient: %s" % gini)


def get_trained_model(train, valid, name, target_variable):
    """
    :param train: Training frame
    :param valid: Validation frame
    :param name: String, Name of model, determines name of file
    :param target_variable: String, Target variable to be predicted
    :return: Trained model
    """

    input_variables = get_input_variables()
    model = random_forest_model(name)

    model.train(input_variables, target_variable,
                training_frame=train, validation_frame=valid)

    print(model)
    write_model_pojo(model)
    return model


def write_model_pojo(model):
    """
    Write the model as POJO
    :param model: trained model
    :return: None
    """

    # Relative path from code dir
    output_directory = "build"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    h2o.download_pojo(model, path=output_directory)
