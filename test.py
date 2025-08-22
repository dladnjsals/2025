import streamlit as st
import time

st.title("👀 눈 건강 타이머 - 20-20-20 규칙")

if "phase" not in st.session_state:
    st.session_state.phase = "study"
    st.session_state.start_time = None

if st.button("타이머 시작"):
    st.session_state.phase = "study"
    st.session_state.start_time = time.time()

if st.session_state.start_time:
    elapsed = time.time() - st.session_state.start_time
    
    if st.session_state.phase == "study":
        remaining = 20*60 - int(elapsed)
        if remaining > 0:
            st.subheader(f"📖 공부 시간 남음: {remaining//60}분 {remaining%60}초")
        else:
            st.session_state.phase = "rest"
            st.session_state.start_time = time.time()
    
    elif st.session_state.phase == "rest":
        remaining = 20 - int(elapsed)
        if remaining > 0:
            st.subheader(f"👀 휴식 시간 남음: {remaining}초")
            st.write("👉 20피트 떨어진 곳을 바라보세요!")
        else:
            st.session_state.phase = "study"
            st.session_state.start_time = time.time()
            st.success("✅ 휴식 끝! 다시 공부를 시작하세요.")

