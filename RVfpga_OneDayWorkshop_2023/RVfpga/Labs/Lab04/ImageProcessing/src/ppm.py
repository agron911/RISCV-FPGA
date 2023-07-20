from PIL import Image
import numpy as np
im = Image.open("../AdditionalFiles/TheScream_256.ppm")
np_im = np.array(im)
new_im = Image.fromarray(np_im)
new_im.save("../AdditionalFiles/TheScream_256.png")