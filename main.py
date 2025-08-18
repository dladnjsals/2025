# Streamlit MBTI Career Recommender — Single-file App
# --------------------------------------------------
# How to run locally:
#   1) pip install streamlit
#   2) streamlit run app.py
# --------------------------------------------------

import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="MBTI 진로 추천 💼✨",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Global Styles (CSS Injection)
# -----------------------------
CUSTOM_CSS = """
<style>
/***** Background Gradient *****/
.stApp {
  background: radial-gradient(1250px circle at 10% 10%, #fff7ef 5%, #ffe9f2 30%, #e8f3ff 65%, #f2f7ff 90%);
}

/***** Fancy Title *****/
.gradient-title {
  font-size: clamp(28px, 4vw, 54px);
  font-weight: 900;
  letter-spacing: -0.5px;
  line-height: 1.08;
  background: linear-gradient(90deg, #ff6cab, #7366ff, #3dd6d0, #ffd166);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.sub-title{
  font-size: clamp(14px, 1.8vw, 20px);
  color: #4b5563;
}

/***** Card *****/
.card{
  background: rgba(255,255,255,0.8);
  border: 1px solid rgba(0,0,0,0.05);
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  transition: transform 200ms ease, box-shadow 200ms ease;
}
.card:hover{ transform: translateY(-3px); box-shadow: 0 16px 36px rgba(0,0,0,0.12);} 
.card-title{ font-weight: 800; font-size: 20px;}
.badge{
  display: inline-block; margin: 6px 6px 0 0; padding: 6px 10px; border-radius: 999px;
  background: linear-gradient(90deg, #eef2ff, #e0e7ff);
  border: 1px solid #c7d2fe; font-size: 13px; color: #4338ca; font-weight: 700;
}

hr.fancy{ height: 10px; border: 0; margin: 10px 0 20px; background:
  radial-gradient(circle closest-side, rgba(0,0,0,0.15), transparent) 0/10px 10px repeat-x; }

/***** Footer *****/
.footer {
  text-align:center; color:#6b7280; font-size:13px; margin-top: 40px;
}

/***** Emoji Rain - simple animation *****/
@keyframes floaty { from {transform: translateY(0)} to {transform: translateY(-18px)} }
.floaty { animation: floaty 1.6s ease-in-out infinite alternate }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------
# Data — MBTI → Careers, Strengths, Tips
# -----------------------------
CAREER_DB = {
    "INTJ": {
        "name": "INTJ — 전략가 🧠🗺️",
        "careers": [
            "데이터 사이언티스트 📊",
            "의과학 연구원 🧬",
            "AI 제품 매니저 🤖",
            "전략 컨설턴트 🧩",
            "UX 리서처 🔬",
        ],
        "strengths": ["장기적 기획", "논리적 문제해결", "독립적 탐구"],
        "tips": [
            "깊이 있는 프로젝트 포트폴리오를 구축해요.",
            "현장실습/인턴으로 현실 감각을 쌓아요.",
            "복잡한 문제를 시각화해 설명하는 연습!",
        ],
        "majors": ["의공학", "통계/데이터", "컴퓨터공학", "바이오인포매틱스"],
    },
    "INTP": {
        "name": "INTP — 사색가 🧩🧪",
        "careers": [
            "연구개발 엔지니어 🧪",
            "알고리즘 연구원 🧬",
            "시스템 아키텍트 🧱",
            "기술분석가 🔎",
            "과학저술가 ✍️",
        ],
        "strengths": ["아이디어 생성", "분석", "개념화"],
        "tips": ["사이드 프로젝트로 가설→실험→검증 루프!", "학회/커뮤니티 참여", "글쓰기로 사고 정리"],
        "majors": ["물리", "수학", "컴퓨터과학", "전기전자"],
    },
    "ENTJ": {
        "name": "ENTJ — 지휘관 🏁📈",
        "careers": ["프로덕트 매니저 🚀", "경영전략 컨설턴트 🧠", "의료경영 리더 🏥", "벤처 창업가 💡", "투자심사역 💼"],
        "strengths": ["리더십", "의사결정", "실행력"],
        "tips": ["리더 역할을 맡아 KPI 설정", "토론·피칭 훈련", "멘토링 네트워크 구축"],
        "majors": ["경영", "보건행정", "산업공학", "의료정보"],
    },
    "ENTP": {
        "name": "ENTP — 토론가 🗣️⚡",
        "careers": ["혁신 컨설턴트 ✨", "신사업 기획 🧨", "크리에이티브 디렉터 🎨", "벤처 빌더 🧱", "글로벌 마케터 🌍"],
        "strengths": ["창의적 발상", "설득", "적응"],
        "tips": ["피치덱·프로토타입 제작 습관", "디벨롭 대신 빠른 실험", "토론/디베이트 동아리"],
        "majors": ["경영", "미디어", "디자인씽킹", "국제학"],
    },
    "INFJ": {
        "name": "INFJ — 옹호자 🕊️🌱",
        "careers": ["임상심리사 🧠", "정책연구원 🏛️", "사회혁신가 🤝", "교육 컨설턴트 📚", "의료사회복지사 💞"],
        "strengths": ["공감", "통찰", "가치지향"],
        "tips": ["윤리·법·정책 읽기", "현장 봉사/캡스톤", "스토리텔링 역량 개발"],
        "majors": ["심리", "교육", "사회복지", "보건정책"],
    },
    "INFP": {
        "name": "INFP — 중재자 🌸🦋",
        "careers": ["콘텐츠 기획자 📝", "아동·청소년 상담사 🧸", "UX 라이터 ✍️", "출판/에디터 📖", "문화예술 기획 🎭"],
        "strengths": ["창의성", "가치중심", "언어 감수성"],
        "tips": ["포트폴리오 블로그 운영", "봉사·현장 실습", "멀티미디어 툴 익히기"],
        "majors": ["국문/영문
