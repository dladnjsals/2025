import streamlit as st
import time

st.title("👀 눈 건강 타이머 ")

# 초기 세션 상태
if "phase" not in st.session_state:
    st.session_state.phase = None

# 사용자 입력 (공부 시간, 휴식 시간)
st.sidebar.header("⚙️ 타이머 설정")
study_minutes = st.sidebar.slider("공부 시간 (분)", 5, 60)
rest_seconds = st.sidebar.slider("휴식 시간 (초)", 10, 120)

# 버튼을 화면 가운데 배치
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("▶️ 타이머 시작", use_container_width=True):
        st.session_state.phase = "study"
        st.rerun()

# 공부 단계
if st.session_state.phase == "study":
    st.info(f"📖 공부 {study_minutes}분을 시작합니다! 집중하세요 😎")
    study_placeholder = st.empty()
    progress_bar = st.progress(0)
    total_sec = study_minutes * 60
    for sec in range(total_sec, 0, -1):
        mins, s = divmod(sec, 60)
        study_placeholder.subheader(f"⏳ 공부 시간 남음: {mins}분 {s}초")
        progress_bar.progress(int((total_sec-sec)/total_sec*100))
        time.sleep(1)
    st.session_state.phase = "rest"
    st.rerun()

# 휴식 단계
elif st.session_state.phase == "rest":
    st.warning(f"👀 휴식 {rest_seconds}초 시작! 먼 곳을 바라보세요 🌳")
    rest_placeholder = st.empty()
    for sec in range(rest_seconds, 0, -1):
        rest_placeholder.subheader(f"😌 휴식 시간 남음: {sec}초")
        time.sleep(1)
    st.success("✅ 휴식 끝! 다시 공부를 시작하세요 🚀")
    st.session_state.phase = "study"
    st.rerun()
