import streamlit as gp
gp.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

tn_year=gp.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
ab_year=tn_yaer-543
gp.header(f"ปี ค.ศ. คือ : {ab_yaer}")
