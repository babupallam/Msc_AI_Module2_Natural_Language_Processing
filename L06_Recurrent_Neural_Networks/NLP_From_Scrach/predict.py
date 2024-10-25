from model import *
from data import *
import sys

# Load the trained model
rnn = torch.load('char-rnn-classification.pt')


# Evaluate the model with a given input line (name)
def evaluate(line_tensor):
    hidden = rnn.initHidden()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    return output


# Predict top N categories for a given name
def predict(line, n_predictions=3):
    output = evaluate(Variable(lineToTensor(line)))

    # Get top N categories
    topv, topi = output.data.topk(n_predictions, 1, True)
    predictions = []

    for i in range(n_predictions):
        value = topv[0][i]
        category_index = topi[0][i]
        print('(%.2f) %s' % (value, all_categories[category_index]))
        predictions.append([value, all_categories[category_index]])

    return predictions


# Run prediction from command line
if __name__ == '__main__':
    predict(sys.argv[1])
