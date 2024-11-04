from tensorflow.keras.models import load_model
import util.sample_reader as sr

model = load_model("models/saved_model.h5")

seismograms = sr.read("training_data.txt")[0]
seismogram = seismograms[0]

predictions = model.predict(seismogram)

print(predictions)