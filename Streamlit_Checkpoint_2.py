import streamlit as st
import pickle
import numpy as np

import gzip
# Load model with gzip decompression
with gzip.open('Financial.pkl.gz', 'rb') as f:
    model = pickle.load(f)

# Créer une fonction pour faire la prédiction
def predict_financial(country, year, bank_account, location_type, cellphone_access, household_size, age_of_respondent,
                      gender_of_respondent, relationship_with_head, marital_status, education_level):
    # Créer un tableau numpy à partir des entrées de l'utilisateur
    input_data = np.array([[country, year, bank_account, location_type, cellphone_access, household_size,
                            age_of_respondent, gender_of_respondent, relationship_with_head, marital_status,
                            education_level]])
    # Effectuer la prédiction avec le modèle
    prediction = model.predict(input_data)
    return prediction


# Mappage des codes aux colonnes
country_mapping = {
    1: 'Kenya', 2: 'Rwanda', 3: 'Tanzania', 4: 'Uganda'
}

bank_account_mapping = {
    1: 'Yes', 2: 'No'
}

location_type_mapping = {
    1: 'Rural', 2: 'Urban'
}

cellphone_access_mapping = {
    1: 'Yes', 2: 'No'
}

gender_of_respondent_mapping = {
    1: 'Female', 2: 'Male'
}

relationship_with_head_mapping = {
    1: 'Spouse', 2: 'Head of Household', 3: 'Other relative', 4: 'Child', 5: 'Parent', 6: 'Other non-relatives'
}

marital_status_mapping = {
    1: 'Married/Living together', 2: 'Widowed', 3: 'Single/Never Married', 4: 'Divorced/Separated', 5: 'Dont know'
}

education_level_mapping = {
    1: 'Secondary education', 2: 'No formal education', 3: 'Vocational/Specialised training',
    4: 'Primary education', 5: 'Tertiary education', 6: 'Other/Dont know/RTA'
}

job_type_mapping = {
    1: 'Self employed', 2: 'Government Dependent', 3: 'Formally employed Private', 4: 'Informally employed',
    5: 'Formally employed Government', 6: 'Farming and Fishing', 7: 'Remittance Dependent', 8: 'Other Income',
    9: 'Dont Know/Refuse to answer', 10: 'No Income'
}

# Interface Streamlit
st.title('Prédiction du Financial Inclusion')
st.header('Remplissez le formulaire ci-dessous pour prédire le type d\'emploi')

# Créer le formulaire pour collecter les entrées de l'utilisateur
country = st.selectbox('Sélectionnez la région', options=list(country_mapping.keys()),
                       format_func=lambda x: country_mapping[x], key='country')
year = st.number_input('Entrez l\'année:', min_value=1900, max_value=2100, value=2024, step=1, key='year')
bank_account = st.selectbox('Avez-vous un compte bancaire ?', options=list(bank_account_mapping.keys()),
                            format_func=lambda x: bank_account_mapping[x], key='bank_account')
location_type = st.selectbox('Type de localisation:', options=list(location_type_mapping.keys()),
                             format_func=lambda x: location_type_mapping[x], key='location_type')
cellphone_access = st.selectbox('Avez-vous un téléphone portable ?', options=list(cellphone_access_mapping.keys()),
                                format_func=lambda x: cellphone_access_mapping[x], key='cellphone_access')
household_size = st.number_input('Taille du ménage:', min_value=1, max_value=20, value=1, step=1, key='household_size')
age_of_respondent = st.number_input('Âge du répondant:', min_value=0, max_value=120, value=30, step=1,
                                    key='age_of_respondent')
gender_of_respondent = st.selectbox('Genre du répondant:', options=list(gender_of_respondent_mapping.keys()),
                                    format_func=lambda x: gender_of_respondent_mapping[x], key='gender_of_respondent')
relationship_with_head = st.selectbox('Relation avec le chef de ménage:',
                                      options=list(relationship_with_head_mapping.keys()),
                                      format_func=lambda x: relationship_with_head_mapping[x],
                                      key='relationship_with_head')
marital_status = st.selectbox('État matrimonial:', options=list(marital_status_mapping.keys()),
                              format_func=lambda x: marital_status_mapping[x], key='marital_status')
education_level = st.selectbox('Niveau d\'éducation:', options=list(education_level_mapping.keys()),
                               format_func=lambda x: education_level_mapping[x], key='education_level')

# Bouton pour prédire
if st.button('Prédire', key='predict'):
    # Faire la prédiction
    result = predict_financial(country, year, bank_account, location_type, cellphone_access, household_size,
                               age_of_respondent, gender_of_respondent, relationship_with_head, marital_status,
                               education_level)

    # Convertir la prédiction en valeur lisible
    job_type_result = job_type_mapping.get(result[0], 'Inconnu')

    # Afficher le résultat
    st.write(f'Le type d\'emploi prédit est : {job_type_result}')
