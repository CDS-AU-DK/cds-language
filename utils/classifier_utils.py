#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate, ShuffleSplit, learning_curve

# Function for balancing datasets using pandas
def balance(dataframe, n=500):
    """
    Create a balanced sample from imbalanced datasets.
    
    dataframe: 
        Pandas dataframe with a column called 'text' and one called 'label'
    n:         
        Number of samples from each label, defaults to 500
    """
    # Use pandas select a random bunch of examples from each label
    out = (dataframe.groupby('label', as_index=False)
            .apply(lambda x: x.sample(n=n))
            .reset_index(drop=True))
    
    return out

# Show the most informative features
def show_features(vectorizer, training_labels, classifier, n=20):
    """
    Return the most informative features from a classifier, i.e. the 'strongest' predictors.
    
    vectorizer:
        A vectorizer defined by the user, e.g. 'CountVectorizer'
    classifier:
        A classifier defined by the user, e.g. 'MultinomialNB'
    n:
        Number of features to display, defaults to 20
        
    """
    # Get feature names and coefficients
    feature_names = vectorizer.get_feature_names()
    coefs_with_fns = sorted(zip(classifier.coef_[0], feature_names))
    # Get ordered labels
    labels = sorted(set(training_labels))
    # Select top n results, where n is function argument
    top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
    # Pretty print columns showing most informative features
    print(f"{labels[0]}\t\t\t\t{labels[1]}\n")
    for (coef_1, fn_1), (coef_2, fn_2) in top:
        for (coef_1, fn_1), (coef_2, fn_2) in top:
            print("%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))

    return None

# Create an ROC plot to evaluate classifier
def plot_ROC(fpr, tpr, AUC):
    """
    Create an 'ROC' plot, used to evaluate the accuracy of a classifier.
    
    fpr:
        False positive rate, calculated by the user
    tpr:
        True positive rate, calculated by the user
    AUC:
        'Area under curve', calculated by the user
    """
    # Create standard ROC plot from defined values
    ax = plt.plot(fpr, tpr, color='red', label = (f'AUC = {AUC}'))
    # Plot diagonal from (0,0) to (1,1)
    plt.plot([0,1],[0,1], color = 'lightgrey',linestyle = '--')
    # Add title; add labels for x and y axes; add legend
    plt.title('ROC')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend(loc = 'lower right')
    # Show plot
    plt.show()

    return None

# Create heatmap visualisation
def plot_cm(y_test, y_pred, normalized:bool):
    """
    Plot confusion matrix
    """
    if normalized == False:
        cm = pd.crosstab(y_test, y_pred, 
                            rownames=['Actual'], colnames=['Predicted'])
        p = plt.figure(figsize=(10,10));
        p = sns.heatmap(cm, annot=True, fmt="d", cbar=False)
    elif normalized == True:
        cm = pd.crosstab(y_test, y_pred, 
                               rownames=['Actual'], colnames=['Predicted'], normalize='index')
        p = plt.figure(figsize=(10,10));
        p = sns.heatmap(cm, annot=True, fmt=".2f", cbar=False)

        return None
    
# Plot learning-validation curve
def plot_learning_curve(estimator, title, X, y, axes=None, ylim=None, cv=None,
                        n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    """
    Function taken from sklearn documentation
    
    Generate 3 plots: the test and training learning curve, the training
    samples vs fit times curve, the fit times vs score curve.

    Parameters
    ----------
    estimator : estimator instance
        An estimator instance implementing `fit` and `predict` methods which
        will be cloned for each validation.

    title : str
        Title for the chart.

    X : array-like of shape (n_samples, n_features)
        Training vector, where ``n_samples`` is the number of samples and
        ``n_features`` is the number of features.

    y : array-like of shape (n_samples) or (n_samples, n_features)
        Target relative to ``X`` for classification or regression;
        None for unsupervised learning.

    axes : array-like of shape (3,), default=None
        Axes to use for plotting the curves.

    ylim : tuple of shape (2,), default=None
        Defines minimum and maximum y-values plotted, e.g. (ymin, ymax).

    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

          - None, to use the default 5-fold cross-validation,
          - integer, to specify the number of folds.
          - :term:`CV splitter`,
          - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : int or None, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    train_sizes : array-like of shape (n_ticks,)
        Relative or absolute numbers of training examples that will be used to
        generate the learning curve. If the ``dtype`` is float, it is regarded
        as a fraction of the maximum size of the training set (that is
        determined by the selected validation method), i.e. it has to be within
        (0, 1]. Otherwise it is interpreted as absolute sizes of the training
        sets. Note that for classification the number of samples usually have
        to be big enough to contain at least one sample from each class.
        (default: np.linspace(0.1, 1.0, 5))
    """
    if axes is None:
        _, axes = plt.subplots(1, 3, figsize=(20, 5))

    axes[0].set_title(title)
    if ylim is not None:
        axes[0].set_ylim(*ylim)
    axes[0].set_xlabel("Training examples")
    axes[0].set_ylabel("Score")

    train_sizes, train_scores, test_scores, fit_times, _ = \
        learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs,
                       train_sizes=train_sizes,
                       return_times=True)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    fit_times_mean = np.mean(fit_times, axis=1)
    fit_times_std = np.std(fit_times, axis=1)

    # Plot learning curve
    axes[0].grid()
    axes[0].fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
    axes[0].fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1,
                         color="g")
    axes[0].plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
    axes[0].plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Cross-validation score")
    axes[0].legend(loc="best")

    # Plot n_samples vs fit_times
    axes[1].grid()
    axes[1].plot(train_sizes, fit_times_mean, 'o-')
    axes[1].fill_between(train_sizes, fit_times_mean - fit_times_std,
                         fit_times_mean + fit_times_std, alpha=0.1)
    axes[1].set_xlabel("Training examples")
    axes[1].set_ylabel("fit_times")
    axes[1].set_title("Scalability of the model")

    # Plot fit_time vs score
    axes[2].grid()
    axes[2].plot(fit_times_mean, test_scores_mean, 'o-')
    axes[2].fill_between(fit_times_mean, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1)
    axes[2].set_xlabel("fit_times")
    axes[2].set_ylabel("Score")
    axes[2].set_title("Performance of the model")

    plt.show()
    
    return None

if __name__=="__main__":
    pass