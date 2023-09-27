import torch

X = torch.tensor([1, 2, 3, 4])
Y = torch.tensor([3, 6, 9, 12])

w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

def forward(x):
    return w * x


def loss(y, y_pred):
    return ((y_pred - y)**2).mean()

print("Weight before training: ",w)

# Training
learning_rate = 0.01
n_iters = 100

for train in range(n_iters):
    # predict = forward pass
    y_pred = forward(X)

    # loss
    l = loss(Y, y_pred)

    # calculate gradients = backward pass
    l.backward()

    # update weights
    #w.data = w.data - learning_rate * w.grad
    with torch.no_grad():
        w -= learning_rate * w.grad
    
    # zero the gradients after updating
    w.grad.zero_()

    if train % 20 == 0:
        print(f'Train {train+1}: w = {w.item():.3f}, loss = {l.item():.5f}')

print("Weight after training: ",(w))

