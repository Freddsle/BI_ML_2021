import numpy as np


def binary_classification_metrics(y_pred, y_true):
    """
    Computes metrics for binary classification
    Arguments:
    y_pred, np array (num_samples) - model predictions
    y_true, np array (num_samples) - true labels
    Returns:
    precision, recall, f1, accuracy - classification metrics
    """

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score


    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    for i, pred in enumerate(y_pred):

        if pred == y_true[i]:
            if pred == 1:
                true_positive += 1
            if pred == 0:
                true_negative += 1

        elif pred != y_true[i]:
            if pred == 1 and y_true[i] == 0:
                false_positive += 1

            elif pred == 0 and y_true[i] == 1:
                false_negative += 1

    accuracy = (true_positive + true_negative) / (true_positive + false_positive + true_negative + false_negative)

    if true_positive == 0 and false_positive == 0 and false_negative == 0:
        # https://github.com/dice-group/gerbil/wiki/Precision,-Recall-and-F1-measure
        precision, recall, f1 = 1, 1, 1

    elif true_positive == 0:
        precision, recall, f1 = 0, 0, 0

    else:
        precision = true_positive / (true_positive + false_positive)
        recall = true_positive / (true_positive + false_negative)
        f1 = (2 * precision * recall) / (recall + precision)

    return precision, recall, f1, accuracy


def multiclass_accuracy(y_pred, y_true):
    """
    Computes metrics for multiclass classification
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true labels
    Returns:
    accuracy - ratio of accurate predictions to total samples
    """

    true_values = 0
    false_value = 0

    for i, pred in enumerate(y_pred):

        if pred == y_true[i]:
            true_values += 1

        else:
            false_value += 1

    accuracy = true_values / (true_values + false_value)

    return accuracy


def r_squared(y_pred, y_true):
    """
    Computes r-squared for regression
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    r2 - r-squared value
    """

    """
    YOUR CODE IS HERE
    """
    pass


def mse(y_pred, y_true):
    """
    Computes mean squared error
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    mse - mean squared error
    """

    """
    YOUR CODE IS HERE
    """
    pass


def mae(y_pred, y_true):
    """
    Computes mean absolut error
    Arguments:
    y_pred, np array of int (num_samples) - model predictions
    y_true, np array of int (num_samples) - true values
    Returns:
    mae - mean absolut error
    """

    """
    YOUR CODE IS HERE
    """
    pass
    