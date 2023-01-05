import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import messages



def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Crypto Recover", page_icon=":key:", layout="wide")
local_css("style/style.css")

selected = option_menu(
        menu_title=None,
        options = ["Crypto Recover", "FAQ", "Contact Us", "Legal Notice"],
        icons=["key", "question-lg", "envelope", "shield-check"],
        menu_icon="case",
        default_index=0,
        orientation="horizontal"
    )


if selected == "Crypto Recover":
    with st.container():
        st.title("Regain access to your crypto wallet")
        st.write(messages.main_1)

        lottie = load_lottie("https://assets5.lottiefiles.com/packages/lf20_O1b0iWuPju.json")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write(messages.main_2)
        with right_column:
            st_lottie(lottie, height=500, width=600, key="Crypto")


elif selected == "FAQ":
    with st.container():
        st.title("Frequently Asked Questions")

        lottie = load_lottie("https://assets3.lottiefiles.com/packages/lf20_ssIwdK.json")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write('* Which wallets are supported?')
            st.write(messages.faq_1)
            st.write('* How much does the software cost?')
            st.write(messages.faq_3)
            st.write('* Is it safe?')
            st.write(messages.faq_4)
            st.write('* How much time will it take to recover my password?')
            st.write(messages.faq_2)
        with right_column:
            st.write('')
            st.write('')
            st.write('')
            st_lottie(lottie, height=600, width=600, key="Crypto")

elif selected == "Contact Us":
    with st.container():
        
        left_column, right_column = st.columns(2)
        with left_column:
            st.title("How to Find Us")
            st.write(messages.contact_1)

            st.header('Headquarters')
            st.write('Winkelriedstrasse 7, 3014 Bern, Switzerland')
            st.write('Phone: 0272511027')
            st.write('Email: support@cryptorecover.guru')
            
        with right_column:
            st.title("Get in touch")
            st.markdown(messages.contact_form,unsafe_allow_html=True)
    
    
elif selected == "Legal Notice":
    with st.container():
        st.title("Terms and Conditions")
        st.header('General Terms')
        st.write(messages.terms_1)
        st.header('Rights to the Software')
        st.write(messages.terms_2)
        st.header('Restrictions on the use of the Software.')
        st.write(messages.terms_3)

        st.write('---')

        st.title("Privacy Policy")
        st.header('Introduction')
        st.write(messages.privacy_policy_1)
        st.header('Legal basis for processing your personal data')
        st.write(messages.privacy_policy_2)
        st.header('What personal data do we use')
        st.write(messages.privacy_policy_3)
        st.header('Processing of your personal data')
        st.write(messages.privacy_policy_5)
        st.header('Payment services of third parties')
        st.write(messages.privacy_policy_7)
        st.header('Your rights regarding the personal data you provide to us')
        st.write(messages.privacy_policy_8)
        st.header('Exercising your rights')
        st.write(messages.privacy_policy_9)
        st.header('Data deletion')
        st.write(messages.privacy_policy_10)
        st.header('Changes to this Privacy Policy')
        st.write(messages.privacy_policy_11)



        

         





        #legal notice no guarantee




st.markdown(messages.footer,unsafe_allow_html=True)
