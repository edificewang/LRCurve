import torch
import torch.optim as optim
from torch.optim import lr_scheduler
from torchvision.models import resnet18
import matplotlib.pyplot as plt

model = resnet18(num_classes=2)
optimizer = optim.SGD(params=model.parameters(), lr=0.05)
multi_steps=[30,25,70,90]
scheduler = lr_scheduler.MultiStepLR(optimizer,milestones=multi_steps, gamma=0.1)
plt.figure()
x = list(range(100))
y = []
for epoch in range(100):
    scheduler.step()
    lr = scheduler.get_lr()
    # print(epoch, scheduler.get_lr()[0])    # get_lr()
    y.append(scheduler.get_lr()[0])
plt.plot(x, y)
plt.savefig('lr_multistep.png')