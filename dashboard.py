import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(layout="wide", page_title="Painel ROV")

st.title("Painel de Monitoramento")

def buscar_dados():
    conn = sqlite3.connect("telemetria.db")
    query = """
        SELECT timestamp, profundidade, temperatura, pressao 
        FROM telemetria 
        ORDER BY id DESC 
        LIMIT 60
    """
    df = pd.read_sql(query, conn)
    conn.close()
    
    if not df.empty:
        dt_col = pd.to_datetime(df["timestamp"], errors="coerce")
        df["Hora"] = dt_col.dt.strftime("%H:%M:%S")
        df["Minuto"] = dt_col.dt.strftime("%M:%S")
        
        df = df.rename(columns={
            "profundidade": "Profundidade (m)",
            "pressao": "Pressão (bar)",
            "temperatura": "Temperatura (°C)"
        })
        
        df = df.set_index("Minuto")
        df = df.iloc[::-1]
    return df

@st.fragment(run_every="0.5s")
def atualizar_painel():
    try:
        df = buscar_dados()
        
        if not df.empty:
            leitura_atual = df.iloc[-1]            
            col1, col2, col3, col4 = st.columns(4)
            
            col1.metric("Profundidade (m)", f"{leitura_atual['Profundidade (m)']:.2f}")
            col2.metric("Temperatura (°C)", f"{leitura_atual['Temperatura (°C)']:.2f}")
            col3.metric("Pressão (bar)", f"{leitura_atual['Pressão (bar)']:.2f}")
            col4.metric("Horário", leitura_atual["Hora"]) 
            
            st.markdown("---")
                        
            grafico_esq, grafico_dir = st.columns(2)
            
            with grafico_esq:
                st.subheader("Profundidade Atual")
                st.line_chart(df['Profundidade (m)'])

            with grafico_dir:
                st.subheader("Pressão")
                st.line_chart(df['Pressão (bar)'])
            st.markdown("---")
            st.subheader("Temperatura")
            st.line_chart(df['Temperatura (°C)'])
            
        else:
            st.warning("Aguardando dados...")
            
    except Exception as e:
        st.error(f"Erro ao ler o banco de dados: {e}")

atualizar_painel()