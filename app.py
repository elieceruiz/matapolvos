import streamlit as st
from datetime import datetime
from pymongo import MongoClient

# === CONFIGURACIÓN DE LA APP ===
st.set_page_config(page_title="💊 Consulta de Salud Íntima", layout="centered")
st.title("💊 Simulación de Consulta Íntima")

# === CONEXIÓN SEGURA A MONGODB ===
MONGO_URI = st.secrets["mongo_uri"]
client = MongoClient(MONGO_URI)
db = client["salud_sexual"]
collection = db["consultas"]

# === INPUT DE USUARIO ===
cedula = st.text_input("📇 Ingresa tu número de cédula o celular")

# === ESCENARIOS CON PISTAS — SELECCIÓN CON TEXTO CLARO ===
select_options = {
    "1": "1️⃣ Sin afiliación ni historial registrado",
    "2": "2️⃣ Con EPS, pero sin pruebas recientes",
    "3": "3️⃣ Prueba hecha hace 1 mes (registro actualizado)",
    "4": "4️⃣ Prueba hecha hoy (alta confianza)"
}

opcion_label = st.selectbox("🧪 Selecciona un escenario de simulación:", list(select_options.values()))
opcion = [key for key, val in select_options.items() if val == opcion_label][0]

# === FECHAS SIMULADAS POR ESCENARIO ===
escenarios = {
    "1": "2020-06-10",
    "2": "2022-11-03",
    "3": "2025-07-04",
    "4": "2025-08-04"
}

# === AL CONSULTAR ===
if st.button("Consultar") and cedula.strip():
    cedula_limpia = cedula.strip()
    hoy = datetime.now()

    # === REGISTRAR CONSULTA EN MONGODB ===
    collection.insert_one({
        "cedula": cedula_limpia,
        "escenario": opcion,
        "fecha_consulta": hoy,
        "timestamp": int(hoy.timestamp())
    })

    # === CONTAR CUÁNTAS VECES SE HA CONSULTADO ESA CÉDULA ===
    total_consultas = collection.count_documents({"cedula": cedula_limpia})

    # === ESCENARIO PERSONALIZADO: ELIECER ===
    if cedula_limpia == "1106889506":
        if opcion == "1":
            st.error("❌ No se encontró afiliación activa a ninguna EPS.")
            st.info("📭 No hay pruebas de VIH ni sífilis registradas.")
        else:
            fecha_str = escenarios[opcion]
            fecha_examen = datetime.strptime(fecha_str, "%Y-%m-%d")
            dias = (hoy - fecha_examen).days

            st.markdown("### 👤 Consulta registrada para: **ELIECER ANDREI RUIZ HIGUITA**")
            st.markdown("🏥 EPS: **SANITAS**")
            st.markdown("📅 Afiliado desde hace varios años.")
            st.markdown("---")
            st.success(f"🗓 Último examen registrado: **{fecha_examen.strftime('%d de %B de %Y')}**")
            st.info(f"⌛ Han pasado **{dias} días** desde esa fecha.")
            st.markdown("📄 [Descargar resultado (PDF simulado)](#)", unsafe_allow_html=True)

    else:
        fecha_str = escenarios[opcion]
        fecha_examen = datetime.strptime(fecha_str, "%Y-%m-%d")
        dias = (hoy - fecha_examen).days

        st.success(f"🗓 Último examen registrado: **{fecha_examen.strftime('%d de %B de %Y')}**")
        st.info(f"⌛ Han pasado **{dias} días** desde esa fecha.")
        st.markdown("📄 [Descargar resultado (PDF simulado)](#)", unsafe_allow_html=True)

    # === MOSTRAR CONTADOR DE CONSULTAS (TODOS LOS CASOS) ===
    st.warning(f"📊 Esta cédula ha sido consultada **{total_consultas} veces** en esta App.")

    if total_consultas >= 5:
        st.error("👁 ¿Demasiado interés? Este historial ha sido accedido con frecuencia.")
    elif total_consultas >= 3:
        st.info("👁 Consulta frecuente detectada.")

    # === CIERRE REFLEXIVO (TODOS LOS CASOS) ===
    st.markdown("---")
    st.markdown("💡 *¿Quién consulta a quién? ¿Quién queda expuesto en este sistema?*")
