import streamlit as st
st.title("ร้านหมีเบเกอร์ร่า")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
vat = price * 0.07
net_price = price - vat
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("กลุ่มที่ 2")
