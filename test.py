import streamlit as st

def main():
    st.title('我的第一个Streamlit应用')
    message = st.text_input("请输入你的名字", "Streamlit")
    if message:
        st.write(f"你好, {message}!")
    else:
        st.write("请输入你的名字")
    if st.button("点击我"):
        st.write("按钮被点击了！")

if __name__ == "__main__":
    main()
