import os
import re
import shutil
import tempfile
import streamlit as st
import yt_dlp

# Page Configuration
st.set_page_config(
    page_title="Legend Stream Pro | @Legend__bhai_",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ultra-Advanced Animated Cyberpunk & Glassmorphism CSS
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800;900&display=swap" rel="stylesheet">

<style>
/* Global Font & Reset */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* Deep Animated Aurora Background */
.stApp {
    background: radial-gradient(circle at 15% 20%, rgba(255, 0, 127, 0.18) 0%, transparent 45%),
                radial-gradient(circle at 85% 80%, rgba(0, 242, 254, 0.18) 0%, transparent 45%),
                radial-gradient(circle at 50% 50%, rgba(121, 40, 202, 0.15) 0%, transparent 60%),
                #05050d;
    background-attachment: fixed;
    color: #f8fafc;
}

/* Floating Animated Orbs */
.orb-container {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(85px);
    opacity: 0.55;
    animation: floatOrb 10s infinite alternate ease-in-out;
}
.orb-1 { width: 320px; height: 320px; background: #ff007f; top: -80px; left: -80px; }
.orb-2 { width: 360px; height: 360px; background: #00f2fe; bottom: -100px; right: -80px; animation-delay: 3s; }
.orb-3 { width: 260px; height: 260px; background: #7928ca; top: 45%; left: 60%; animation-delay: 6s; }

@keyframes floatOrb {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(40px, -40px) scale(1.15); }
    100% { transform: translate(-30px, 30px) scale(0.9); }
}

/* Top Instagram Creator Pill */
.creator-pill-wrap {
    display: flex;
    justify-content: center;
    margin-bottom: 12px;
    position: relative;
    z-index: 2;
}
.creator-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 20px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 0, 127, 0.45);
    box-shadow: 0 0 25px rgba(255, 0, 127, 0.35), inset 0 0 12px rgba(0, 242, 254, 0.2);
    backdrop-filter: blur(16px);
    text-decoration: none !important;
    color: #ffffff !important;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.5px;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}
.creator-pill:hover {
    transform: translateY(-3px) scale(1.05);
    border-color: #00f2fe;
    box-shadow: 0 0 35px rgba(0, 242, 254, 0.7), 0 0 50px rgba(255, 0, 127, 0.5);
}
.creator-pill i {
    font-size: 1.15rem;
    background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Hero Title */
.hero-title {
    font-size: 3.3rem;
    font-weight: 900;
    text-align: center;
    line-height: 1.1;
    background: linear-gradient(90deg, #00f2fe, #4facfe, #ff007f, #ffb199, #00f2fe);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shineText 5s linear infinite;
    margin-bottom: 8px;
}
@keyframes shineText {
    to { background-position: 300% center; }
}

.hero-sub {
    text-align: center;
    color: #94a3b8;
    font-size: 1rem;
    margin-bottom: 22px;
}

/* Supported Platform Floating Icons */
.platform-bar {
    display: flex;
    justify-content: center;
    gap: 18px;
    margin-bottom: 28px;
}
.plat-icon {
    width: 44px; height: 44px;
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    color: #cbd5e1;
    transition: all 0.3s ease;
}
.plat-icon:hover {
    transform: translateY(-5px) scale(1.12);
    border-color: #00f2fe;
    box-shadow: 0 10px 25px rgba(0, 242, 254, 0.35);
    color: #ffffff;
}

/* Glass Container for Inputs */
div[data-testid="stVerticalBlock"] > div:has(div.stTextInput) {
    background: rgba(15, 18, 38, 0.65);
    backdrop-filter: blur(22px);
    -webkit-backdrop-filter: blur(22px);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 26px;
    padding: 26px;
    box-shadow: 0 25px 60px rgba(0, 0, 0, 0.65), 0 0 35px rgba(121, 40, 202, 0.25);
}

/* Input Boxes Styling */
.stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
    background: rgba(6, 8, 20, 0.85) !important;
    border: 1.5px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 16px !important;
    color: #ffffff !important;
    padding: 12px 16px !important;
    font-size: 0.98rem !important;
    transition: all 0.3s ease !important;
}
.stTextInput input:focus, .stSelectbox div[data-baseweb="select"] > div:focus-within {
    border-color: #00f2fe !important;
    box-shadow: 0 0 20px rgba(0, 242, 254, 0.35) !important;
}

/* Neon Animated Buttons */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #ff007f 0%, #7928ca 50%, #00f2fe 100%) !important;
    background-size: 200% 200% !important;
    color: #ffffff !important;
    font-weight: 800 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.6px !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 0.85rem 1.5rem !important;
    box-shadow: 0 10px 30px rgba(255, 0, 127, 0.45) !important;
    transition: all 0.35s ease !important;
    animation: shineText 5s ease infinite !important;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 0 35px rgba(0, 242, 254, 0.75), 0 0 55px rgba(255, 0, 127, 0.5) !important;
}

/* Emerald Save Button */
.stDownloadButton > button {
    width: 100%;
    background: linear-gradient(135deg, #00f2fe 0%, #10b981 50%, #059669 100%) !important;
    color: #04131a !important;
    font-weight: 900 !important;
    font-size: 1.1rem !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 0.95rem 1.5rem !important;
    box-shadow: 0 0 30px rgba(16, 185, 129, 0.6) !important;
    transition: all 0.3s ease !important;
}
.stDownloadButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 0 45px rgba(0, 242, 254, 0.9) !important;
}

/* Video Preview Glass Card */
.video-card {
    background: rgba(12, 14, 30, 0.78);
    border: 1px solid rgba(0, 242, 254, 0.35);
    border-radius: 22px;
    padding: 20px;
    margin-top: 20px;
    margin-bottom: 20px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(0, 242, 254, 0.18);
}
.video-thumb {
    width: 100%;
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    margin-bottom: 14px;
}
.meta-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 10px;
}
.badge {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 5px 13px;
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 600;
    color: #38bdf8;
}

/* Signature Footer Card */
.insta-footer {
    margin-top: 40px;
    padding: 22px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(255, 0, 127, 0.12), rgba(121, 40, 202, 0.15), rgba(0, 242, 254, 0.12));
    border: 1px solid rgba(255, 255, 255, 0.15);
    text-align: center;
    backdrop-filter: blur(18px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.5);
}
.insta-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    margin-top: 12px;
    padding: 12px 28px;
    border-radius: 999px;
    background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
    color: #ffffff !important;
    font-weight: 800;
    font-size: 1rem;
    text-decoration: none !important;
    box-shadow: 0 10px 25px rgba(220, 39, 67, 0.5);
    transition: all 0.3s ease;
}
.insta-btn:hover {
    transform: translateY(-3px) scale(1.06);
    box-shadow: 0 15px 35px rgba(220, 39, 67, 0.85);
}
</style>

<!-- Background Orbs -->
<div class="orb-container">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
</div>

<!-- Top Floating Instagram Badge -->
<div class="creator-pill-wrap">
    <a href="https://instagram.com/Legend__bhai_" target="_blank" class="creator-pill">
        <i class="fa-brands fa-instagram"></i>
        <span>CRAFTED BY @Legend__bhai_</span>
        <i class="fa-solid fa-circle-check" style="color: #00f2fe; -webkit-text-fill-color: #00f2fe; font-size: 0.9rem;"></i>
    </a>
</div>

<!-- Hero Title & Icons -->
<div class="hero-title">⚡ LegendStream Pro</div>
<div class="hero-sub">Next-Gen Animated 4K/HD Video & Pure MP3 Audio Downloader</div>

<div class="platform-bar">
    <div class="plat-icon" title="YouTube"><i class="fa-brands fa-youtube" style="color:#ff0033;"></i></div>
    <div class="plat-icon" title="Instagram"><i class="fa-brands fa-instagram" style="color:#e1306c;"></i></div>
    <div class="plat-icon" title="Facebook"><i class="fa-brands fa-facebook" style="color:#1877f2;"></i></div>
    <div class="plat-icon" title="X / Twitter"><i class="fa-brands fa-x-twitter" style="color:#00f2fe;"></i></div>
    <div class="plat-icon" title="TikTok / Shorts"><i class="fa-brands fa-tiktok" style="color:#a855f7;"></i></div>
</div>
""", unsafe_allow_html=True)

# Main Input Container
with st.container():
    url = st.text_input(
        "🔗 Paste Video URL Here:",
        placeholder="https://www.youtube.com/watch?v=... or Instagram Reel link"
    )

    col1, col2 = st.columns([1.3, 1])
    with col1:
        format_choice = st.selectbox(
            "🎛️ Select Quality & Format:",
            [
                "🔥 1080p Full HD (MP4)",
                "⚡ 720p HD Ready (MP4)",
                "📱 480p Fast Save (MP4)",
                "🎵 MP3 Studio Audio (192kbps)"
            ]
        )
    with col2:
        st.write("")
        st.write("")
        start_btn = st.button("🚀 Fetch & Prepare")

def format_duration(seconds):
    if not seconds:
        return "Live / Short"
    mins, secs = divmod(int(seconds), 60)
    hrs, mins = divmod(mins, 60)
    if hrs > 0:
        return f"{hrs}h {mins}m {secs}s"
    return f"{mins}m {secs}s"

if start_btn:
    if not url.strip():
        st.warning("⚠️ Bhai, pehle kisi video ya Reel ka link paste karein!")
    else:
        temp_dir = tempfile.mkdtemp()
        output_template = os.path.join(temp_dir, "%(title).75B.%(ext)s")

        # Live Progress Elements
        status_box = st.empty()
        progress_bar = st.progress(0)
        preview_placeholder = st.empty()

        def progress_hook(d):
            if d["status"] == "downloading":
                raw_pct = d.get("_percent_str", "0%")
                clean_pct = re.sub(r"\x1b\[[0-9;]*m", "", raw_pct).replace("%", "").strip()
                raw_speed = re.sub(r"\x1b\[[0-9;]*m", "", d.get("_speed_str", "Fast")).strip()
                raw_eta = re.sub(r"\x1b\[[0-9;]*m", "", d.get("_eta_str", "00:00")).strip()
                try:
                    val = min(int(float(clean_pct)), 100)
                    progress_bar.progress(val)
                    status_box.markdown(
                        f"<p style='text-align:center; color:#00f2fe; font-weight:700;'>"
                        f"⚡ Downloading Stream: {val}% &nbsp;|&nbsp; 🚀 Speed: {raw_speed} &nbsp;|&nbsp; ⏳ ETA: {raw_eta}</p>",
                        unsafe_allow_html=True
                    )
                except ValueError:
                    pass
            elif d["status"] == "finished":
                progress_bar.progress(100)
                status_box.markdown(
                    "<p style='text-align:center; color:#10b981; font-weight:700;'>"
                    "✨ Stream Extracted! Merging High-Definition Audio & Video via FFmpeg...</p>",
                    unsafe_allow_html=True
                )

        if "MP3" in format_choice:
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": output_template,
                "noplaylist": True,
                "progress_hooks": [progress_hook],
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }
        else:
            res_match = re.search(r"(\d+)p", format_choice)
            res = res_match.group(1) if res_match else "720"
            ydl_opts = {
                "format": f"bestvideo[height<={res}]+bestaudio/best[height<={res}]/best",
                "merge_output_format": "mp4",
                "outtmpl": output_template,
                "noplaylist": True,
                "progress_hooks": [progress_hook],
            }

        try:
            status_box.markdown(
                "<p style='text-align:center; color:#f472b6; font-weight:700;'>"
                "🔍 Analyzing Link & Fetching Metadata...</p>",
                unsafe_allow_html=True
            )
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url.strip(), download=True)

            # Render Rich Preview Card
            title = info.get("title", "Media Stream")
            thumb = info.get("thumbnail", "")
            uploader = info.get("uploader", "Verified Creator")
            duration_str = format_duration(info.get("duration"))
            views = info.get("view_count")
            views_str = f"{views:,} views" if views else "HD Stream"

            if thumb:
                preview_placeholder.markdown(f"""
                <div class="video-card">
                    <img src="{thumb}" class="video-thumb" alt="Thumbnail" />
                    <div style="font-size:1.2rem; font-weight:800; color:#ffffff;">{title}</div>
                    <div class="meta-badges">
                        <span class="badge"><i class="fa-solid fa-user-astronaut"></i> {uploader}</span>
                        <span class="badge"><i class="fa-solid fa-clock"></i> {duration_str}</span>
                        <span class="badge"><i class="fa-solid fa-eye"></i> {views_str}</span>
                        <span class="badge" style="color:#f472b6;"><i class="fa-solid fa-bolt"></i> @Legend__bhai_ Engine</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            files = os.listdir(temp_dir)
            if files:
                file_path = os.path.join(temp_dir, files[0])
                file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

                with open(file_path, "rb") as f:
                    file_bytes = f.read()

                st.balloons()
                status_box.empty()
                st.success(f"✅ Ready! File Size: {file_size_mb:.2f} MB — Niche click karke save karein:")

                st.download_button(
                    label=f"⬇️ SAVE TO DEVICE — {files[0]} ({file_size_mb:.1f} MB)",
                    data=file_bytes,
                    file_name=files[0],
                    mime="application/octet-stream"
                )
        except Exception as e:
            status_box.empty()
            st.error(f"❌ Download Error: {str(e)}")
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

# Glowing Instagram Footer Card
st.markdown("""
<div class="insta-footer">
    <div style="font-size: 1.25rem; font-weight: 800; color: #ffffff;">
        🔥 Designed & Powered by <span style="color: #00f2fe;">Legend Bhai</span>
    </div>
    <div style="font-size: 0.9rem; color: #cbd5e1; margin-top: 4px;">
        Follow on Instagram for more crazy full-stack tools, 3D animations & updates!
    </div>
    <a href="https://instagram.com/Legend__bhai_" target="_blank" class="insta-btn">
        <i class="fa-brands fa-instagram" style="font-size: 1.3rem;"></i>
        <span>Follow @Legend__bhai_</span>
    </a>
</div>
""", unsafe_allow_html=True)
        
