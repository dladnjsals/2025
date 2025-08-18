import streamlit as st

st.set_page_config(page_title="내신 목표 계산기", page_icon="📚", layout="wide")

st.title("🎯 내신 목표 달성 계산기")
st.write("👉 학기별 내신과 반영 비율을 입력하면, 앞으로 몇 등급을 받아야 목표 내신을 달성할 수 있는지 계산해드립니다!")

# ------------------------
# 입력
# ------------------------
st.subheader("1️⃣ 학기별 내신 입력 (없으면 0 입력)")
grades = {}
for semester in ["1-1", "1-2", "2-1", "2-2", "3-1", "3-2"]:
    grades[semester] = st.number_input(f"{semester} 등급", min_value=0.0, max_value=9.0, step=0.1, value=0.0)

st.subheader("2️⃣ 학기별 반영 비율 (%)")
weights = {}
for semester in ["1-1", "1-2", "2-1", "2-2", "3-1", "3-2"]:
    weights[semester] = st.slider(f"{semester} 반영 비율", 0, 100, 20)

st.subheader("3️⃣ 목표 내신 등급 입력")
target = st.number_input("목표 내신 등급", min_value=1.0, max_value=9.0, step=0.1, value=2.0)

# ------------------------
# 계산
# ------------------------
if st.button("📌 목표 달성 가능 여부 확인"):
    total_weight = sum(weights.values())

    if total_weight != 100:
        st.warning("⚠️ 반영 비율의 합은 100%가 되어야 합니다!")
    else:
        # 이미 나온 학기와 아직 남은 학기를 구분
        achieved = {s: g for s, g in grades.items() if g > 0}
        remaining = [s for s, g in grades.items() if g == 0]

        # 이미 나온 학기 점수 (가중합)
        achieved_score = sum(grades[s] * weights[s] for s in achieved) / 100
        achieved_weight = sum(weights[s] for s in achieved) / 100

        remaining_weight = 1 - achieved_weight

        if remaining_weight <= 0:
            st.info("✅ 모든 학기 성적이 입력되었습니다!")
        else:
            # 남은 학기에서 필요한 평균 등급
            required_avg = (target - achieved_score) / remaining_weight

            if required_avg <= 9:
                st.success(f"📊 남은 {len(remaining)}학기에서 평균 **{required_avg:.2f} 등급**을 받으면 목표({target}등급) 달성 가능!")
            else:
                st.error("😭 목표 달성이 불가능합니다. 목표를 조정하거나 더 높은 성적이 필요합니다.")
