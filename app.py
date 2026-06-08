import streamlit as st
import yt_dlp
import os

# వెబ్‌సైట్ ప్రొఫైల్ లుక్ సెట్ చేస్తున్నాం
st.set_page_config(page_title="Social Downloader", page_icon="✨", layout="centered")

st.title("✨ All-in-One Social Media Downloader")
st.write("యాడ్స్ లేవు, అశ్లీల పాప్-అప్స్ లేవు! సూపర్ క్లీన్ గా డౌన్‌లోడ్ చేసుకోండి.")

# లింక్ బాక్స్
video_url = st.text_input("🔗 ఇన్‌స్టాగ్రామ్ లేదా యూట్యూబ్ లింక్ ఇక్కడ పేస్ట్ చేయండి:")

if st.button("Get Download Link 🚀"):
    if video_url:
        with st.spinner("బ్యాక్‌గ్రౌండ్ లో లింక్ జనరేట్ అవుతోంది... ప్లీజ్ వెయిట్..."):
            try:
                # yt-dlp కాన్ఫిగరేషన్ (వీడియో లింక్ మాత్రమే తెచ్చుకోవడానికి)
                ydl_opts = {
                    'format': 'best',
                    'quiet': True,
                    'no_warnings': True,
                }
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(video_url, download=False)
                    # అసలైన డైరెక్ట్ వీడియో యుఆర్ఎల్ ని తీసుకుంటున్నాం
                    direct_link = info.get('url', None)
                    title = info.get('title', 'video')
                
                if direct_link:
                    st.success("🎉 మీ డౌన్‌లోడ్ లింక్ రెడీ అయిపోయింది!")
                    # అందమైన బటన్ ద్వారా డైరెక్ట్ వీడియో ఓపెన్ లేదా డౌన్లోడ్ అయ్యేలా లింక్ ఇస్తున్నాం
                    st.video(direct_link)
                    st.markdown(f'[👉 క్లిక్ చేసి వీడియో డౌన్‌లోడ్ చేసుకోండి]({direct_link})')
                else:
                    st.error("లింక్ దొరకలేదు ఫ్రెండ్! ఒకసారి యుఆర్ఎల్ కరెక్ట్ గా ఉందో లేదో చూడు.")
                    
            except Exception as e:
                st.error("ఇన్‌స్టాగ్రామ్/యూట్యూబ్ సర్వర్ బ్లాక్ చేసింది. క్లౌడ్ ఐపీ ఇష్యూ వల్ల కొన్ని లింక్స్ అప్పుడప్పుడు ఫెయిల్ అవ్వచ్చు ఫ్రెండ్.")
    else:
        st.warning("ప్లీజ్, ఫస్ట్ ఏదైనా ఒక లింక్ పేస్ట్ చేయండి ఫ్రెండ్!")