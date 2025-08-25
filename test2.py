import streamlit as st
import time

st.set_page_config(page_title="눈 건강 타이머", page_icon="👀", layout="centered")

st.title("👀 눈 건강 타이머 - 20-20-20 규칙")

# 초기 세션 상태
if "phase" not in st.session_state:
    st.session_state.phase = None

# 버튼을 화면 가운데 배치
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("▶️ 타이머 시작", use_container_width=True):
        st.session_state.phase = "study"
        st.experimental_rerun()

# 공부 단계
if st.session_state.phase == "study":
    st.info("📖 공부 20분을 시작합니다! 집중하세요 😎")
    study_placeholder = st.empty()
    progress_bar = st.progress(0)
    for sec in range(20*60, 0, -1):
        mins, s = divmod(sec, 60)
        study_placeholder.subheader(f"⏳ 공부 시간 남음: {mins}분 {s}초")
        progress_bar.progress(int((20*60-sec)/(20*60)*100))
        time.sleep(1)
    st.session_state.phase = "rest"
    st.experimental_rerun()

# 휴식 단계
elif st.session_state.phase == "rest":
    st.warning("👀 휴식 20초 시작! 먼 곳을 바라보세요 🌳")
    rest_placeholder = st.empty()
    for sec in range(20, 0, -1):
        rest_placeholder.subheader(f"😌 휴식 시간 남음: {sec}초")
        time.sleep(1)
    st.success("✅ 휴식 끝! 다시 공부를 시작하세요 🚀")
    st.session_state.phase = "study"
    st.experimental_rerun()
