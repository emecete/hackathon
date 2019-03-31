from conv_porsche import read_data, data_augmentation, train
import pickle
from keras import Sequential

x, y = read_data('dataset_imagenes_instagram', 'dataset.csv')
x, y = data_augmentation(x, y)

model, acc = train(x, y)

print(acc)
print(model)
model.save("model_3103201901.pkl")
filehandler = open("model_3103201901.pkl", 'w')
pickle.dump(model, filehandler)
