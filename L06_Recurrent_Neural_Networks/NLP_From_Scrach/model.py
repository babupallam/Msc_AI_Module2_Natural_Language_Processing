import torch
import torch.nn as nn
from torch.autograd import Variable


# RNN model definition
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size

        # Input to hidden and input to output layers
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)

        # Softmax layer for output
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        # Combine input and hidden state
        combined = torch.cat((input, hidden), 1)

        # Calculate the next hidden state
        hidden = self.i2h(combined)

        # Calculate the output
        output = self.i2o(combined)
        output = self.softmax(output)

        return output, hidden

    def initHidden(self):
        # Initialize the hidden state with zeros
        return Variable(torch.zeros(1, self.hidden_size))
