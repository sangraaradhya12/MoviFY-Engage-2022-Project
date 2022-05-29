import streamlit as st
import streamlit_authenticator as stauth

names = ['Administrator']
usernames = ['admin']
passwords = ['123']

hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
