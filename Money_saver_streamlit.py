# it's actually an application in malagasy with the output
# But the whole code here is in english for more accessibility in calling variable

import streamlit as st

if "necessities" not in st.session_state:
    st.session_state.necessities = []

def add_necessity():
    name = st.session_state.nec_name
    if name:
        st.session_state.necessities.append(
            {"name": name, "cost": st.session_state.nec_cost}
            )
    st.session_state.nec_name = ""
    st.session_state.nec_cost = 0

def clear_necessities():
    st.session_state.necessities = []

st.title("Angom - bola hanamora ny fiainanao")

# Goal
st.subheader("Inona ny tanjona tianao ho tratrarina na ny zavatra tianao ho azo atsy ho atsy ?")
goal_name = st.text_input("Tanjona (oh: Akanjo Krisimasy / afaka atao amin'ny teny hafa a !)")
goal_amount = st.number_input("Vola tiana ho tratrarina (Ar)", min_value=1.0, value = 50000.0)
days = st.number_input("Fehi-potoana (firy andro)", min_value=1, value=60)

# Daily money
daily_money = st.number_input("Mahazo ohatrinona isan'andro ianao ? (Ar) : ", min_value=0)

# Necessities
st.subheader("Fandaniaina ilaina andavan'andro")
st.text_input("ohatra 'Sakafo', 'frais bus'...", key="nec_name")
st.number_input("Ohatrinona ? (Ar)", min_value = 0, step = 100, key="nec_cost")
st.button("✛ hanampy", on_click=add_necessity)
st.button("Hamafa", on_click=clear_necessities)

st.table(st.session_state.necessities)

total = sum(n["cost"] for n in st.session_state.necessities)
rest = daily_money - total

st.write("Fandaniainao isan'andro:", total, "Ar")
st.write("Ambim-bolanao:", rest, "Ar")

# Progress = suivi de l'objectif
st.subheader("Aiza ho aiza ny tanjonao izao ? ")
expected_savings = rest * days
progress = max(0.0, min(expected_savings / goal_amount, 1.0))

st.progress(progress, text=f"{progress * 100:.0f}% 'ny tanjonao")
st.write("Vinavinan-tahiry ao anatin'ny ", days, " :", expected_savings, "Ar")

if rest < 0:
    st.write("Betsaka noho ny vola anananao isan'andro ny fandaniainao .")
elif expected_savings >= goal_amount:
    st.write("Tratra ny tanjona :", goal_name)
    st.write("Vola sisa mihoatra:", expected_savings - goal_amount, "Ar")
else:
    st.write("mbola tsy ampy ", goal_amount - expected_savings, "Ar ny volanao. Mbola tsy traatra ny tanjonao : ", goal_name)
