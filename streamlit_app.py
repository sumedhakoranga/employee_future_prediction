import pandas as pd
import pickle
import streamlit as st


def prediction(input):
    return model.predict(input)[0]


def main():
    st.title('Employee Future Prediction')

    html_temp = """
	<div style ="background-color:blue;padding:13px">
	<h1 style ="color:white;text-align:center;">Employee Future Prediction App </h1>
	</div>
	"""

    st.markdown(html_temp, unsafe_allow_html=True)

    education = st.selectbox('Education', ('Bachelors', 'Masters', 'PHD'))
    joining_year = st.text_input(
        'Joining Year', '')
    city = st.selectbox('City', ('Bangalore', 'New Delhi', 'Pune'))
    payment_tier = st.selectbox('Payment Tier', ('1', '2', '3'))
    age = st.text_input('Age', '')
    gender = st.selectbox('Gender', ('Male', 'Female'))
    ever_benched = st.selectbox('Ever Benched?', ('Yes', 'No'))
    experience = st.text_input('Experience in Current Domain', '')

    leave = None
    if st.button('Predict'):
        leave = prediction(
            pd.DataFrame({
                'Education': education,
                'JoiningYear': int(joining_year),
                'City': city,
                'PaymentTier': int(payment_tier),
                'Age': int(age),
                'Gender': gender,
                'EverBenched': ever_benched,
                'ExperienceInCurrentDomain': int(experience)
            }, index=[0])
        )

    if leave == None:
        pass
    elif leave == 0:
        st.success('The Employee will stay in the company.')
    else:
        st.success('The Employee will leave in the next two years.')


if __name__ == '__main__':
    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)

    main()
