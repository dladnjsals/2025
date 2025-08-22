import streamlit as st

st.title("🍬 당뇨병 위험도 계산기 (교육용)")

age = st.slider("나이", 10, 80, 18)
bmi = st.slider("BMI (체질량지수)", 10.0, 40.0, 22.0)
family_history = st.selectbox("가족 중 당뇨병 환자가 있나요?", ["없음", "있음"])
exercise = st.selectbox("주 3회 이상 운동을 하나요?", ["예", "아니오"])

# 위험 점수 계산 (아주 간단하게)
risk = 0
if age > 45:
    risk += 2
if bmi > 25:
    risk += 2
if family_history == "있음":
    risk += 3
if exercise == "아니오":
    risk += 2

# 위험도 단계
if risk <= 2:
    result = "낮음"
elif risk <= 5:
    result = "보통"
else:
    result = "높음"

st.subheader(f"👉 당신의 당뇨병 위험도는: **{result}**")
st.progress(min(risk/7, 1.0))
