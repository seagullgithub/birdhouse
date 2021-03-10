import numpy as np
import cv2
from datetime import datetime

def take_snapshot():
    dt = datetime.now(tz=None)
    timestamp = dt.strftime("%Y-%m-%d_%H-%M-%S")

    img = np.random.randint(0, 255, (100,150))

    cv2.imwrite('birdhouse_' + str(timestamp) + '.png',img)

    return True
