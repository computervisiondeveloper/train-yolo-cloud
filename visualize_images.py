import os

import matplotlib.pyplot as plt
import cv2


imgs_dir = '/home/phillip/Desktop/todays_tutorial/14_train_custom_yolo/data/train/imgs'
anns_dir = '/home/phillip/Desktop/todays_tutorial/14_train_custom_yolo/data/train/anns'

for j in os.listdir(imgs_dir):
	filename = os.path.join(imgs_dir, j)
	img = cv2.imread(filename)
	H, W, _ = img.shape
	
	ann_file = open(os.path.join(anns_dir, j[:-4] + '.txt'), 'r')
	line = [l[:-1] for l in ann_file.readlines() if len(l) > 1][0]
	ann_file.close()

	line = [float(l) for l in line.split(' ')]

	img = cv2.rectangle(img, (int(W * (line[1] - line[3] / 2)), int(H * (line[2] - line[4] / 2))),
						(int(W * (line[1] + line[3] / 2)), int(H * (line[2] + line[4] / 2))), (0, 255, 0), 3)

	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	plt.imshow(img)
	mng = plt.get_current_fig_manager()
	mng.resize(*mng.window.maxsize())
	plt.show()
