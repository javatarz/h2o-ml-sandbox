from models.train_both_models import train_both_models

if __name__ == "__main__":
    model_type = "random_forest"
    # model_type = "logistic_regression"
    # model_type = "gradient_boosting"

    train_both_models(model_type)
