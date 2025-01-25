from osgeo import gdal
import numpy as np
import os
import  cv2

path = 'your path'


fileList = os.listdir(path)

for i in range(len(fileList)):
    dataset = gdal.Open(os.path.join(path,fileList[i]))
    im_width = dataset.RasterXSize
    im_height = dataset.RasterYSize
    image = dataset.ReadAsArray(0, 0, im_width, im_height).astype(np.float64)
    del dataset
    print(image.shape)

    image = image / 5 * 255
    cv2.imwrite(os.path.join('your path',fileList[i]),image)
