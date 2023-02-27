import numpy as np
import os

def create_fake_data():
    for i in range(80):
        img_directory = "C:/Users/Edward/Desktop/Palette-Image-to-Image-Diffusion-Models/datasets/FakeVolumes/images"
        flist_directory = "C:/Users/Edward/Desktop/Palette-Image-to-Image-Diffusion-Models/datasets/FakeVolumes/flist"
        if not os.path.exists(img_directory):
            os.makedirs(img_directory)

        if not os.path.exists(flist_directory):
            os.makedirs(flist_directory)

        random_data = np.random.rand(4, 16, 16, 16)
        #np.save("Data\\TrainingData\\" + str(i) + ".npy", random_data)
        np.save(os.path.join(img_directory, str(i) + ".npy"), random_data)

    train_names = range(0, int(0.8 * i) - 1)
    test_names = range(int(0.8 * i), i)

    file = open(os.path.join(flist_directory, "train.flist"), 'w')
    for items in train_names:
        file.writelines(str(items) + ".npy" + '\n')
    file.close()
    file = open(os.path.join(flist_directory, "test.flist"), 'w')
    for items in test_names:
        file.writelines(str(items) + ".npy" + '\n')
    file.close()

create_fake_data()

if __name__ == '__main__':
    create_fake_data()