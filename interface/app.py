import streamlit as st

st.set_page_config(page_title="Bank Statement Analyzer", layout="wide")

st.title("📊 Bank Statement Analyzer")
st.write("Faça upload de um extrato bancário em PDF para começar a análise.")

uploaded_file = st.file_uploader("Selecione um arquivo PDF", type="pdf")

if uploaded_file:
    st.success("Arquivo carregado com sucesso!")
    # Aqui no futuro chamaremos a extração e processamento dos dados
