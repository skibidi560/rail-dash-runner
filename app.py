
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Rail Dash",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header {
    visibility: hidden;
}
.block-container {
    padding: 0.4rem 0.6rem 0.5rem;
    max-width: 1200px;
}
[data-testid="stAppViewContainer"] {
    background: #101827;
}
</style>
""", unsafe_allow_html=True)

game_file = Path(__file__).parent / "game.html"

if game_file.exists():
    html = game_file.read_text(encoding="utf-8")
    components.html(
        html,
        height=790,
        scrolling=False
    )
else:
    st.error("Không tìm thấy game.html. Hãy tạo file này trong cùng repository.")
