import streamlit as st

# ------------------------
# 기본 세팅
# ------------------------
st.set_page_config(page_title="MBTI Career Recommender", page_icon="🌈", layout="wide")

# 제목
st.markdown("<h1 style='text-align:center; font-size:50px;'>🌟 MBTI 기반 진로 추천 사이트 🌟</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>당신의 성격 유형에 맞는 ✨최고의 직업✨을 찾아보세요! 🚀</h3>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------
# MBTI 데이터베이스
# ------------------------
career_dict = {
    "INTJ": ["🧠 데이터 사이언티스트 📊", "🧬 의과학 연구원 🧪", "📈 전략 컨설턴트 💼"],
    "INTP": ["🔬 연구개발 엔지니어 🛠️", "📐 알고리즘 연구원 🤖", "✍️ 과학저술가 📚"],
    "ENTJ": ["🚀 프로덕트 매니저 📱", "📊 경영전략 컨설턴트 💡", "🏥 의료경영 리더 🧑‍⚕️"],
    "ENFP": ["🎨 콘텐츠 기획자 ✨", "📣 마케터 🌍", "🎭 크리에이티브 디렉터 🖌️"],
    "INFJ": ["🧑‍⚕️ 임상심리사 🧠", "🏛️ 정책연구원 📜", "🌱 사회혁신가 🤝"],
    "ISFP": ["🎬 아트 디렉터 🎨", "📷 영상 크리에이터 📸", "🎭 의료미술치료사 💕"],
    "ESTP": ["🏎️ 스포츠 매니저 ⚽", "📣 이벤트 프로듀서 🎉", "🚑 응급구조사 🩺"],
    "ESFJ": ["👩‍🏫 교사 📚", "🫂 상담가 💞", "🎪 이벤트 플래너 🎊"],
    # 나머지 MBTI도 추가 가능
}

# ------------------------
# 입력 받기
# ------------------------
mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", list(career_dict.keys()))

# ------------------------
# 추천 직업 출력
# ------------------------
if mbti:
    st.markdown(f"<h2 style='text-align:center;'>✨ {mbti} 유형에게 어울리는 직업 ✨</h2>", unsafe_allow_html=True)
    cols = st.columns(3)  # 3열 레이아웃
    
    jobs = career_dict[mbti]
    for i, job in enumerate(jobs):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #fceabb, #f8b500);
                            padding:20px; border-radius:20px; 
                            margin:10px; text-align:center; 
                            box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                    <h3 style="color:#fff;">{job}</h3>
                    <p style="color:#333;">🔥 이 직업은 당신의 성향과 찰떡! 🔥</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# ------------------------
# 화려한 효과 (애니메이션)
# ------------------------
st.snow()
st.balloons()

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>🌈 Made with ❤️ in Streamlit</p>", unsafe_allow_html=True)
