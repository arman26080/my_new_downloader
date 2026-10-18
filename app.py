import os
import shutil
import tempfile
import streamlit as st
import yt_dlp

st.set_page_config(page_title="Video Downloader", page_icon="📥")
st.title("📥 Media Stream Downloader")
st.write("Kisi bhi video ka link paste karein aur format select karke download karein.")

url = st.text_input("Video URL:", placeholder="https://www.youtube.com/watch?v=...")
format_choice = st.selectbox(
    "Format Chunein:",
    ["720p MP4 Video", "1080p MP4 Video", "480p MP4 Video", "MP3 Audio Only"]
)

if st.button("Fetch & Prepare Download") and url:
    with st.spinner("Server par video tayyar ho rahi hai... Thoda wait karein..."):
        temp_dir = tempfile.mkdtemp()
        output_template = os.path.join(temp_dir, "%(title).80B.%(ext)s")

        if "MP3" in format_choice:
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": output_template,
                "noplaylist": True,
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }
        else:
            res = format_choice.split("p")[0]
            ydl_opts = {
                "format": f"bestvideo[height<={res}]+bestaudio/best[height<={res}]/best",
                "merge_output_format": "mp4",
                "outtmpl": output_template,
                "noplaylist": True,
            }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(url, download=True)

            files = os.listdir(temp_dir)
            if files:
                file_path = os.path.join(temp_dir, files[0])
                with open(file_path, "rb") as f:
                    file_bytes = f.read()

                st.success("✅ File tayyar hai! Niche button dabakar apne phone/PC mein save karein:")
                st.download_button(
                    label=f"⬇️ Save {files[0]}",
                    data=file_bytes,
                    file_name=files[0],
                    mime="application/octet-stream"
                )
        except Exception as e:
            st.error(f"Download Error: {str(e)}")
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
          
