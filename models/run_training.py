# from models.train_both_models import train_both_models
# from reporting.accuracy_curves import get_accuracy_curves, calculate_gini
from loan_models.models.train_both_models import train_both_models
from loan_models.reporting.accuracy_curves import get_accuracy_curves

if __name__ == "__main__":
    model_type = "random_forest"
    # model_type = "gradient_boosting"
    bad_loan_model, interest_rate_model, valid = train_both_models(model_type)


