import streamlit as st

st.title("🍬 당뇨병 위험도 계산기")

# 사용자 입력
age = st.slider("나이", 10, 80, 18)
height = st.number_input("키 (cm)", min_value=100, max_value=220, value=170)
weight = st.number_input("체중 (kg)", min_value=30, max_value=150, value=60)
family_history = st.selectbox("가족 중 당뇨병 환자가 있나요?", ["없음", "있음"])
exercise = st.selectbox("주 3회 이상 운동을 하나요?", ["예", "아니오"])

# BMI 계산
bmi = weight / ((height/100)**2)
st.write(f"📏 당신의 BMI는 **{bmi:.1f}** 입니다.")

# 위험 점수 계산
risk = 0
if age > 45:
    risk += 2
if bmi > 25:
    risk += 2
if family_history == "있음":
    risk += 3
if exercise == "아니오":
    risk += 2

# 결과
if risk <= 2:
    result = "낮음"
elif risk <= 5:
    result = "보통"
else:
    result = "높음"

st.subheader(f"👉 당신의 당뇨병 위험도는: **{result}**")
st.progress(min(risk/7, 1.0))
