import streamlit as st

st.set_page_config(page_title="내신 등급 계산기", page_icon="📚", layout="wide")

st.title("📊 내신 등급 계산기")
st.write("👉 현재 내신과 목표 내신을 입력하면, 학년별 반영비율을 고려하여 최종 내신을 계산해드립니다!")

# ------------------------
# 입력 파트
# ------------------------
st.subheader("1️⃣ 현재 내신 등급 입력")
grade1 = st.number_input("1학년 내신 등급 (없으면 0 입력)", min_value=0.0, max_value=9.0, step=0.1, value=0.0)
grade2 = st.number_input("2학년 내신 등급 (없으면 0 입력)", min_value=0.0, max_value=9.0, step=0.1, value=0.0)
grade3 = st.number_input("3학년 내신 등급 (없으면 0 입력)", min_value=0.0, max_value=9.0, step=0.1, value=0.0)

st.subheader("2️⃣ 목표 내신 등급 입력")
target = st.number_input("목표 내신 등급", min_value=1.0, max_value=9.0, step=0.1, value=2.0)

st.subheader("3️⃣ 학년별 반영 비율 (%)")
weight1 = st.slider("1학년 반영 비율", 0, 100, 20)
weight2 = st.slider("2학년 반영 비율", 0, 100, 40)
weight3 = st.slider("3학년 반영 비율", 0, 100, 40)

# 비율 합계가 100이 아닐 경우 보정
total_weight = weight1 + weight2 + weight3
if total_weight != 100:
    st.warning("⚠️ 반영 비율의 합은 100%가 되어야 합니다!")

# ------------------------
# 계산
# ------------------------
if st.button("📌 내신 계산하기"):
    if total_weight == 100:
        weighted_sum = (grade1 * weight1 + grade2 * weight2 + grade3 * weight3) / 100
        st.success(f"🎓 현재 예상 최종 내신 등급: **{weighted_sum:.2f} 등급**")

        if weighted_sum <= target:
            st.balloons()
            st.info(f"👏 목표 내신 {target:.2f} 등급 달성이 가능합니다!")
        else:
            diff = weighted_sum - target
            st.warning(f"😅 현재 계산 결과는 {weighted_sum:.2f} 등급으로, 목표보다 {diff:.2f} 등급 높습니다. 더 노력해야 해요!")
