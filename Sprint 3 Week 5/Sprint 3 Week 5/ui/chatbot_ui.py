import streamlit as st
import re
from rag_chain import qa_chain

st.set_page_config(page_title="UrbanNest AI", page_icon="🛋️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600&display=swap');
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { background-color: #0d0d0f; color: #e8e8e6; font-family: 'Sora', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton, [data-testid="stToolbar"] { display: none; }
.block-container { max-width: 780px !important; padding: 0 1.5rem 180px 1.5rem !important; margin: 0 auto; }

.urbannest-header { display:flex; align-items:center; gap:10px; padding:26px 0 8px 0; border-bottom:1px solid #1a1a20; margin-bottom:24px; }
.urbannest-logo { font-size:1.15rem; font-weight:600; color:#f0ede8; letter-spacing:-0.02em; }
.urbannest-badge { font-size:0.63rem; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.08); color:#555552; padding:2px 7px; border-radius:20px; letter-spacing:0.07em; text-transform:uppercase; }

.empty-state { display:flex; flex-direction:column; align-items:center; padding:56px 0 28px 0; gap:9px; }
.empty-icon { font-size:2.2rem; margin-bottom:2px; }
.empty-title { font-size:1.35rem; font-weight:600; color:#f0ede8; letter-spacing:-0.02em; }
.empty-sub { font-size:0.86rem; color:#44444a; text-align:center; max-width:320px; line-height:1.65; margin-bottom:6px; }
.pill-label { font-size:0.68rem; color:#333338; text-transform:uppercase; letter-spacing:0.07em; }

div[data-testid="stHorizontalBlock"] .stButton button {
    background: #111116 !important;
    border: 1px solid #1e1e24 !important;
    color: #666662 !important;
    border-radius: 22px !important;
    padding: 10px 20px !important;
    font-size: 0.82rem !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 400 !important;
    width: 100% !important;
    transition: all 0.18s !important;
    white-space: nowrap !important;
    letter-spacing: 0.01em !important;
}
div[data-testid="stHorizontalBlock"] .stButton button:hover {
    background: #18181f !important;
    border-color: #32323c !important;
    color: #c0beb8 !important;
    transform: translateY(-1px) !important;
}

.msg-user { display:flex; gap:14px; padding:22px 0; border-bottom:1px solid rgba(255,255,255,0.035); animation:fadeIn 0.2s ease both; }
.msg-ai-wrap { display:flex; gap:14px; padding:22px 0; border-bottom:1px solid rgba(255,255,255,0.035); animation:fadeIn 0.2s ease both; }
@keyframes fadeIn { from{opacity:0;transform:translateY(7px);}to{opacity:1;transform:translateY(0);} }
.avatar { width:27px; height:27px; border-radius:7px; display:flex; align-items:center; justify-content:center; flex-shrink:0; margin-top:1px; }
.avatar-user { background:linear-gradient(135deg,#3b5bdb,#228be6); color:white; font-weight:700; font-size:0.68rem; }
.avatar-ai { background:#161620; border:1px solid #242430; font-size:0.85rem; }
.msg-body { flex:1; min-width:0; }
.msg-sender { font-size:0.69rem; font-weight:600; color:#3a3a3f; letter-spacing:0.06em; text-transform:uppercase; margin-bottom:8px; }
.user-text { font-size:0.93rem; color:#cccac4; line-height:1.7; }
.intro-text { font-size:0.9rem; color:#7a7a76; line-height:1.7; margin-bottom:12px; }

.stTextInput input { background-color:#101014 !important; color:#e8e8e6 !important; border:1px solid #1e1e26 !important; border-radius:13px !important; padding:13px 17px !important; font-family:'Sora',sans-serif !important; font-size:0.9rem !important; }
.stTextInput input:focus { border-color:#303040 !important; box-shadow:0 0 0 3px rgba(99,102,241,0.07) !important; }
.stTextInput input::placeholder { color:#30303a !important; }
.send-btn .stButton button { background:#141420 !important; color:#707070 !important; border:1px solid #222230 !important; border-radius:11px !important; padding:11px !important; font-family:'Sora',sans-serif !important; font-size:0.84rem !important; font-weight:500 !important; width:100% !important; margin-top:8px !important; transition:all 0.15s !important; }
.send-btn .stButton button:hover { background:#1a1a28 !important; border-color:#2e2e40 !important; color:#c0c0b8 !important; }
.hint { text-align:center; font-size:0.68rem; color:#252530; margin-top:8px; letter-spacing:0.03em; }
</style>
""", unsafe_allow_html=True)

# ── helpers ──────────────────────────────────────────────
PRODUCT_RE = re.compile(
    r"Product Name:\s*(.+?)\s+Style:\s*(.+?)\s+Price:\s*([\d,]+)\s+Rating:\s*([\d.]+)\s+Stock:\s*(\d+)",
    re.IGNORECASE
)

def parse_products(text):
    products = []
    for m in PRODUCT_RE.finditer(text):
        products.append({
            "name": m.group(1).strip(),
            "style": m.group(2).strip(),
            "price": int(m.group(3).replace(",", "")),
            "rating": float(m.group(4)),
            "stock": int(m.group(5)),
        })
    intro = PRODUCT_RE.sub("", text)
    intro = re.sub(r"^\s*\d+\.\s*", "", intro, flags=re.MULTILINE).strip()
    return products, intro

def stars(r):
    full = int(r); half = 1 if (r - full) >= 0.5 else 0; empty = 5 - full - half
    return "★" * full + ("½" if half else "") + "☆" * empty

def stock_label(n):
    if n >= 15: return f"🟢 In stock ({n})"
    if n >= 5:  return f"🟡 Low stock ({n})"
    return f"🔴 Very low ({n})"

# ── session state ─────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []
if "pending" not in st.session_state:
    st.session_state.pending = ""
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# ── header ────────────────────────────────────────────────
st.markdown("""
<div class="urbannest-header">
  <span>🛋️</span>
  <span class="urbannest-logo">UrbanNest AI</span>
  <span class="urbannest-badge">Beta</span>
</div>
""", unsafe_allow_html=True)

# ── empty state ───────────────────────────────────────────
SUGGESTIONS = [
    "Suggest a Scandinavian sofa under ₹50,000",
    "Show me Minimalist beds with high ratings",
    "Luxury dining tables available in stock",
    "Best rated Industrial chairs",
]

if not st.session_state.history:
    st.markdown("""
    <div class="empty-state">
      <div class="empty-icon">🛋️</div>
      <div class="empty-title">What are you looking for?</div>
      <div class="empty-sub">Describe your space, style, or budget — I'll find the right furniture for you.</div>
      <div class="pill-label">Try asking</div>
    </div>""", unsafe_allow_html=True)
    row1 = st.columns([1, 1], gap="medium")
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    row2 = st.columns([1, 1], gap="medium")
    for i, s in enumerate(SUGGESTIONS):
        target = row1[i % 2] if i < 2 else row2[i % 2]
        with target:
            if st.button(s, key=f"sug_{i}"):
                st.session_state.pending = s
                st.rerun()

# ── process pending ───────────────────────────────────────
if st.session_state.pending:
    q = st.session_state.pending
    st.session_state.pending = ""
    st.session_state.history.append((q, qa_chain.run(q)))

# ── chat history ──────────────────────────────────────────
for q, r in st.session_state.history:
    # user
    st.markdown(f"""
    <div class="msg-user">
      <div class="avatar avatar-user">U</div>
      <div class="msg-body">
        <div class="msg-sender">You</div>
        <div class="user-text">{q}</div>
      </div>
    </div>""", unsafe_allow_html=True)

    # ai header + intro
    products, intro = parse_products(r)
    st.markdown(f"""
    <div class="msg-ai-wrap">
      <div class="avatar avatar-ai">✦</div>
      <div class="msg-body">
        <div class="msg-sender">UrbanNest AI</div>
        {"<div class='intro-text'>" + intro + "</div>" if intro else ""}
    </div></div>""", unsafe_allow_html=True)

    # product cards — rendered via Streamlit native components, NOT passed through LLM
    if products:
        for p in products:
            with st.container():
                st.markdown(f"""
                <div style="background:#111116;border:1px solid #1e1e26;border-radius:14px;
                            padding:18px 20px;margin-bottom:10px;margin-left:41px;">
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                    <span style="font-size:0.97rem;font-weight:600;color:#e8e6e0;letter-spacing:-0.01em;">{p['name']}</span>
                    <span style="font-size:0.85rem;font-weight:600;color:#7c9e7a;background:rgba(100,160,100,0.08);
                                 border:1px solid rgba(100,160,100,0.18);padding:3px 11px;border-radius:20px;">
                      ₹{p['price']:,}
                    </span>
                  </div>
                  <div style="display:flex;gap:28px;flex-wrap:wrap;">
                    <div>
                      <div style="font-size:0.62rem;text-transform:uppercase;letter-spacing:0.07em;color:#383840;margin-bottom:3px;">Style</div>
                      <div style="font-size:0.83rem;color:#8a8884;">{p['style']}</div>
                    </div>
                    <div>
                      <div style="font-size:0.62rem;text-transform:uppercase;letter-spacing:0.07em;color:#383840;margin-bottom:3px;">Rating</div>
                      <div style="font-size:0.83rem;color:#c4943a;">{stars(p['rating'])} <span style="color:#8a8884;">{p['rating']}</span></div>
                    </div>
                    <div>
                      <div style="font-size:0.62rem;text-transform:uppercase;letter-spacing:0.07em;color:#383840;margin-bottom:3px;">Availability</div>
                      <div style="font-size:0.83rem;color:#8a8884;">{stock_label(p['stock'])}</div>
                    </div>
                  </div>
                </div>""", unsafe_allow_html=True)

# ── input bar ─────────────────────────────────────────────
query = st.text_input("", placeholder="Describe your space or what you're looking for...",
                      label_visibility="collapsed", key=f"query_{st.session_state.input_key}")
st.markdown('<div class="send-btn">', unsafe_allow_html=True)
if st.button("Send →", key="send_btn"):
    if query.strip():
        st.session_state.pending = query
        st.session_state.input_key += 1
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="hint">UrbanNest AI can make mistakes. Verify important details.</div>', unsafe_allow_html=True)