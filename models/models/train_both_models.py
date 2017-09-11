from .training import init_h2o, get_data
from .training import get_trained_model, print_gini


def train_both_models():
    """
    Train both models
    """
    init_h2o()

    train, valid = get_data()

    target_variable = "bad_loan"
    name = "BadLoanModel"
    bad_loan_model = get_trained_model(train, valid, name, target_variable)
    print_gini(bad_loan_model)

    target_variable = "int_rate"
    name = "InterestRateModel"
    _ = get_trained_model(train, valid, name, target_variable)


if __name__ == "__main__":
    train_both_models()

