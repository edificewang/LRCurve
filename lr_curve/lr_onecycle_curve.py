import torch
import torch.optim as optim
from torch.optim import lr_scheduler
from torchvision.models import resnet18
import matplotlib.pyplot as plt

model = resnet18(num_classes=2)
lr=0.05
optimizer = optim.SGD(params=model.parameters(), lr=lr)
scheduler = lr_scheduler.OneCycleLR(optimizer,max_lr=lr,total_steps=100)

plt.figure()
x = list(range(100))
y = []
for epoch in range(100):
    scheduler.step()
    lr = scheduler.get_lr()
    # print(epoch, scheduler.get_lr()[0])    # get_lr()
    y.append(scheduler.get_lr()[0])
plt.plot(x, y)
plt.savefig('lr_onecycle.png')