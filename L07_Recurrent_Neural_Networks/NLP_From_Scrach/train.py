import torch
from data import *
from model import *
import random
import time
import math

# Set hyperparameters
n_hidden = 128
n_epochs = 100000
print_every = 5000
plot_every = 1000
learning_rate = 0.005

# Function to get category from model output
def categoryFromOutput(output):
    top_n, top_i = output.data.topk(1)  # Get top predicted category
    category_i = top_i[0][0]
    return all_categories[category_i], category_i


# Function to randomly select an item from a list (fix for the error)
def randomChoice(l):
    return l[random.randint(0, len(l) - 1)]

# Function to pick a random training pair
def randomTrainingPair():
    category = randomChoice(all_categories)
    line = randomChoice(category_lines[category])
    category_tensor = Variable(torch.LongTensor([all_categories.index(category)]))
    line_tensor = Variable(lineToTensor(line))
    return category, line, category_tensor, line_tensor

# Initialize RNN model, optimizer, and loss function
rnn = RNN(n_letters, n_hidden, n_categories)
optimizer = torch.optim.SGD(rnn.parameters(), lr=learning_rate)
criterion = nn.NLLLoss()

# Train the model
def train(category_tensor, line_tensor):
    hidden = rnn.initHidden()
    optimizer.zero_grad()

    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    loss = criterion(output, category_tensor)
    loss.backward()
    optimizer.step()

    return output, loss.item()

# Track losses for plotting
current_loss = 0
all_losses = []

# Timing helper function
def timeSince(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

# Start training loop
start = time.time()
for epoch in range(1, n_epochs + 1):
    category, line, category_tensor, line_tensor = randomTrainingPair()
    output, loss = train(category_tensor, line_tensor)
    current_loss += loss

    # Print every 'print_every' steps
    if epoch % print_every == 0:
        guess, guess_i = categoryFromOutput(output)
        correct = '✓' if guess == category else '✗ (%s)' % category
        print(f'{epoch} {epoch / n_epochs * 100}% ({timeSince(start)}) {loss:.4f} {line} / {guess} {correct}')

    # Add current loss to plot every 'plot_every' steps
    if epoch % plot_every == 0:
        all_losses.append(current_loss / plot_every)
        current_loss = 0

# Save the trained model
torch.save(rnn, 'char-rnn-classification.pt')
