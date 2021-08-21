import streamlit as st
from PIL import Image
import pickle
import numpy as np
pickle_in = open("forest_model1.pkl", "rb")
model = pickle.load(pickle_in)


def main():
    img=Image.open('Billboard_Hot_100.jpg')
    img=img.resize((267,176))
    st.image(img, use_column_width=False)
    st.title("BillBoard Hit Predictor")
    st.text("Team B")


    songname = st.text_input("song name")

    instrumentalness = st.number_input("instrumentalness")

    acousticness= st.number_input("acousticness")

    duration_s = st.number_input("duration_s")

    energy = st.number_input("energy")

    loudness = st.number_input("loudness")

    liveness = st.number_input("liveness")

    valence = st.number_input("valence")

    danceability = st.number_input("danceability")

    Key = st.number_input("Key")

    speechiness = st.number_input("speechiness")

    tempo = st.number_input("tempo")

    mode = st.number_input("mode")

    if st.button("Submit"):
        duration_ms = duration_s * 1000
        duration_ms = np.log(duration_ms)

        if mode == 0:
            Key_mode_ratio = 0
        else:
            Key_mode_ratio = float(Key / mode)
        prediction = model.predict([[danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness,valence, tempo,Key_mode_ratio,duration_ms]])
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))

        if ans == 0:
          st.error("The song "+songname+" will not be a Billboard Hit")
        else:
          st.success("The song "+songname+" will be a Billboard Hit")

if __name__=='__main__':
    main()
