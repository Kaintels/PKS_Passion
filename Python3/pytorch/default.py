import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.modules
import torch.nn.functional as F
from torchsummary import summary
import torch.optim as optim

use_cuda = torch.cuda.is_available()
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv1d(10, 2, kernel_size=1)
        self.conv2 = nn.Conv1d(2, 10, kernel_size=1)
        self.fc1 = nn.Linear(4, 1)
        self.pool = nn.MaxPool1d(1)
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 4) # flatten layer
        x = F.relu(self.fc1(x))
        x = F.log_softmax(x, dim=-1)
        print(np.shape(x))
        return x

model = Net().cuda()
print(torch.cuda.get_device_name())
summary(model, (10, 20))

