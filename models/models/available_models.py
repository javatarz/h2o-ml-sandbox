from h2o.estimators import H2ORandomForestEstimator


def random_forest_model(name):
    """
    Get the (untrained) Random Forest Model
    :param name: model name, will determine filename
    :return: model
    """
    model = H2ORandomForestEstimator(
        ntrees=100,
        max_depth=5,
        stopping_tolerance=0.01,
        stopping_rounds=2,
        score_each_iteration=True,
        model_id=name,
        seed=2000000
    )
    return model
