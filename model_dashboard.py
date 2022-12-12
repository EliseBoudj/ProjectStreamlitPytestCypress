import streamlit as st 
import joblib

@st.cache
def load_model():
    return joblib.load('regression.joblib')


st.title('Prédiction de prix de maison')

taille = st.number_input("Taille maison", value=0)
nb_rooms = st.number_input("Nombre de chambre", value=0)
garden = st.number_input("Y a un jardin", value=0)

model = load_model()

if taille <= 0:
    st.write('mettre taille correcte')
if nb_rooms <= 0:
    st.write("mettre nombre de chambre correct")
if garden != 0 or garden !=1:
    st.write("mettre nombre de chambre correct")



if taille > 0 and nb_rooms > 0:
    
    X = [[taille, nb_rooms, garden]]
    prediction = model.predict(X)
    ## afficher la prediction
    st.write("le prix de la maison est : ")
    st.write(prediction[0].item())

