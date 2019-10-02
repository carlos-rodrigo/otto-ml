import sys
import settings
from models import model

if __name__ == '__main__':
    settings.setup()
    model.train_model()
