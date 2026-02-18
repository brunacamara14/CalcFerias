import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

# Configuração da página (título e ícone)
st.set_page_config(page_title="Contagem Regressiva de Férias", page_icon="🏖️")

# Estilo simples para centralizar e aumentar fontes
st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título do App
st.title("🏖️ Calculadora de Férias")
st.write("Insira a data do início das suas férias para ver quanto tempo falta.")

# --- Entrada de Dados ---
# Data de hoje (pode ser automático, mas fixei no exemplo para bater com sua conta)
hoje = date.today() 

# Input do usuário (Data das férias)
data_ferias = st.date_input(
    "Quando começam as férias?",
    value=date(2026, 7, 13),  # O Python exige ordem: Ano, Mês, Dia
    min_value=hoje,
    format="DD/MM/YYYY"       # Isso força o site a MOSTRAR como Dia/Mês/Ano
)

st.write("---")

# --- Lógica de Cálculo ---
if data_ferias > hoje:
    # Cálculo total de dias
    diferenca_total = data_ferias - hoje
    total_dias = diferenca_total.days
    
    # Cálculo de Meses e Dias (usando relativedelta para precisão de calendário)
    diferenca_relativa = relativedelta(data_ferias, hoje)
    meses = diferenca_relativa.months
    dias_restantes = diferenca_relativa.days
    
    # --- Exibição dos Resultados ---
    st.subheader("Do dia {} até {}:".format(hoje.strftime('%d/%m/%Y'), data_ferias.strftime('%d/%m/%Y')))
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"📅 **Total de dias:**\n\n# {total_dias} dias")
        
    with col2:
        texto_meses = f"{meses} meses" if meses > 0 else ""
        texto_dias = f"{dias_restantes} dias"
        
        # Conector "e" apenas se tiver meses e dias
        conector = " e " if meses > 0 and dias_restantes > 0 else ""
        
        st.success(f"📆 **Equivalente a:**\n\n# {texto_meses}{conector}{texto_dias}")

elif data_ferias == hoje:
    st.balloons()
    st.success("🎉 É hoje! Boas férias!")
else:
    st.warning("Essa data já passou!")