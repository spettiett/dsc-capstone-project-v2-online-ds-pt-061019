from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def print_metrics(labels, preds, TN, TP, FN, FP, numObsv):
    '''
    Purpose: Print Performance Metrics
    '''
    print(f'Precision Score: {precision_score(labels, preds)}')
    print(f'Specificity: {TN / (TN+FP)}')  # True Negative Rate
    print(f'Recall Score: {recall_score(labels, preds)}')  # True Positive Rate
    print(f'Accuracy Score: {accuracy_score(labels, preds)}')
    print(f'F1 Score: {f1_score(labels, preds)}')
    print(f'Misclassification Rate: {(1 - accuracy_score(labels, preds))}')
    print(f'_________ \n')

    print(f'Among {numObsv} observations our model is predicting {TP+FP} canceled. \nIn actual,  {TP+FN} have canceled and among those, the model identified {TP} correctly.\n')

    print(f'True  Positive: {TP}.  The model has predicted the positive (1) case, correctly.')
    print(f'True  Negative: {TN}.  The model has predicted the negative case (0), correctly.')
    print(f'False Positive: {FP}.  The model has predicted these customers would cancel, but in actual they do not cancel -- Type I Error.')
    print(f'False Negative: {FN}.  The model has predicted these customers will not cancel, but in actual they do cancel -- Type II Error.')

    print(f'*_Accuracy Score:  {(TP+TN)/(TP+FP+TN+FN)} is the accuracy of the predicton model.')
    print(f'*_Precision Score: {TP/(TP+FP)} is the measure of the accuracy of the model in predicting that a customer will cancel the booking.')
    print(f'Sensitivity (Recall) Score: {TP/(TP+FN)} of the cancellations are correctly identified as been canceled -- True Postive Rate.')
    print(f'Specificity Score:          {TN/(TN+FP)} of the successful bookings are correctly identified as not been canceled -- True Negative Rate.')
