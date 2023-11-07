import streamlit as st
from encrypt import encrypt
from decrypt import decrypt

# st.header("S-DES Encryption and Decryption")
st.markdown(f'<p style="font-size: 50px; text-align : center; font-weight : bold; ">CycloCrypt</p>', unsafe_allow_html=True)

choice = st.radio("Choose an option:", ("Encrypt", "Decrypt"))

if choice == "Encrypt":
    user_input = st.text_input("Text to encrypt")
    k1 = st.text_input("Enter k1(Alphanumeric)")
    k2 = st.text_input("Enter k2(Numreic)")

    if st.button("Encrypt"):
        encrypted_text = encrypt(user_input, k1, int(k2))
        # st.write("Encrypted text is:", encrypted_text)
        st.markdown(f'<p style="font-size: 30px; text-align : center;">Encrypted text is: {encrypted_text}</p>', unsafe_allow_html=True)

elif choice == "Decrypt":
    user_input = st.text_input("Text to decrypt")
    k1 = st.text_input("Enter k1(Alphanumeric)")
    k2 = st.text_input("Enter k2(Numreic)")

    if st.button("Decrypt"):
        decrypted_text = decrypt(user_input, k1, int(k2))
        st.markdown(f'<p style="font-size: 30px; text-align : center;">Encrypted text is: {decrypted_text}</p>', unsafe_allow_html=True)
        # st.write("Decrypted text is:", )
