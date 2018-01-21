"""
    ----------------------------------------------------------------------------------------
    AndroidAppClassifier (training_file, testing_file, split_data=False, group_game=False):
    ----------------------------------------------------------------------------------------
    This classifier, classifies Android apps on Google Play to appropriate categories,
    using Naive Bayes Classifier (MultinomialNB and BernoulliNB)

    Parameters
    ----------
    training_file : string
        The training file for the classifier

    testing_file : string
        The testing file for the classifier

    split_data : boolean
        If True, the classifier uses the training file alone and splits the file into two
        (n,n), using one as the training set and the other as the testing set. The split
        value is adjusted manually

        If false, the classifier uses the training file and test file specified

   """
