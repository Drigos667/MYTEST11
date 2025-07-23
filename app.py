import streamlit as st
import requests
import json

API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://meusite.com",
    "X-Title": "chat-openrouter-test"
}

st.title("CryptoBot")

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    if not pergunta.strip():
        st.warning("Por favor, digite uma pergunta.")
    else:
        with st.spinner("Processando..."):
            body = {
                "model": "mistralai/mistral-7b-instruct:free",
                "messages": [
                    {"role": "system", "content": "Você é um assistente útil que responde sempre em português."},
                    {"role": "user", "content": pergunta}
                ]
            }
            try:
                response = requests.post(url, headers=headers, data=json.dumps(body))
                response.raise_for_status()
                resposta = response.json()["choices"][0]["message"]["content"]
                st.success("Resposta:")
                st.write(resposta)
            except Exception as e:
                st.error(f"Erro: {str(e)}")