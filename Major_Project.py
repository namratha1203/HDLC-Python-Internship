import streamlit as st
from PIL import Image
img=Image.open("Image.png")
st.image(img, width=400)

name=st.text_input("Enter Your Name: ","Your Name!")
if(st.button('Submit')):
    result1= name.title()
    st.success(result1)
gender=st.radio("Select Gender: ",('Male','Female','Prefer not to respond'))
if (gender == 'Male'):
    st.success("Male")
elif(gender == 'Female'):
    st.success("Female")
else:
    st.success("Prefer not to respond")
age=st.number_input("Enter your age: ")
address = st.text_input("Enter Your Address: ", "Not more than 50 characters!")
if(st.button('Click here to submit')):
    result3= address.title()
    st.success(result3)
st.write(' ')
st.subheader("Your Hobbies!")         
if st.checkbox("Fostering animals") or st.checkbox("Tutoring") or st.checkbox("Pilates") or st.checkbox("Volleyball") or st.checkbox("Rock climbing") or st.checkbox("Other"):st.text("Selected!")
weight = st.number_input("Enter your weight (in kgs)")
height = st.number_input("Enter your height (in cms)")
try:
    bmi = weight / ((height/100)**2)
except:
    st.text("Enter some value of height")
bmi = weight / ((height/100)**2)
if(st.button('Calculate BMI')):
    st.text("Your BMI Index is {}.".format(bmi))
    if(bmi<16):
        st.error("You are Extremely Underweight")
    elif(bmi>=16 and bmi<18.5):
        st.warning("You are Underweight")
    elif(bmi>=18.5 and bmi<25):
        st.success("Healthy")
    elif(bmi>=25 and bmi<30):
        st.warning("Overweight")
    elif(bmi>=30):
        st.error("Extremely Overweight")
