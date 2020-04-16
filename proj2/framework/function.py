import math


def tanh(x):
    return 2.0/(1.0 + (-2*x).exp()) - 1


def mse(x, y):
    return (x-y).pow(2).sum() / x.nelement()


def softmax(x):
    x_exp = (x - x.max(1)[0].view(-1, 1)).exp()
    return x_exp / x_exp.sum(1).view(-1, 1)


def xavier_normal_(x, gain=1):
    # for gain see https://pytorch.org/docs/stable/nn.init.html#torch.nn.init.calculate_gain
    std = gain * math.sqrt(2.0/sum(x.shape))
    return x.normal_(0, std)

