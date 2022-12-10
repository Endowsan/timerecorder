# 1. Streamlitと必要なライブラリをインポートする
import streamlit as st
import time

# 2. ボタンを配置する
button = st.button("Click")

# 3. ボタンが押されたときの処理を設定する
if button:
    # 押された時間を取得する
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    st.write(f"Button clicked at {current_time}")
