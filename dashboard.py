import plotly.express as px

def create_chart(scores):

    fig = px.bar(
        x=list(scores.keys()),
        y=list(scores.values())
    )

    return fig