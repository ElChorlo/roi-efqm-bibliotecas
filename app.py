"""ROI EFQM de las bibliotecas universitarias (Bibliotecas Líderes EFQM, 2023-2025).

Ejecución:  py -m streamlit run app.py
Datos: instantánea del informe de Power BI de la Biblioteca de la Universidad de Sevilla.
"""
import json

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="ROI EFQM de las bibliotecas universitarias", layout="wide")

LIBS = pd.DataFrame(json.loads(r'''[{"biblioteca": "BUS", "anio": 2023, "valor_meur": 1131.24, "coste_personal_meur": 9.98, "coste_recursos_meur": 5.3, "roi_publicado": 74.04, "nota": "Valor reconstruido como suma de los 14 servicios (el informe lo muestra como 1,13 mil M€)"}, {"biblioteca": "BUS", "anio": 2024, "valor_meur": 816.02, "coste_personal_meur": 10.84, "coste_recursos_meur": 5.7, "roi_publicado": 49.44, "nota": ""}, {"biblioteca": "BUS", "anio": 2025, "valor_meur": 318.76, "coste_personal_meur": 11.05, "coste_recursos_meur": 5.6, "roi_publicado": 19.14, "nota": ""}, {"biblioteca": "UAH", "anio": 2023, "valor_meur": 114.71, "coste_personal_meur": 3.69, "coste_recursos_meur": 1.7, "roi_publicado": 21.1, "nota": ""}, {"biblioteca": "UAH", "anio": 2024, "valor_meur": 123.41, "coste_personal_meur": 3.56, "coste_recursos_meur": 1.9, "roi_publicado": 22.8, "nota": ""}, {"biblioteca": "UAH", "anio": 2025, "valor_meur": 138.34, "coste_personal_meur": 5.32, "coste_recursos_meur": 1.9, "roi_publicado": 19.2, "nota": ""}, {"biblioteca": "UB", "anio": 2023, "valor_meur": 604.05, "coste_personal_meur": 11.39, "coste_recursos_meur": 5.6, "roi_publicado": 35.5, "nota": ""}, {"biblioteca": "UB", "anio": 2024, "valor_meur": 763.71, "coste_personal_meur": 11.72, "coste_recursos_meur": 5.6, "roi_publicado": 44.0, "nota": ""}, {"biblioteca": "UB", "anio": 2025, "valor_meur": 669.65, "coste_personal_meur": 12.02, "coste_recursos_meur": 6.2, "roi_publicado": 36.8, "nota": ""}, {"biblioteca": "UGR", "anio": 2023, "valor_meur": 617.76, "coste_personal_meur": 11.09, "coste_recursos_meur": 5.3, "roi_publicado": 37.6, "nota": ""}, {"biblioteca": "UGR", "anio": 2024, "valor_meur": 685.18, "coste_personal_meur": 11.06, "coste_recursos_meur": 5.5, "roi_publicado": 41.3, "nota": ""}, {"biblioteca": "UGR", "anio": 2025, "valor_meur": 120.24, "coste_personal_meur": 12.11, "coste_recursos_meur": 5.5, "roi_publicado": 6.8, "nota": ""}, {"biblioteca": "UV", "anio": 2023, "valor_meur": 318.48, "coste_personal_meur": 8.29, "coste_recursos_meur": 5.4, "roi_publicado": 23.3, "nota": ""}, {"biblioteca": "UV", "anio": 2024, "valor_meur": 131.72, "coste_personal_meur": 8.26, "coste_recursos_meur": 5.3, "roi_publicado": 9.7, "nota": ""}, {"biblioteca": "UV", "anio": 2025, "valor_meur": 352.07, "coste_personal_meur": 8.52, "coste_recursos_meur": 5.5, "roi_publicado": 25.1, "nota": ""}, {"biblioteca": "UZ", "anio": 2023, "valor_meur": 425.94, "coste_personal_meur": 6.66, "coste_recursos_meur": 3.0, "roi_publicado": 44.2, "nota": ""}, {"biblioteca": "UZ", "anio": 2024, "valor_meur": 1030.0, "coste_personal_meur": 6.54, "coste_recursos_meur": 3.1, "roi_publicado": 107.0, "nota": "Valor publicado redondeado a 10 M€ (1,03 y 1,28 mil M€)"}, {"biblioteca": "UZ", "anio": 2025, "valor_meur": 1280.0, "coste_personal_meur": 7.07, "coste_recursos_meur": 2.9, "roi_publicado": 128.5, "nota": "Valor publicado redondeado a 10 M€ (1,03 y 1,28 mil M€)"}]'''))
SERV = pd.DataFrame(json.loads(r'''[{"codigo": "S.0.1", "servicio": "Libros prestados", "bloque": "Libros prestados", "familia": "Colecciones", "anio": 2023, "valor_eur": 15668739.6, "valor_unitario_eur": 37.86, "unidad": "préstamo"}, {"codigo": "S.0.1", "servicio": "Libros prestados", "bloque": "Libros prestados", "familia": "Colecciones", "anio": 2024, "valor_eur": 12426778.56, "valor_unitario_eur": 37.72, "unidad": "préstamo"}, {"codigo": "S.0.1", "servicio": "Libros prestados", "bloque": "Libros prestados", "familia": "Colecciones", "anio": 2025, "valor_eur": 14039392.2, "valor_unitario_eur": 40.12, "unidad": "préstamo"}, {"codigo": "S.0.2", "servicio": "PI monografías", "bloque": "Resto de servicios", "familia": "Préstamo interbibliotecario", "anio": 2023, "valor_eur": 60902.08, "valor_unitario_eur": 45.86, "unidad": "préstamo"}, {"codigo": "S.0.2", "servicio": "PI monografías", "bloque": "Resto de servicios", "familia": "Préstamo interbibliotecario", "anio": 2024, "valor_eur": 63550.8, "valor_unitario_eur": 45.72, "unidad": "préstamo"}, {"codigo": "S.0.2", "servicio": "PI monografías", "bloque": "Resto de servicios", "familia": "Préstamo interbibliotecario", "anio": 2025, "valor_eur": 60823.68, "valor_unitario_eur": 48.12, "unidad": "préstamo"}, {"codigo": "S.0.3", "servicio": "PI artículos", "bloque": "Resto de servicios", "familia": "Préstamo interbibliotecario", "anio": 2023, "valor_eur": 126972.9, "valor_unitario_eur": 57.35, "unidad": "copia"}, {"codigo": "S.0.3", "servicio": "PI artículos", "bloque": "Resto de servicios", "familia": "Préstamo interbibliotecario", "anio": 2024, "valor_eur": 139894.56, "valor_unitario_eur": 57.24, "unidad": "copia"}, {"codigo": "S.0.3", "servicio": "PI artículos", "bloque": "Resto de servicios", "familia": "Préstamo interbibliotecario", "anio": 2025, "valor_eur": 117583.4, "valor_unitario_eur": 53.35, "unidad": "copia"}, {"codigo": "S.0.4", "servicio": "Descargas de libros electrónicos", "bloque": "Libros electrónicos", "familia": "Colecciones", "anio": 2023, "valor_eur": 13838095.02, "valor_unitario_eur": 37.86, "unidad": "descarga"}, {"codigo": "S.0.4", "servicio": "Descargas de libros electrónicos", "bloque": "Libros electrónicos", "familia": "Colecciones", "anio": 2024, "valor_eur": 15157555.68, "valor_unitario_eur": 37.72, "unidad": "descarga"}, {"codigo": "S.0.4", "servicio": "Descargas de libros electrónicos", "bloque": "Libros electrónicos", "familia": "Colecciones", "anio": 2025, "valor_eur": 6830791.08, "valor_unitario_eur": 40.12, "unidad": "descarga"}, {"codigo": "S.0.5", "servicio": "Descargas de artículos en línea", "bloque": "Descargas de artículos", "familia": "Colecciones", "anio": 2023, "valor_eur": 63207842.94, "valor_unitario_eur": 53.46, "unidad": "descarga"}, {"codigo": "S.0.5", "servicio": "Descargas de artículos en línea", "bloque": "Descargas de artículos", "familia": "Colecciones", "anio": 2024, "valor_eur": 67951632.75, "valor_unitario_eur": 53.25, "unidad": "descarga"}, {"codigo": "S.0.5", "servicio": "Descargas de artículos en línea", "bloque": "Descargas de artículos", "familia": "Colecciones", "anio": 2025, "valor_eur": 42159560.64, "valor_unitario_eur": 49.36, "unidad": "descarga"}, {"codigo": "S.0.6", "servicio": "Descargas de repositorios", "bloque": "Repositorio institucional", "familia": "Colecciones", "anio": 2023, "valor_eur": 1034451000.0, "valor_unitario_eur": 53.46, "unidad": "descarga"}, {"codigo": "S.0.6", "servicio": "Descargas de repositorios", "bloque": "Repositorio institucional", "familia": "Colecciones", "anio": 2024, "valor_eur": 716088108.0, "valor_unitario_eur": 53.25, "unidad": "descarga"}, {"codigo": "S.0.6", "servicio": "Descargas de repositorios", "bloque": "Repositorio institucional", "familia": "Colecciones", "anio": 2025, "valor_eur": 250274746.56, "valor_unitario_eur": 49.36, "unidad": "descarga"}, {"codigo": "S.0.7", "servicio": "Servicios de referencia", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2023, "valor_eur": 37717.65, "valor_unitario_eur": 12.51, "unidad": "consulta de 1/2 h"}, {"codigo": "S.0.7", "servicio": "Servicios de referencia", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2024, "valor_eur": 59938.8, "valor_unitario_eur": 12.55, "unidad": "consulta de 1/2 h"}, {"codigo": "S.0.7", "servicio": "Servicios de referencia", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2025, "valor_eur": 62184.06, "valor_unitario_eur": 14.22, "unidad": "consulta de 1/2 h"}, {"codigo": "S.0.8", "servicio": "Consultas de apoyo a docencia e investigación", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2023, "valor_eur": 1651.32, "valor_unitario_eur": 12.51, "unidad": "consulta de 1/2 h"}, {"codigo": "S.0.8", "servicio": "Consultas de apoyo a docencia e investigación", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2024, "valor_eur": 1280.1, "valor_unitario_eur": 12.55, "unidad": "consulta de 1/2 h"}, {"codigo": "S.0.8", "servicio": "Consultas de apoyo a docencia e investigación", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2025, "valor_eur": 8958.6, "valor_unitario_eur": 14.22, "unidad": "consulta de 1/2 h"}, {"codigo": "S.0.9", "servicio": "Informes de calidad en publicaciones", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2023, "valor_eur": 672809.0, "valor_unitario_eur": 1041.5, "unidad": "informe"}, {"codigo": "S.0.9", "servicio": "Informes de calidad en publicaciones", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2024, "valor_eur": 600945.5, "valor_unitario_eur": 1041.5, "unidad": "informe"}, {"codigo": "S.0.9", "servicio": "Informes de calidad en publicaciones", "bloque": "Resto de servicios", "familia": "Información y apoyo", "anio": 2025, "valor_eur": 1340410.5, "valor_unitario_eur": 1041.5, "unidad": "informe"}, {"codigo": "S.10", "servicio": "Formación de usuarios", "bloque": "Resto de servicios", "familia": "Formación", "anio": 2023, "valor_eur": 111663.65, "valor_unitario_eur": 58.31, "unidad": "hora"}, {"codigo": "S.10", "servicio": "Formación de usuarios", "bloque": "Resto de servicios", "familia": "Formación", "anio": 2024, "valor_eur": 116328.45, "valor_unitario_eur": 58.31, "unidad": "hora"}, {"codigo": "S.10", "servicio": "Formación de usuarios", "bloque": "Resto de servicios", "familia": "Formación", "anio": 2025, "valor_eur": 113412.95, "valor_unitario_eur": 58.31, "unidad": "hora"}, {"codigo": "S.11", "servicio": "Formación de bibliotecarios", "bloque": "Resto de servicios", "familia": "Formación", "anio": 2023, "valor_eur": 481582.29, "valor_unitario_eur": 58.31, "unidad": "hora"}, {"codigo": "S.11", "servicio": "Formación de bibliotecarios", "bloque": "Resto de servicios", "familia": "Formación", "anio": 2024, "valor_eur": 494935.28, "valor_unitario_eur": 58.31, "unidad": "hora"}, {"codigo": "S.11", "servicio": "Formación de bibliotecarios", "bloque": "Resto de servicios", "familia": "Formación", "anio": 2025, "valor_eur": 665258.79, "valor_unitario_eur": 58.31, "unidad": "hora"}, {"codigo": "S.12", "servicio": "Uso de salas de estudio o reunión", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2023, "valor_eur": 1501400.88, "valor_unitario_eur": 19.62, "unidad": "hora"}, {"codigo": "S.12", "servicio": "Uso de salas de estudio o reunión", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2024, "valor_eur": 1951836.84, "valor_unitario_eur": 19.62, "unidad": "hora"}, {"codigo": "S.12", "servicio": "Uso de salas de estudio o reunión", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2025, "valor_eur": 2281060.44, "valor_unitario_eur": 19.62, "unidad": "hora"}, {"codigo": "S.13", "servicio": "Uso de ordenadores", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2023, "valor_eur": 1064614.25, "valor_unitario_eur": 7.73, "unidad": "día de préstamo"}, {"codigo": "S.13", "servicio": "Uso de ordenadores", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2024, "valor_eur": 954338.07, "valor_unitario_eur": 7.73, "unidad": "día de préstamo"}, {"codigo": "S.13", "servicio": "Uso de ordenadores", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2025, "valor_eur": 796390.98, "valor_unitario_eur": 7.73, "unidad": "día de préstamo"}, {"codigo": "S.14", "servicio": "Visitas guiadas", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2023, "valor_eur": 12639.36, "valor_unitario_eur": 13.62, "unidad": "asistente"}, {"codigo": "S.14", "servicio": "Visitas guiadas", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2024, "valor_eur": 12094.56, "valor_unitario_eur": 13.62, "unidad": "asistente"}, {"codigo": "S.14", "servicio": "Visitas guiadas", "bloque": "Resto de servicios", "familia": "Espacios y equipos", "anio": 2025, "valor_eur": 12639.36, "valor_unitario_eur": 13.62, "unidad": "asistente"}]'''))
YEARS = [2023, 2024, 2025]
# Paleta apta para daltonismo (Okabe-Ito) y colores de texto con contraste alto
BLUE, ORANGE, GREEN, RED, PURPLE, SKY, GREY = "#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#9AA5B8"
INK, MUTED, GRID = "#1B1F27", "#4A5568", "#E3E8F0"
COL = [BLUE, ORANGE, GREEN, PURPLE, SKY, RED]
BLOQUES = ["Repositorio institucional", "Descargas de artículos", "Libros electrónicos", "Libros prestados", "Resto de servicios"]
BCOL = dict(zip(BLOQUES, [BLUE, ORANGE, GREEN, PURPLE, GREY]))
BTXT = dict(zip(BLOQUES, ["white", INK, INK, INK, INK]))
CORTO = dict(zip(BLOQUES, ["Repositorio", "Artículos", "Libros electrónicos", "Libros prestados", "Resto"]))


def n(v, d=1):
    return f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(v, d=1, signo=False):
    s = n(abs(v), d) + " %"
    return (("+" if v > 0 else "−" if v < 0 else "") + s) if signo else s


def fig_base(fig, h=400, **kw):
    leg = dict(orientation="h", y=-0.18, font_size=14)
    leg.update(kw.pop("legend", {}))
    fig.update_layout(template="plotly_white", height=h, margin=dict(l=10, r=20, t=20, b=10),
                      paper_bgcolor="white", plot_bgcolor="white", font=dict(size=14, color=INK),
                      hoverlabel=dict(font_size=14, bgcolor="white", font_color=INK),
                      legend=leg, **kw)
    fig.update_xaxes(gridcolor=GRID, zerolinecolor=GRID, linecolor=GRID, tickfont_size=13)
    fig.update_yaxes(gridcolor=GRID, zerolinecolor=GRID, linecolor=GRID, tickfont_size=13)
    return fig


def show(fig, key, **kw):
    """Gráfico con tema propio (no depende del tema oscuro o claro del navegador) y sin barra de herramientas."""
    st.plotly_chart(fig, theme=None, width="stretch", key=key, config={"displayModeBar": False}, **kw)


def titular(texto, ayuda=None):
    st.markdown(f"##### {texto}")
    if ayuda:
        st.caption(ayuda)


# ------------------------------------------------------------------ cálculos
LIBS["coste"] = LIBS.coste_personal_meur + LIBS.coste_recursos_meur
LIBS["roi"] = LIBS.roi_publicado
LIBS["puesto"] = LIBS.groupby("anio")["roi"].rank(ascending=False, method="min").astype(int)
LIBS["mediana"] = LIBS.groupby("anio")["roi"].transform("median")

filas = []
for y in YEARS:
    s = SERV[SERV.anio == y]
    tot = s.valor_eur.sum()
    por = s.groupby("bloque").valor_eur.sum()
    b = LIBS[(LIBS.biblioteca == "BUS") & (LIBS.anio == y)].iloc[0]
    resto = LIBS[(LIBS.anio == y) & (LIBS.biblioteca != "BUS")].roi.mean()
    cod = lambda c: s[s.codigo == c].valor_eur.sum()
    fila = dict(anio=y, valor=tot / 1e6, coste=b.coste, personal=b.coste_personal_meur, recursos=b.coste_recursos_meur,
                roi=b.roi, puesto=int(b.puesto), media_resto=resto, ratio=b.roi / resto)
    for k in BLOQUES:
        fila[k] = por[k] / 1e6
    repo, art, ebk = cod("S.0.6"), cod("S.0.5"), cod("S.0.4")
    fila["roi_sin_repo"] = (tot - repo) / 1e6 / b.coste
    fila["roi_sin_desc"] = (tot - repo - art - ebk) / 1e6 / b.coste
    for f in (0.5, 0.25, 0.1):
        fila[f"roi_repo{int(f*100)}"] = (tot - repo * (1 - f)) / 1e6 / b.coste
    fila["desc_repo_m"] = repo / s[s.codigo == "S.0.6"].valor_unitario_eur.iloc[0] / 1e6
    filas.append(fila)
BUS = pd.DataFrame(filas).set_index("anio")

SERV["volumen"] = SERV.valor_eur / SERV.valor_unitario_eur
SERV["indice"] = SERV.groupby("codigo").volumen.transform(lambda x: x / x.iloc[0] * 100)


# ------------------------------------------------------------------ filtros
ESC = [("roi", "ROI publicado"), ("roi_repo50", "Repositorio al 50 %"), ("roi_repo25", "Repositorio al 25 %"),
       ("roi_repo10", "Repositorio al 10 %"), ("roi_sin_repo", "Sin repositorio"), ("roi_sin_desc", "Sin descargas digitales")]
MET = {"ROI (€ por €)": ("roi", "€"), "Valor total (M€)": ("valor_meur", "M€"), "Coste total (M€)": ("coste", "M€")}
TODAS = sorted(LIBS.biblioteca.unique())
FAMILIAS = sorted(SERV.familia.unique())
with st.sidebar:
    st.header("Filtros")
    anio = st.radio("Año", YEARS, index=2, horizontal=True)
    sel_libs = st.multiselect("Bibliotecas", TODAS, default=TODAS) or TODAS
    metrica = st.radio("Métrica del benchmarking", list(MET))
    bloques_sel = st.multiselect("Bloques de valor (BUS)", BLOQUES, default=BLOQUES) or BLOQUES
    familias_sel = st.multiselect("Familias de servicio (BUS)", FAMILIAS, default=FAMILIAS) or FAMILIAS
    esc_sel = st.multiselect("Escenarios de sensibilidad", [x[1] for x in ESC], default=[x[1] for x in ESC]) or [x[1] for x in ESC]
    st.caption("Los filtros afectan a los gráficos y tablas. Los indicadores, el puesto y la lectura usan siempre las seis bibliotecas y todos los servicios.")
col, unidad = MET[metrica]
LF = LIBS[LIBS.biblioteca.isin(sel_libs)]

# ------------------------------------------------------------------ estilo
st.markdown(
    """
<style>
html, body, [data-testid="stAppViewContainer"], .stApp { background: #FFFFFF; color: #1B1F27; font-size: 16px; }
[data-testid="stSidebar"] { background: #F3F6FB; }
[data-testid="stMetric"] { background: #F7F9FC; border: 1px solid #D5DCE8; border-radius: 10px; padding: 12px 14px; }
[data-testid="stMetricLabel"] p { font-size: 0.95rem; color: #2D3748; font-weight: 600; }
[data-testid="stMetricValue"] { font-size: 2.1rem; }
h1, h2, h3, h5 { color: #1B1F27; }
h2 { border-top: 2px solid #E3E8F0; padding-top: 1.1rem; margin-top: 1.4rem; }
[data-testid="stCaptionContainer"], .stCaption { color: #4A5568; font-size: 0.95rem; }
.lectura { font-size: 1.05rem; line-height: 1.65; }
</style>
""",
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------ cabecera
st.title("ROI de las bibliotecas universitarias")
st.caption("Bibliotecas Líderes EFQM · 2023-2025 · Fuente: informe de la Biblioteca de la Universidad de Sevilla")

b23, b24, b25 = BUS.loc[2023], BUS.loc[2024], BUS.loc[2025]
caida = (1 - b25.valor / b23.valor) * 100
repo_caida = (b23["Repositorio institucional"] - b25["Repositorio institucional"]) / (b23.valor - b25.valor) * 100
st.markdown(
    f"El ROI de la BUS pasa de **{n(b23.roi)} €** a **{n(b25.roi)} €** por euro invertido entre 2023 y 2025 "
    f"({pct((b25.roi / b23.roi - 1) * 100, 1, True)}). El valor total cae un **{pct(caida)}** y el coste sube un "
    f"**{pct((b25.coste / b23.coste - 1) * 100)}**, de modo que la variación procede del valor. Las descargas del "
    f"repositorio explican el **{pct(repo_caida)}** de esa pérdida."
)

with st.expander("Cómo leer este panel"):
    st.markdown(
        """
- **ROI** es el valor económico que generan los servicios por cada euro de coste (personal más recursos de información). Un ROI de 20 significa que cada euro invertido devuelve 20 euros de valor estimado.
- **Los filtros están en la barra lateral** (en el móvil, en la flecha de arriba a la izquierda). Permiten cambiar de año, elegir bibliotecas, la métrica y los servicios que se muestran.
- **Los gráficos se pueden leer sin leyenda**: las etiquetas están junto a cada elemento. Al pasar el cursor por encima aparece el dato exacto.
- **La BUS va siempre en azul** y el resto de bibliotecas en tonos neutros o distintos entre sí.
"""
    )

i = YEARS.index(anio)
act, prev = BUS.loc[anio], (BUS.loc[YEARS[i - 1]] if i else None)


def delta(campo):
    if prev is None:
        return None
    return pct((act[campo] / prev[campo] - 1) * 100, 1, True).replace("−", "-")


# ------------------------------------------------------------------ resumen
st.header("Resumen de la BUS")
st.caption(f"Año {anio}" + (f", con la variación respecto a {YEARS[i - 1]}." if prev is not None else ". Primer año de la serie, sin variación."))
c = st.columns(5)
c[0].metric("ROI publicado", n(act.roi), delta("roi"), help="Euros de valor por cada euro de coste. Valor de los servicios dividido entre el coste total.")
c[1].metric("Valor total (M€)", n(act.valor), delta("valor"), help="Suma del valor económico de los 14 servicios.")
c[2].metric("Coste total (M€)", n(act.coste), delta("coste"), delta_color="inverse", help="Personal más recursos de información. Si sube, se muestra en rojo.")
c[3].metric("ROI sin repositorio", n(act.roi_sin_repo), delta("roi_sin_repo"), help="ROI de la BUS si se excluyen las descargas del repositorio institucional.")
c[4].metric("Puesto por ROI", f"{int(act.puesto)}.º de 6", f"{n(act.ratio, 2)}× la media del resto", delta_color="off", delta_arrow="off",
            help="Posición de la BUS entre las seis bibliotecas según su ROI del año.")

# ------------------------------------------------------------------ benchmarking
st.header("Benchmarking con las otras cinco bibliotecas")
st.caption("El coste anual de cada biblioteca se mueve en un rango estrecho. El valor generado varía varias veces más, y con él el ROI.")
a, b = st.columns(2)

# --- barras horizontales del año seleccionado
with a:
    corto = metrica.split(" (")[0]
    orden = LF[LF.anio == anio].sort_values(col, ascending=False).biblioteca.tolist()
    d = LF[LF.anio == anio].set_index("biblioteca").loc[orden]
    ref = LF[LF.anio == 2023].set_index("biblioteca").loc[orden]
    if col == "roi" and "BUS" in orden:
        titular(f"En {anio}, la BUS ocupa el {int(act.puesto)}.º puesto de 6 en ROI",
                "Barras: año seleccionado. Rombo vacío: valor de 2023 como referencia.")
    else:
        titular(f"{corto} por biblioteca en {anio}", "Barras: año seleccionado. Rombo vacío: valor de 2023 como referencia.")
    f1 = go.Figure()
    f1.add_bar(y=orden, x=d[col], orientation="h", marker_color=[BLUE if x == "BUS" else GREY for x in orden],
               name=f"{anio}", showlegend=False, hovertemplate="%{y}: %{x:.1f} " + unidad + "<extra></extra>")
    fin = [max(d[col][x], ref[col][x]) if anio != 2023 else d[col][x] for x in orden]
    fin = [v + max(d[col].max(), ref[col].max()) * 0.035 for v in fin]
    f1.add_scatter(y=orden, x=fin, mode="text", text=[n(v) for v in d[col]], textposition="middle right",
                   textfont=dict(size=15, color=INK), showlegend=False, hoverinfo="skip")
    if anio != 2023:
        f1.add_scatter(y=orden, x=ref[col], mode="markers", name="2023 (referencia)", marker=dict(symbol="diamond-open", size=13, color=INK, line_width=2),
                       hovertemplate="%{y} en 2023: %{x:.1f} " + unidad + "<extra></extra>")
    if col == "roi":
        f1.add_vline(x=LIBS[LIBS.anio == anio].mediana.iloc[0], line_dash="dash", line_color=MUTED,
                     annotation_text="mediana de las seis", annotation_position="top", annotation_font_color=MUTED)
    f1.update_yaxes(autorange="reversed", tickfont_size=15)
    f1.update_xaxes(title=unidad if unidad == "M€" else "€ de valor por € invertido", range=[0, max(d[col].max(), ref[col].max()) * 1.22])
    show(fig_base(f1, h=max(300, 62 * len(orden) + 80)), "g_barras")

# --- trayectorias
with b:
    titular("La BUS cae desde lo más alto mientras otras suben" if col == "roi" else f"Evolución de {corto.lower()} 2023-2025",
            "Cada línea es una biblioteca. Al final de cada línea, el valor de 2025.")
    f2 = go.Figure()
    otros = [x for x in sel_libs if x != "BUS"]
    TC = {"UZ": ORANGE, "UB": GREEN, "UGR": PURPLE, "UV": SKY, "UAH": RED}
    fins = []
    for bib in otros + (["BUS"] if "BUS" in sel_libs else []):
        d2 = LIBS[LIBS.biblioteca == bib].sort_values("anio")
        me = bib == "BUS"
        colr = BLUE if me else TC.get(bib, GREY)
        f2.add_scatter(x=d2.anio, y=d2[col], mode="lines+markers", name=bib, line=dict(width=5 if me else 2.5, color=colr),
                       marker=dict(size=10 if me else 7, color=colr), hovertemplate=bib + " %{x}: %{y:.1f} " + unidad + "<extra></extra>")
        fins.append([bib, float(d2[col].iloc[2]), colr, me])
        if me:
            f2.add_annotation(x=2023, y=float(d2[col].iloc[0]), text=n(d2[col].iloc[0]), showarrow=False, xanchor="right", xshift=-8,
                              font=dict(size=14, color=BLUE))
    rango = max(x[1] for x in fins) if fins else 1
    sep = rango * 0.065
    fins.sort(key=lambda x: x[1])
    pos = []
    for k_, f_ in enumerate(fins):
        pos.append(f_[1] if k_ == 0 else max(f_[1], pos[-1] + sep))
    for f_, yp in zip(fins, pos):
        f2.add_annotation(x=2025, y=yp, text=f"{f_[0]}  {n(f_[1])}", showarrow=False, xanchor="left", xshift=10,
                          font=dict(size=15 if f_[3] else 13, color=f_[2]))
    f2.update_xaxes(tickvals=YEARS, range=[2022.7, 2025.75])
    f2.update_yaxes(title=unidad if unidad == "M€" else "€ por € invertido", rangemode="tozero")
    show(fig_base(f2, h=max(300, 62 * len(orden) + 80), showlegend=False), "g_trayectorias")

a, b = st.columns(2)
with a:
    titular("Costes parecidos, valores muy distintos",
            f"Cada punto es una biblioteca en {anio}. Cuanto más arriba, más valor. Las líneas de puntos marcan un ROI constante.")
    d = LF[LF.anio == anio]
    xmax = LIBS.coste.max() * 1.15
    ymax = LIBS.valor_meur.max() * 1.12
    f3 = go.Figure()
    for k in (10, 25, 50, 100):
        ya = min(xmax * k, ymax)
        f3.add_scatter(x=[0, ya / k], y=[0, ya], mode="lines", line=dict(dash="dot", color=GREY, width=1.5), showlegend=False, hoverinfo="skip")
        f3.add_annotation(x=ya / k, y=ya, text=f"ROI {k}", showarrow=False, xanchor="right", yanchor="bottom", font=dict(color=MUTED, size=12))
    f3.add_scatter(x=d.coste, y=d.valor_meur, mode="markers+text", text=d.biblioteca, textposition="top center", textfont=dict(size=14, color=INK),
                   marker=dict(size=[20 if x == "BUS" else 14 for x in d.biblioteca], color=[BLUE if x == "BUS" else ORANGE for x in d.biblioteca],
                               line=dict(width=2, color="white")), showlegend=False,
                   hovertemplate="%{text}<br>Coste %{x:.1f} M€<br>Valor %{y:.1f} M€<extra></extra>")
    f3.update_xaxes(range=[0, xmax], title="Coste total (M€)")
    f3.update_yaxes(range=[0, ymax], title="Valor total (M€)")
    show(fig_base(f3, h=420), "g_dispersion")

with b:
    titular("Mapa de ROI y estabilidad", "Cuanto más oscuro el azul, mayor ROI. CV: variabilidad del ROI entre años (más alto, menos estable).")
    bench = []
    for bib, g in LIBS.groupby("biblioteca"):
        g = g.sort_values("anio")
        r = g.roi.tolist()
        bench.append({"Biblioteca": bib, "ROI 2023": r[0], "ROI 2024": r[1], "ROI 2025": r[2],
                      "Var. ROI (%)": (r[2] / r[0] - 1) * 100, "CV (%)": g.roi.std(ddof=0) / g.roi.mean() * 100,
                      "Var. valor (%)": (g.valor_meur.iloc[2] / g.valor_meur.iloc[0] - 1) * 100,
                      "Var. coste (%)": (g.coste.iloc[2] / g.coste.iloc[0] - 1) * 100})
    bench = pd.DataFrame(bench).sort_values("ROI 2025", ascending=False).set_index("Biblioteca")
    bench = bench.loc[[x for x in bench.index if x in sel_libs]]
    ROI_COLS = ["ROI 2023", "ROI 2024", "ROI 2025"]
    ROI_MAX = bench[ROI_COLS].max().max()
    st.dataframe(
        bench.style.format(precision=1, decimal=",").map(lambda v: f"background-color: rgba(0,114,178,{0.08 + 0.55 * v / ROI_MAX:.2f}); color: #1B1F27", subset=ROI_COLS),
        width="stretch", height=35 * (len(bench) + 1) + 3)

# ------------------------------------------------------------------ composición
st.header("Dónde se genera el valor de la BUS")
st.caption("Cinco bloques sobre catorce servicios. Los diez servicios restantes se agrupan en «Resto» porque ninguno supera el 1 % del total.")
a, b = st.columns(2)
with a:
    vista = st.segmented_control("Vista", ["M€", "% del total"], default="M€", key="vista") or "M€"
    titular(f"El repositorio pasa del {pct(b23['Repositorio institucional'] / b23.valor * 100, 0)} al {pct(b25['Repositorio institucional'] / b25.valor * 100, 0)} del valor",
            "Cada columna es un año. Los colores son los bloques de servicios.")
    f4 = go.Figure()
    for bl in bloques_sel:
        v = BUS[bl] if vista == "M€" else BUS[bl] / BUS.valor * 100
        f4.add_bar(x=[str(y) for y in YEARS], y=v, name=CORTO[bl], marker_color=BCOL[bl],
                   text=[(n(x, 0) if vista == "M€" else n(x, 0) + " %") if x >= (110 if vista == "M€" else 7) else "" for x in v],
                   textposition="inside", insidetextanchor="middle", textangle=0, textfont=dict(color=BTXT[bl], size=14),
                   hovertemplate=CORTO[bl] + ": %{y:.1f}" + (" M€" if vista == "M€" else " %") + "<extra></extra>")
    if vista == "M€":
        tot = BUS[bloques_sel].sum(axis=1)
        f4.add_scatter(x=[str(y) for y in YEARS], y=tot, mode="text", text=[n(x, 0) + " M€" for x in tot], textposition="top center",
                       textfont=dict(size=14, color=INK), showlegend=False, hoverinfo="skip")
    f4.update_yaxes(title="M€" if vista == "M€" else "% del valor total")
    f4.update_layout(legend_traceorder="normal")
    show(fig_base(f4, h=430, barmode="stack"), "g_comp")

with b:
    periodo = st.segmented_control("Periodo", ["2023 → 2025", "2024 → 2025"], default="2023 → 2025", key="per") or "2023 → 2025"
    y0 = 2023 if periodo.startswith("2023") else 2024
    d0, d1 = BUS.loc[y0], BUS.loc[2025]
    ETQ = {"Repositorio institucional": "Repo-<br>sitorio", "Descargas de artículos": "Artículos", "Libros electrónicos": "Libros<br>electrón.",
           "Libros prestados": "Libros<br>prestados", "Resto de servicios": "Resto"}
    nombres = [f"Valor<br>{y0}"] + [ETQ[k] for k in BLOQUES] + ["Valor<br>2025"]
    vals = [d0.valor] + [d1[k] - d0[k] for k in BLOQUES] + [d1.valor]
    share = (d0["Repositorio institucional"] - d1["Repositorio institucional"]) / (d0.valor - d1.valor) * 100
    titular(f"El valor cae {n(d0.valor - d1.valor, 0)} M€ y el repositorio explica el {pct(share, 0)}",
            "Cascada: parte del valor inicial, suma o resta lo que aporta cada bloque y llega al valor final.")
    f5 = go.Figure(go.Waterfall(x=nombres, y=vals, measure=["absolute"] + ["relative"] * 5 + ["total"],
                                text=[("" if i in (0, 6) else ("+" if v >= 0 else "-")) + n(abs(v), 0) for i, v in enumerate(vals)],
                                textposition="outside", textfont=dict(size=14, color=INK), cliponaxis=False,
                                decreasing=dict(marker=dict(color=RED)), increasing=dict(marker=dict(color=GREEN)),
                                totals=dict(marker=dict(color=BLUE)), connector=dict(line=dict(color=GREY, dash="dot"))))
    f5.update_yaxes(title="M€", range=[0, max(vals[0], vals[-1]) * 1.15])
    f5.update_xaxes(tickangle=0, tickfont_size=13)
    show(fig_base(f5, h=430), "g_puente")

# ------------------------------------------------------------------ sensibilidad
st.header("Sensibilidad del ROI")
st.caption("El indicador depende en gran medida de una descarga valorada al precio de un artículo. La gráfica recalcula el ROI de la BUS si ese servicio pesara menos o no existiera.")
a, b = st.columns([3, 2])
sel_esc = [(c_, nm) for c_, nm in ESC if nm in esc_sel]
with a:
    titular(f"Sin el repositorio, el ROI de {anio} sería {n(act.roi_sin_repo)} € y no {n(act.roi)} €",
            "Cada barra es un escenario. La línea roja marca el umbral de rentabilidad (ROI = 1: el servicio solo cubre su coste).")
    nombres_e = [nm for _, nm in sel_esc]
    vals_e = [act[c_] for c_, _ in sel_esc]
    f6 = go.Figure(go.Bar(y=nombres_e, x=vals_e, orientation="h", marker_color=[BLUE if nm == "ROI publicado" else SKY for nm in nombres_e],
                          text=[n(v, 1 if v >= 10 else 2) for v in vals_e], textposition="outside", cliponaxis=False,
                          hovertemplate="%{y}: %{x:.2f} €<extra></extra>"))
    f6.add_vline(x=1, line_color=RED, line_width=2, line_dash="dash")
    f6.update_yaxes(autorange="reversed", tickfont_size=14)
    f6.update_xaxes(title="€ de valor por € invertido", range=[0, max(vals_e) * 1.18])
    show(fig_base(f6, h=max(300, 58 * len(nombres_e) + 90)), "g_sens")
with b:
    titular("Evolución de cada escenario", "Escala logarítmica: cada marca vale diez veces la anterior, para ver a la vez valores pequeños y grandes.")
    f7 = go.Figure()
    EC = {"ROI publicado": BLUE, "Repositorio al 50 %": GREEN, "Repositorio al 25 %": ORANGE, "Repositorio al 10 %": PURPLE,
          "Sin repositorio": RED, "Sin descargas digitales": INK}
    for k, (c_, nm) in enumerate(sel_esc):
        colr = EC[nm]
        f7.add_scatter(x=YEARS, y=BUS[c_], mode="lines+markers", name=nm, line=dict(width=4 if k == 0 else 2.5, color=colr),
                       hovertemplate=nm + " %{x}: %{y:.2f} €<extra></extra>")
    f7.add_hline(y=1, line_dash="dash", line_color=RED)
    f7.update_yaxes(type="log", tickvals=[1, 2, 5, 10, 20, 50], ticktext=["1", "2", "5", "10", "20", "50"])
    f7.update_xaxes(tickvals=YEARS)
    show(fig_base(f7, h=max(300, 58 * len(nombres_e) + 90), legend=dict(orientation="h", y=-0.35, font_size=12)), "g_sens_log")
st.caption("Repositorio al 50 %, 25 % y 10 %: se conserva esa fracción de su valor. «Sin descargas digitales» excluye repositorio, artículos y libros electrónicos.")

# ------------------------------------------------------------------ actividad
st.header("Actividad estimada detrás del valor")
st.caption("Volumen = valor del servicio dividido entre su valor unitario consensuado. Es una estimación derivada, no una cifra publicada. En los gráficos pequeños, 100 es el nivel de 2023: por debajo, el servicio se usa menos; por encima, más.")
ACT = [("S.0.1", "Libros prestados"), ("S.0.5", "Descargas de artículos"), ("S.0.4", "Descargas de libros electrónicos"),
       ("S.0.6", "Descargas del repositorio"), ("S.12", "Horas de salas de estudio"), ("S.0.9", "Informes de calidad"),
       ("S.11", "Horas de formación de bibliotecarios"), ("S.13", "Uso de ordenadores")]
FAM = SERV.drop_duplicates("codigo").set_index("codigo").familia
ACT_F = [(c_, nm) for c_, nm in ACT if FAM[c_] in familias_sel]
if not ACT_F:
    st.info("Ningún servicio de esta selección tiene indicador de actividad estimada.")
cols = st.columns(4)
for k, (cod, nombre) in enumerate(ACT_F):
    g = SERV[SERV.codigo == cod].sort_values("anio")
    v25, var = g.volumen.iloc[-1], (g.volumen.iloc[-1] / g.volumen.iloc[0] - 1) * 100
    colr = RED if var < 0 else GREEN
    uni = SERV[SERV.codigo == cod].unidad.iloc[0]
    uni = "días de préstamo" if uni == "día de préstamo" else uni + "s"
    with cols[k % 4]:
        if True:
            st.metric(nombre, f"{n(v25 / 1e6, 2)} M" if v25 >= 1e6 else n(v25, 0), pct(var, 1, True).replace("−", "-") + " frente a 2023",
                      help=f"Estimación del volumen de 2025, en {uni}.")
            st.caption(f"{uni.capitalize()} estimados (2025)")
            fs = go.Figure(go.Scatter(x=g.anio, y=g.indice, mode="lines+markers+text", line=dict(color=colr, width=3), marker=dict(size=8, color=colr),
                                      text=["", "", f"{n(g.indice.iloc[-1], 0)}"], textposition="top center", textfont=dict(size=13, color=colr),
                                      hovertemplate="%{x}: índice %{y:.0f}<extra></extra>"))
            fs.add_hline(y=100, line_dash="dot", line_color=GREY)
            lo, hi = min(100, g.indice.min()), max(100, g.indice.max())
            fs.update_yaxes(visible=False, range=[lo - (hi - lo) * 0.15 - 1, hi + (hi - lo) * 0.3 + 1])
            fs.update_xaxes(tickvals=YEARS, tickfont_size=12)
            fs.update_layout(height=130, margin=dict(l=4, r=4, t=4, b=4), template="plotly_white", paper_bgcolor="white", plot_bgcolor="white",
                             font=dict(color=INK))
            show(fs, f"sp{cod}")

# ------------------------------------------------------------------ servicios
st.header("Los catorce servicios de la BUS")
st.caption("Valor en miles de euros. Pulsa una cabecera para ordenar.")
t = SERV.pivot_table(index=["codigo", "servicio", "familia"], columns="anio", values="valor_eur").reset_index()
t.columns = ["Cód.", "Servicio", "Familia", "2023 (k€)", "2024 (k€)", "2025 (k€)"]
for c_ in ("2023 (k€)", "2024 (k€)", "2025 (k€)"):
    t[c_] = (t[c_] / 1000).round(0)
t["var"] = (t["2025 (k€)"] / t["2023 (k€)"] - 1) * 100
t["Cuota 2025"] = t["2025 (k€)"] / t["2025 (k€)"].sum() * 100
t["Variación 2023-25"] = t["var"].map(lambda v: ("▲ +" if v >= 0 else "▼ -") + n(abs(v), 1) + " %")
t = t[t.Familia.isin(familias_sel)]
q = st.text_input("Buscar servicio")
if q:
    t = t[t.Servicio.str.contains(q, case=False) | t["Cód."].str.contains(q, case=False)]
st.dataframe(
    t.sort_values("2025 (k€)", ascending=False)[["Cód.", "Servicio", "Familia", "2023 (k€)", "2024 (k€)", "2025 (k€)", "Variación 2023-25", "Cuota 2025"]],
    width="stretch", hide_index=True, height=35 * (len(t) + 1) + 3,
    column_config={
        "2023 (k€)": st.column_config.NumberColumn(format="localized"), "2024 (k€)": st.column_config.NumberColumn(format="localized"),
        "2025 (k€)": st.column_config.NumberColumn(format="localized"),
        "Cuota 2025": st.column_config.ProgressColumn("Peso en 2025", format="%.1f %%", min_value=0, max_value=100),
    },
)

# ------------------------------------------------------------------ lectura
st.header("Lectura del indicador")
v = lambda cod, y: SERV[(SERV.codigo == cod) & (SERV.anio == y)].volumen.iloc[0]
ugr = LIBS[LIBS.biblioteca == "UGR"].set_index("anio")
uz = LIBS[LIBS.biblioteca == "UZ"].set_index("anio")
corr = LIBS.valor_meur.corr(LIBS.coste)
otros25 = b25["Resto de servicios"] / b25.valor * 100
st.markdown(f"""<div class="lectura">

1. **El deterioro procede del numerador.** Entre 2023 y 2025 el valor total cae un {pct(caida)} y el coste crece un {pct((b25.coste / b23.coste - 1) * 100)}. El personal sube un {pct((b25.personal / b23.personal - 1) * 100)} y los recursos de información un {pct((b25.recursos / b23.recursos - 1) * 100)}. El ROI publicado retrocede un {pct((1 - b25.roi / b23.roi) * 100)}.
2. **Un solo servicio concentra el resultado.** Las descargas del repositorio pasan del {pct(b23["Repositorio institucional"] / b23.valor * 100)} al {pct(b25["Repositorio institucional"] / b25.valor * 100)} del valor total y explican el {pct(repo_caida)} de la caída. El volumen estimado baja de {n(b23.desc_repo_m)} a {n(b25.desc_repo_m)} millones de descargas ({pct((b25.desc_repo_m / b23.desc_repo_m - 1) * 100, 1, True)}), valoradas al precio consensuado de una descarga de artículo.
3. **El núcleo del servicio se mantiene por encima del umbral.** Sin el repositorio, el ROI es de {n(b23.roi_sin_repo)} €, {n(b24.roi_sin_repo)} € y {n(b25.roi_sin_repo)} € en 2023, 2024 y 2025. Sin ninguna descarga digital queda en {n(b23.roi_sin_desc, 2)} €, {n(b24.roi_sin_desc, 2)} € y {n(b25.roi_sin_desc, 2)} €. Los demás servicios cubren el coste, con un margen estrecho.
4. **La comparación entre bibliotecas cambia el orden.** La BUS ocupa el puesto {int(b23.puesto)}.º en 2023 y el {int(b25.puesto)}.º en 2025. Su ROI pasa de {n(b23.ratio, 2)} a {n(b25.ratio, 2)} veces la media del resto. UGR registra una caída de {pct((1 - ugr.roi[2025] / ugr.roi[2024]) * 100)} solo en 2025, mientras UZ multiplica su valor por {n(uz.valor_meur[2025] / uz.valor_meur[2023])} con un coste casi estable ({pct((uz.coste[2025] / uz.coste[2023] - 1) * 100, 1, True)}). La correlación entre valor y coste en las dieciocho observaciones es de {n(corr, 2)}, de modo que el gasto explica poco del resultado.
5. **Los servicios de menor peso son los que crecen.** Las horas de salas aumentan un {pct((v("S.12", 2025) / v("S.12", 2023) - 1) * 100)} entre 2023 y 2025, los informes de calidad se multiplican por {n(v("S.0.9", 2025) / v("S.0.9", 2023))} y la formación de bibliotecarios crece un {pct((v("S.11", 2025) / v("S.11", 2023) - 1) * 100)}. El uso de ordenadores retrocede un {pct((1 - v("S.13", 2025) / v("S.13", 2023)) * 100)}. Los diez servicios restantes suman el {pct(otros25)} del valor de 2025.

</div>""", unsafe_allow_html=True)
st.info("Queda sin resolver si el valor unitario asignado a una descarga del repositorio es comparable entre las seis bibliotecas. "
        "Mientras no se fije ese criterio, el ranking mide en parte una diferencia de valoración y no solo una diferencia de impacto.")

with st.expander("Notas de método"):
    st.markdown("""
- Fuente: informe «ROI Bibliotecas Universitarias», Bibliotecas Líderes EFQM, publicado por la Biblioteca de la Universidad de Sevilla. Consulta del 20 de octubre de 2026.
- El informe ofrece el detalle por servicio solo para la BUS. Para las otras cinco bibliotecas se dispone de valor total, costes y ROI.
- El valor total de la BUS en 2023 se reconstruye como suma de sus servicios, porque el informe lo muestra redondeado. Los valores de UZ en 2024 y 2025 se publican redondeados a decenas de millones.
- El ROI de cada biblioteca es el publicado. Los escenarios de sensibilidad y los volúmenes estimados se calculan aquí a partir de los valores por servicio y sus valores unitarios.
- Las descargas de libros y artículos combinan datos COUNTER y no COUNTER, y las del repositorio proceden de datos propios. Esa heterogeneidad afecta a la comparabilidad de los volúmenes.
""")
