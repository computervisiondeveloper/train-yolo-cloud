import os

import cv2


anns_dir = '/home/phillip/Desktop/todays_tutorial/14_train_custom_yolo/data/train/anns'
imgs_dir = '/home/phillip/Desktop/todays_tutorial/14_train_custom_yolo/data/train/imgs'

output_file = '/home/phillip/Desktop/todays_tutorial/14_train_custom_yolo/data/data_train.csv'

with open(output_file, 'w') as f:

    for j in os.listdir(anns_dir):
        img = cv2.imread(os.path.join(imgs_dir, j[:-4] + '.jpg'))
        H, W, _ = img.shape

        with open(os.path.join(anns_dir, j)) as fr:
            line = [l[:-1] for l in fr.readlines() if len(l) > 1][0]
            line = [float(l) for l in line.split(' ')]
            x1, y1, x2, y2 = int(W * (line[1] - line[3] / 2)), int(H * (line[2] - line[4] / 2)), \
                                int(W * (line[1] + line[3] / 2)), int(H * (line[2] + line[4] / 2))

            filename = '/home/ubuntu/TrainYourOwnYOLO/data/train/imgs/{}'.format(j[:-4] + '.jpg')

            f.write('{} {},{},{},{},{}\n'.format(filename, x1, y1, x2, y2, 0))

    f.close()
