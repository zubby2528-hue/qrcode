import streamlit as st
import qrcode
from PIL import Image

st.title(" qr code gen")
data=st.text_input("enter url:")
if st.button("generated qr"):
  if data:
    qr=qrcode.make(data)
    qr.save("qr.png")

    img=Image.open("qr.png")
    st.image(img,caption="gen qr codr")

    with open("qr.png","rb") as f:
          st.download_button("download qr", f, file_name="qr.png")
  else:
    st.warning("please enter some txt:")
