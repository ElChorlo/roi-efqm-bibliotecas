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
COL = ["#2f6fdb", "#e08a1e", "#2a9d8f", "#9b5de5", "#8d99ae", "#d1495b"]
BLOQUES = ["Repositorio institucional", "Descargas de artículos", "Libros electrónicos", "Libros prestados", "Resto de servicios"]
BCOL = dict(zip(BLOQUES, COL))
EJE = dict(gridcolor="rgba(128,128,128,.25)", zerolinecolor="rgba(128,128,128,.35)")


def n(v, d=1):
    return f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(v, d=1, signo=False):
    s = n(abs(v), d) + " %"
    return (("+" if v > 0 else "−" if v < 0 else "") + s) if signo else s


def fig_base(fig, h=380, **kw):
    fig.update_layout(height=h, margin=dict(l=10, r=10, t=30, b=10), legend=dict(orientation="h", y=-0.15),
                      xaxis=EJE, yaxis=EJE, **kw)
    return fig


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

anio = st.segmented_control("Año", YEARS, default=2025, key="anio") or 2025
i = YEARS.index(anio)
act, prev = BUS.loc[anio], (BUS.loc[YEARS[i - 1]] if i else None)


def delta(campo, inv=False):
    if prev is None:
        return None
    return pct((act[campo] / prev[campo] - 1) * 100, 1, True).replace("−", "-")


# ------------------------------------------------------------------ resumen
st.header("Resumen de la BUS")
st.caption("El ROI es el valor generado por los servicios dividido entre el coste del personal y el gasto en recursos de información.")
c = st.columns(5)
c[0].metric("ROI publicado (€ por €)", n(act.roi), delta("roi"))
c[1].metric("Valor total (M€)", n(act.valor), delta("valor"))
c[2].metric("Coste total (M€)", n(act.coste), delta("coste"), delta_color="inverse")
c[3].metric("ROI sin repositorio", n(act.roi_sin_repo), delta("roi_sin_repo"))
c[4].metric("Puesto entre seis bibliotecas", f"{int(act.puesto)}.º", f"{n(act.ratio, 2)}× la media del resto", delta_color="off", delta_arrow="off")

# ------------------------------------------------------------------ benchmarking
st.header("Benchmarking con las otras cinco bibliotecas")
st.caption("El coste anual de cada biblioteca se mueve en un rango estrecho. El valor generado varía varias veces más, y con él el ROI.")
a, b = st.columns(2)

orden = LIBS[LIBS.anio == anio].sort_values("roi", ascending=False).biblioteca.tolist()
f1 = go.Figure()
for k, y in enumerate(YEARS):
    d = LIBS[LIBS.anio == y].set_index("biblioteca").loc[orden]
    f1.add_bar(x=orden, y=d.roi, name=str(y), marker_color=COL[k], opacity=1 if y == anio else 0.35,
               text=[n(v) if y == anio else "" for v in d.roi], textposition="outside",
               hovertemplate="%{x} · " + str(y) + "<br>ROI %{y:.1f} €<extra></extra>")
f1.add_hline(y=LIBS[LIBS.anio == anio].mediana.iloc[0], line_dash="dash", annotation_text="mediana")
a.subheader("ROI por biblioteca")
a.plotly_chart(fig_base(f1, barmode="group"), width="stretch")

f2 = go.Figure()
for bib in LIBS.biblioteca.unique():
    d = LIBS[LIBS.biblioteca == bib]
    me = bib == "BUS"
    f2.add_scatter(x=d.anio, y=d.roi, mode="lines+markers+text", name=bib, line=dict(width=4 if me else 2, color=COL[0] if me else None),
                   text=["", "", bib], textposition="middle right", hovertemplate=bib + " %{x}: %{y:.1f} €<extra></extra>")
f2.update_xaxes(tickvals=YEARS)
b.subheader("Trayectorias 2023-2025")
b.plotly_chart(fig_base(f2, showlegend=False), width="stretch")

a, b = st.columns(2)
d = LIBS[LIBS.anio == anio]
f3 = go.Figure()
xmax = LIBS.coste.max() * 1.1
for k in (10, 25, 50, 100):
    f3.add_scatter(x=[0, xmax], y=[0, xmax * k], mode="lines", line=dict(dash="dot", color="gray", width=1), showlegend=False,
                   hoverinfo="skip")
    ya = min(xmax * k, LIBS.valor_meur.max() * 1.1)
    f3.add_annotation(x=ya / k, y=ya, text=f"ROI {k}", showarrow=False, xanchor="right", yanchor="bottom", font=dict(color="gray", size=10))
f3.add_scatter(x=d.coste, y=d.valor_meur, mode="markers+text", text=d.biblioteca, textposition="middle right",
               marker=dict(size=[16 if x == "BUS" else 11 for x in d.biblioteca], color=[COL[0] if x == "BUS" else COL[1] for x in d.biblioteca]),
               hovertemplate="%{text}<br>Coste %{x:.1f} M€<br>Valor %{y:.1f} M€<extra></extra>", showlegend=False)
f3.update_xaxes(range=[0, xmax], title="Coste total (M€)")
f3.update_yaxes(range=[0, LIBS.valor_meur.max() * 1.1], title="Valor total (M€)")
a.subheader("Coste frente a valor")
a.caption("Año seleccionado. Las líneas discontinuas marcan ROI constante.")
a.plotly_chart(fig_base(f3), width="stretch")

bench = []
for bib, g in LIBS.groupby("biblioteca"):
    g = g.sort_values("anio")
    r = g.roi.tolist()
    bench.append({"Biblioteca": bib, "ROI 2023": r[0], "ROI 2024": r[1], "ROI 2025": r[2],
                  "Var. ROI (%)": (r[2] / r[0] - 1) * 100, "CV (%)": g.roi.std(ddof=0) / g.roi.mean() * 100,
                  "Var. valor (%)": (g.valor_meur.iloc[2] / g.valor_meur.iloc[0] - 1) * 100,
                  "Var. coste (%)": (g.coste.iloc[2] / g.coste.iloc[0] - 1) * 100})
bench = pd.DataFrame(bench).sort_values("ROI 2025", ascending=False).set_index("Biblioteca")
b.subheader("Mapa de ROI y estabilidad")
b.caption("CV: coeficiente de variación del ROI en los tres años. Las variaciones comparan 2025 con 2023.")
b.dataframe(bench.style.format("{:.1f}").background_gradient(subset=["ROI 2023", "ROI 2024", "ROI 2025"], cmap="Blues"),
            width="stretch")

# ------------------------------------------------------------------ composición
st.header("Dónde se genera el valor de la BUS")
st.caption("Cinco bloques sobre catorce servicios. Los diez servicios restantes se agrupan porque ninguno supera el 1 % del total.")
a, b = st.columns(2)
vista = a.segmented_control("Vista", ["M€", "% del total"], default="M€", key="vista") or "M€"
f4 = go.Figure()
for bl in BLOQUES:
    v = BUS[bl] if vista == "M€" else BUS[bl] / BUS.valor * 100
    f4.add_bar(x=[str(y) for y in YEARS], y=v, name=bl, marker_color=BCOL[bl],
               hovertemplate=bl + "<br>%{y:.1f}<extra></extra>")
a.subheader("Composición del valor por año")
a.plotly_chart(fig_base(f4, barmode="stack"), width="stretch")

periodo = b.segmented_control("Periodo", ["2023 → 2025", "2024 → 2025"], default="2023 → 2025", key="per") or "2023 → 2025"
y0 = 2023 if periodo.startswith("2023") else 2024
d0, d1 = BUS.loc[y0], BUS.loc[2025]
nombres = [f"Valor {y0}"] + ["Repositorio", "Artículos", "Libros electrónicos", "Libros prestados", "Resto"] + ["Valor 2025"]
vals = [d0.valor] + [d1[k] - d0[k] for k in BLOQUES] + [d1.valor]
f5 = go.Figure(go.Waterfall(x=nombres, y=vals, measure=["absolute"] + ["relative"] * 5 + ["total"],
                            text=[n(v) for v in vals], textposition="outside",
                            decreasing=dict(marker=dict(color="#d1495b")), increasing=dict(marker=dict(color=COL[2])),
                            totals=dict(marker=dict(color=COL[0]))))
b.subheader("De dónde viene la caída")
b.caption("Contribución de cada bloque a la variación del valor total (M€).")
b.plotly_chart(fig_base(f5), width="stretch")

# ------------------------------------------------------------------ sensibilidad
st.header("Sensibilidad del ROI")
st.caption("El indicador depende en gran medida de una descarga valorada al precio de un artículo. La gráfica recalcula el ROI de la BUS si ese servicio pesara menos o no existiera. Escala logarítmica.")
esc = [("roi", "ROI publicado"), ("roi_repo50", "Repositorio al 50 %"), ("roi_repo25", "Repositorio al 25 %"),
       ("roi_repo10", "Repositorio al 10 %"), ("roi_sin_repo", "Sin repositorio"), ("roi_sin_desc", "Sin descargas digitales")]
f6 = go.Figure()
for k, (campo, nombre) in enumerate(esc):
    f6.add_scatter(x=YEARS, y=BUS[campo], mode="lines+markers", name=nombre, line=dict(width=4 if k == 0 else 2, color=COL[k % 6]),
                   hovertemplate=nombre + " %{x}: %{y:.2f} €<extra></extra>")
f6.add_hline(y=1, line_dash="dash", line_color="#d1495b", annotation_text="umbral de rentabilidad (ROI = 1)")
f6.update_yaxes(type="log")
f6.update_xaxes(tickvals=YEARS)
st.plotly_chart(fig_base(f6, h=420), width="stretch")
st.caption("Repositorio al 50 %, 25 % y 10 %: se conserva esa fracción de su valor. «Sin descargas digitales» excluye repositorio, artículos y libros electrónicos.")

# ------------------------------------------------------------------ actividad
st.header("Actividad estimada detrás del valor")
st.caption("Volumen = valor del servicio dividido entre su valor unitario consensuado. Es una estimación derivada, no una cifra publicada. Índice 2023 = 100.")
ACT = [("S.0.1", "Libros prestados"), ("S.0.5", "Descargas de artículos"), ("S.0.4", "Descargas de libros electrónicos"),
       ("S.0.6", "Descargas del repositorio"), ("S.12", "Horas de salas de estudio"), ("S.0.9", "Informes de calidad"),
       ("S.11", "Horas de formación de bibliotecarios"), ("S.13", "Uso de ordenadores")]
cols = st.columns(4)
for k, (cod, nombre) in enumerate(ACT):
    g = SERV[SERV.codigo == cod].sort_values("anio")
    v25, var = g.volumen.iloc[-1], (g.volumen.iloc[-1] / g.volumen.iloc[0] - 1) * 100
    with cols[k % 4]:
        st.metric(nombre, f"{n(v25 / 1e6, 2)} M" if v25 >= 1e6 else n(v25, 0), pct(var, 1, True).replace("−", "-") + " frente a 2023")
        fs = go.Figure(go.Scatter(x=g.anio, y=g.indice, mode="lines+markers", line=dict(color="#d1495b" if var < 0 else COL[2], width=2),
                                  hovertemplate="%{x}: índice %{y:.0f}<extra></extra>"))
        fs.add_hline(y=100, line_dash="dot", line_color="gray")
        fs.update_layout(height=110, margin=dict(l=0, r=0, t=0, b=0), xaxis=dict(tickvals=YEARS, visible=True), yaxis=dict(visible=False))
        st.plotly_chart(fs, width="stretch", key=f"sp{cod}")

# ------------------------------------------------------------------ servicios
st.header("Los catorce servicios de la BUS")
t = SERV.pivot_table(index=["codigo", "servicio"], columns="anio", values="valor_eur").reset_index()
t.columns = ["Cód.", "Servicio", "2023 (k€)", "2024 (k€)", "2025 (k€)"]
for col in ("2023 (k€)", "2024 (k€)", "2025 (k€)"):
    t[col] = t[col] / 1000
t["Var. 23-25 (%)"] = (t["2025 (k€)"] / t["2023 (k€)"] - 1) * 100
t["Cuota 2025 (%)"] = t["2025 (k€)"] / t["2025 (k€)"].sum() * 100
q = st.text_input("Buscar servicio")
if q:
    t = t[t.Servicio.str.contains(q, case=False) | t["Cód."].str.contains(q, case=False)]
st.dataframe(t.sort_values("2025 (k€)", ascending=False).style.format(
    {"2023 (k€)": "{:,.1f}", "2024 (k€)": "{:,.1f}", "2025 (k€)": "{:,.1f}", "Var. 23-25 (%)": "{:+.1f}", "Cuota 2025 (%)": "{:.1f}"}),
    width="stretch", hide_index=True)

# ------------------------------------------------------------------ lectura
st.header("Lectura del indicador")
v = lambda cod, y: SERV[(SERV.codigo == cod) & (SERV.anio == y)].volumen.iloc[0]
ugr = LIBS[LIBS.biblioteca == "UGR"].set_index("anio")
uz = LIBS[LIBS.biblioteca == "UZ"].set_index("anio")
corr = LIBS.valor_meur.corr(LIBS.coste)
otros25 = b25["Resto de servicios"] / b25.valor * 100
st.markdown(f"""
1. **El deterioro procede del numerador.** Entre 2023 y 2025 el valor total cae un {pct(caida)} y el coste crece un {pct((b25.coste / b23.coste - 1) * 100)}. El personal sube un {pct((b25.personal / b23.personal - 1) * 100)} y los recursos de información un {pct((b25.recursos / b23.recursos - 1) * 100)}. El ROI publicado retrocede un {pct((1 - b25.roi / b23.roi) * 100)}.
2. **Un solo servicio concentra el resultado.** Las descargas del repositorio pasan del {pct(b23["Repositorio institucional"] / b23.valor * 100)} al {pct(b25["Repositorio institucional"] / b25.valor * 100)} del valor total y explican el {pct(repo_caida)} de la caída. El volumen estimado baja de {n(b23.desc_repo_m)} a {n(b25.desc_repo_m)} millones de descargas ({pct((b25.desc_repo_m / b23.desc_repo_m - 1) * 100, 1, True)}), valoradas al precio consensuado de una descarga de artículo.
3. **El núcleo del servicio se mantiene por encima del umbral.** Sin el repositorio, el ROI es de {n(b23.roi_sin_repo)} €, {n(b24.roi_sin_repo)} € y {n(b25.roi_sin_repo)} € en 2023, 2024 y 2025. Sin ninguna descarga digital queda en {n(b23.roi_sin_desc, 2)} €, {n(b24.roi_sin_desc, 2)} € y {n(b25.roi_sin_desc, 2)} €. Los demás servicios cubren el coste, con un margen estrecho.
4. **La comparación entre bibliotecas cambia el orden.** La BUS ocupa el puesto {int(b23.puesto)}.º en 2023 y el {int(b25.puesto)}.º en 2025. Su ROI pasa de {n(b23.ratio, 2)} a {n(b25.ratio, 2)} veces la media del resto. UGR registra una caída de {pct((1 - ugr.roi[2025] / ugr.roi[2024]) * 100)} solo en 2025, mientras UZ multiplica su valor por {n(uz.valor_meur[2025] / uz.valor_meur[2023])} con un coste casi estable ({pct((uz.coste[2025] / uz.coste[2023] - 1) * 100, 1, True)}). La correlación entre valor y coste en las dieciocho observaciones es de {n(corr, 2)}, de modo que el gasto explica poco del resultado.
5. **Los servicios de menor peso son los que crecen.** Las horas de salas aumentan un {pct((v("S.12", 2025) / v("S.12", 2023) - 1) * 100)} entre 2023 y 2025, los informes de calidad se multiplican por {n(v("S.0.9", 2025) / v("S.0.9", 2023))} y la formación de bibliotecarios crece un {pct((v("S.11", 2025) / v("S.11", 2023) - 1) * 100)}. El uso de ordenadores retrocede un {pct((1 - v("S.13", 2025) / v("S.13", 2023)) * 100)}. Los diez servicios restantes suman el {pct(otros25)} del valor de 2025.
""")
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
