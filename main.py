from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='MECHA LAB 2.0 | 6-AXIS', page_icon='🦾', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarCollapsedControl"] {display:none!important}
.block-container {max-width:100%!important;padding:0!important}
header[data-testid="stHeader"]{display:none!important}
.stApp {background:#090f1c}
iframe {display:block}
</style>''', unsafe_allow_html=True)
html = (Path(__file__).resolve().parent / 'assets' / 'robot_3d.html').read_text(encoding='utf-8')
components.html(html, height=950, scrolling=False)
