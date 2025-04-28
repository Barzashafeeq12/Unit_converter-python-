import streamlit as st
st.title("Unit Converter App")
st.markdown("### Convert Length ,Time ,Weight and Mass Instantly")
st.write("* Welcome! Choose the category.")
st.write("* Enter the Value.")
st.write("* Get the Result in Real Time.")
catagary =st.selectbox("Choose a catagary",["Length","Time","Weight"])

def convertUnit (catagary,value,unit):
    if catagary == "Length":
     if unit == "Kilometers to Miles":
        return value * 0.621371
     elif unit == "Miles to Kilometers":
        return value / 0.621371
     elif catagary == "Weight":
         if unit == "Kilograms to pounds":
          return value  * 2.20462
         if unit == "Pounds to kilograms":
          return value  / 2.20462
     elif catagary == "Time":
         if unit == "Seconds to minutes":
          return value  / 60
     elif unit == "Minutes to seconds":
          return value  * 60
     elif unit == "Hours to days":
          return value  / 24
     elif unit == "Days to hours":
          return value  * 24
     elif unit == "Minutes to hours":
          return value  / 60
     elif unit == "Hours to minutes":
          return value  * 60
    return 0

if catagary == "Length":
   unit = st.selectbox("Choose a Conversion",["Miles to Kilometers","Kilometers to Miles"])
elif catagary == "Weight":
        unit = st.selectbox("Choose a Conversion",["Kilograms to pounds","Pounds to kilograms"])
elif catagary == "Time":
        unit = st.selectbox("Choose a Conversion",["Seconds to minutes","Minutes to seconds","Hours to days", "Days to hours","Minutes to hours","Hours to minutes"])

value = st.number_input("Enter the value to convert")  
if st.button("Convert"):
        result = convertUnit(catagary,value,unit)
        st.success(f"The Result is {result:.2f}")

    
    