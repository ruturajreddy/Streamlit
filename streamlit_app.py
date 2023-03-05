import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime
import altair as alt

from vega_datasets import data

st.header('Practice Streamlit')


# df = pd.DataFrame({
#     'first column' : [1, 2, 3, 4],
#     'second column' : [10, 20, 30, 40]
# })

# st.write(df)

# df = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns = ['a', 'b', 'c']
# )
# st.write(df)
# c = alt.Chart(df).mark_circle().encode(
#     x = 'a', y = 'b', size='a', color='c', tooltip=['a', 'b', 'c']
# )
# st.write(c)

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# st.area_chart(chart_data)

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)

# # We use @st.cache_data to keep the dataset in cache
# @st.cache_data
# def get_data():
#     source = data.stocks()
#     source = source[source.date.gt("2004-01-01")]
#     return source

# source = get_data()


# # Define the base time-series chart.
# def get_chart(data):
#     hover = alt.selection_single(
#         fields=["date"],
#         nearest=True,
#         on="mouseover",
#         empty="none",
#     )

#     lines = (
#         alt.Chart(data, title="Evolution of stock prices")
#         .mark_line()
#         .encode(
#             x="date",
#             y="price",
#             color="symbol",
#         )
#     )

#     # Draw points on the line, and highlight based on selection
#     points = lines.transform_filter(hover).mark_circle(size=65)

#     # Draw a rule at the location of the selection
#     tooltips = (
#         alt.Chart(data)
#         .mark_rule()
#         .encode(
#             x="yearmonthdate(date)",
#             y="price",
#             opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
#             tooltip=[
#                 alt.Tooltip("date", title="Date"),
#                 alt.Tooltip("price", title="Price (USD)"),
#             ],
#         )
#         .add_selection(hover)
#     )
#     return (lines + points + tooltips).interactive()

# chart = get_chart(source)

# # Add annotations
# ANNOTATIONS = [
#     ("Mar 01, 2008", "Pretty good day for GOOG"),
#     ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
#     ("Nov 01, 2008", "Market starts again thanks to..."),
#     ("Dec 01, 2009", "Small crash for GOOG after..."),
# ]
# annotations_df = pd.DataFrame(ANNOTATIONS, columns=["date", "event"])
# annotations_df.date = pd.to_datetime(annotations_df.date)
# annotations_df["y"] = 10

# annotation_layer = (
#     alt.Chart(annotations_df)
#     .mark_text(size=20, text="⬇", dx=-8, dy=-10, align="left")
#     .encode(
#         x="date:T",
#         y=alt.Y("y:Q"),
#         tooltip=["event"],
#     )
#     .interactive()
# )

# st.altair_chart(
#     (chart + annotation_layer).interactive(),
#     use_container_width=True
# )