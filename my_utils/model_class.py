import torch
from torch import nn


class MLP(nn.Module):
    def __init__(self, in_nums, out_nums, drop_p=0.5):
        super(MLP, self).__init__()
        self.linear_stack = nn.Sequential(
            nn.Linear(in_features=in_nums, out_features=16),
            nn.Dropout(p=drop_p),
            nn.ReLU(),
            nn.Linear(in_features=16, out_features=8),
            nn.Dropout(p=drop_p),
            nn.ReLU(),
            nn.Linear(in_features=8, out_features=out_nums)
        )

    def forward(self, x):
        out = self.linear_stack(x)
        return out


if __name__ == '__main__':
    model = MLP(in_nums=22, out_nums=1, drop_p=0.5)
    print(model)

    input_tensor = torch.rand(4, 22)
    output_tensor = model(input_tensor)

    print(input_tensor)
    print(output_tensor)
    # print(output_tensor.argmax(1))
