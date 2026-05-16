import plotly.express as px
from utils import capitalize_words

px.defaults.template = "seaborn"

def my_bar_chart(data, x, y, title=None, x_title=None, y_title=None, top=True):
    fig = px.bar(
        data_frame=data,
        x=x, 
        y=y,
        text=y
    )

    if top:
        fig.update_traces(textposition="outside")

    fig.update_layout(
        title=capitalize_words(title),
        xaxis_title=capitalize_words(x_title),
        yaxis_title=capitalize_words(y_title),
    )
    return fig

def my_line_chart(data, x, y, title=None, x_title=None, y_title=None, markers=False):
    fig = px.line(
        data_frame=data,
        x=x,
        y=y,
        markers=markers
    )
    
    fig.update_layout(
        title=capitalize_words(title),
        xaxis_title=capitalize_words(x_title),
        yaxis_title=capitalize_words(y_title),
    )
    
    fig.update_yaxes(rangemode="tozero")
    return fig

