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
    add_number = st.slider('选择一个数字', 0, 100)
    st.write(f"你选择的数字是: {add_number}")
    options = st.multiselect('选择一些选项', ['苹果', '香蕉', '樱桃'])
    st.write('你选择的水果是:', options)

if __name__ == "__main__":
    main()
