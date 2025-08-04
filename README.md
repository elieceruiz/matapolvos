# 💊 Matapolvos – Simulador Crítico de Consulta Íntima

Una App demo construida en Streamlit que simula una herramienta para consultar el estado de salud sexual de una persona antes de un encuentro íntimo, a partir de su número de cédula o celular.

## 🔍 Objetivo

La aplicación busca abrir el debate sobre:

- Acceso a información personal en contextos de consentimiento sexual
- Vigilancia médica y perfilamiento
- Poder y exposición digital en dinámicas íntimas

## 🧪 ¿Cómo funciona?

1. El usuario ingresa una cédula o número de teléfono.
2. Selecciona un escenario simulado (desde sin EPS hasta con prueba reciente).
3. La App muestra una respuesta simulada, y registra el acceso en MongoDB.
4. Si el número se consulta múltiples veces, lanza alertas sutiles.

> 💡 *"¿Quién consulta a quién? ¿Y quién queda expuesto en este sistema?"*

## 🛠️ Requisitos

- Python 3.9+
- MongoDB (local o Atlas)
- Streamlit

## ⚙️ Setup rápido

```bash
pip install -r requirements.txt
streamlit run app.py
