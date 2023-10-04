import torch
import torch.nn as nn

## Define model ##
# The model defined here is a vanilla Fully Connected Network
class ANNModel(nn.Module):
    def __init__(self, input_dim=96, layer1=32, layer2=48, output_dim=2, dropout_rate=0.5):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, layer1)
        self.fc2 = nn.Linear(layer1, layer2)
        self.fc3 = nn.Linear(layer2, output_dim)
        self.activation = nn.ReLU()
        self.dropout = nn.Dropout(dropout_rate)
        self.batchnorm1 = nn.BatchNorm1d(layer1)
        self.batchnorm2 = nn.BatchNorm1d(layer2)
        self.batch_size = None

    def forward(self, x):
        self.batch_size = x.shape[0]

        x = self.activation(self.fc1(x.view(self.batch_size, -1)))
        x = self.batchnorm1(x)
        x = self.activation(self.dropout(self.fc2(x)))
        x = self.batchnorm2(x)
        x = self.fc3(x)

        return x