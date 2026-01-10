import streamlit as st
import anthropic

# إعداد الصفحة
st.set_page_config(page_title="AI Humanizer 2026", page_icon="🚀")

st.title("🚀 محول النصوص للأسلوب البشري")
st.subheader("حول نصوص الذكاء الاصطناعي إلى نصوص بشرية بضغطة زر")

# وضع مفتاح الـ API
MY_KEY = st.secrets["ANTHROPIC_API_KEY"]
client = anthropic.Anthropic(api_key=MY_KEY)

# صندوق إدخال النص
user_input = st.text_area("أدخل نص ChatGPT هنا:", height=200)

if st.button("تحويل الآن ✨"):
    if user_input:
        with st.spinner('جاري لمس النص بسحر بشري...'):
            try:
                message = client.messages.create(
                    model="claude-sonnet-4-5-20250929",
                    max_tokens=1500,
                    temperature=0.85,
                    system="أنت محرر بشري عالمي. أعد صياغة النص ليكون طبيعياً ومذهلاً.",
                    messages=[{"role": "user", "content": f"حول هذا لأسلوب بشري: {user_input}"}]
                )
                result = message.content[0].text
                st.success("تم التحويل بنجاح!")
                st.markdown("### النص البشري الناتج:")
                st.write(result)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("من فضلك أدخل نصاً أولاً.")
