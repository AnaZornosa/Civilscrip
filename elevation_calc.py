import streamlit as st

def calculate_offset(navdoo, rim):
    offset = navdoo - rim
    feet = int(offset)
    inches = (offset - feet) * 12
    whole_inches = int(inches)
    fraction_inches = (inches - whole_inches) * 100
    return feet, whole_inches, fraction_inches

st.title("Elevation Offset Calculator")

ffe = st.number_input("Enter the FFE (Finish Floor Elevation) in NAVD88:")
catch_basin = st.number_input("Enter the catch basin or Storm Manhole Elevation (RIM) in NAVD88:")

if st.button("Calculate Offset"):
    feet, whole_inches, fraction_inches = calculate_offset(ffe, catch_basin)
    st.write(f"Offset: {feet}' {whole_inches}\" {fraction_inches:.2f}''")