class ConvAutoencoder(nn.Module):
    def __init__(self):
        super(ConvAutoencoder, self).__init__()

        self.cnn_layers = nn.Sequential(
            nn.Conv2d(3, 16, 3, 2, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2, 0),

            nn.Conv2d(16, 32, 3, 2, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2, 0),

        )
        self.fc_layers = nn.Sequential(
            nn.Linear(2048, 256),
            nn.ReLU(),
            nn.Linear(256, 64),
            nn.ReLU(),            
            nn.Linear(64, 1)
        )

    def forward(self, x):
        x = self.cnn_layers(x)
        x = x.flatten(1)
        x = self.fc_layers(x)
        return x

 class ConvAutoencoder(nn.Module):
    def __init__(self):
        super(ConvAutoencoder, self).__init__()

        self.cnn_layers = nn.Sequential(
            nn.Conv2d(3, 16, 3, 3, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2, 0),

            nn.Conv2d(16, 32, 3, 3, 1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2, 0),

        )
        self.fc_layers = nn.Sequential(
            nn.Linear(288, 256),
            nn.ReLU(),
            nn.Linear(256, 64),
            nn.ReLU(),            
            nn.Linear(64, 1)
        )

    def forward(self, x):
        x = self.cnn_layers(x)
        x = x.flatten(1)
        x = self.fc_layers(x)
        return x 