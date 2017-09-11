from .training import init_h2o, get_data
from .training import get_trained_model, print_gini


def train_both_models(model_type):
    """
    Train both Bad Loan and Interest Rate Models
    :param model_type: model_type (currently one of:
    random_forest, gradient_boosting or logistic regression)
    :return:
    """

    init_h2o()

    train, valid = get_data()

    if model_type == "logistic_regression":
        # Logistic regression requires 0 or 1 integer
        # rather than categorical (enum)
        target_variable = "bad_loan"
    else:
        target_variable = "bad_loan_categorical"

    name = "BadLoanModel"
    bad_loan_model = get_trained_model(train, valid, name,
                                       target_variable, model_type)

    if model_type != 'logistic_regression':
        print_gini(bad_loan_model)

    target_variable = "int_rate"
    name = "InterestRateModel"
    _ = get_trained_model(train, valid, name, target_variable, model_type)

