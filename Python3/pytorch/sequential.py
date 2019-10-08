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
        self.model = nn.Sequential(
            nn.Conv1d(10, 2, kernel_size=1),
            nn.MaxPool1d(1),
            nn.Conv1d(2, 1, kernel_size=1),
            nn.Linear(20, 1),
            nn.MaxPool1d(1),
            nn.Linear(1, 1)
        )
    def forward(self, x):
        x = self.model(x)
        x = x.view(-1, 2)
        x = F.log_softmax(x, dim=-1)
        print(np.shape(x))
        return x
    
model = Net().cuda()
print(model)
print(torch.cuda.get_device_name())
summary(model, (10, 20))
