import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np


x = [i for i in range(1,16)]
y = [100, 20000, 300, 400, 500, 600, 700, 800, 900, 100, 200, 500, 700, 800]

def spc_limits(y):
    """
    Get the mean, standard deviation, upper control limit and lower control limit
    from a list.

    Parameters
    ----------
    y = list: list of y values
    
    Returns
    -------
    mean = float: arithmetic mean
    sd = float: standard deviation
    ucl = float: upper control limit
    lcl = float: lower control limit
    """
    mean = np.mean(y)
    sd = np.std(y, ddof=1) # using 1 assumes we are using sample data and not population.
    ucl = mean + sd*3
    lcl = mean - sd*3
    return mean, sd, ucl, lcl


def draw_scatter_plot(x, y, title="Interactive Plotly Graph", xaxis="x", yaxis="y"):
    mean, sd, ucl, lcl = spc_limits(y)

    fig = go.Figure(layout=dict(
        title=title,
        xaxis=dict(title=xaxis),
        yaxis=dict(title=yaxis)
        )
    )

    trace = go.Scatter(
            x=x, y=y,
            name='Trace',
            mode='lines+markers',
            line=dict(
                color="blue",
                width=2
                ),
            marker=dict(
                    color="blue",
                    size=8,
                    line=dict(
                        color="blue",
                        width=0.5
                        ),
                    ),
            text="y"
    )

    ucl_trace = go.Scatter(
            x=x, y=[ucl]*len(y),
            name='UCL',
            mode='lines',
            connectgaps=True,
            line=dict(
                    color="red",
                    width=3)
    )

    lcl_trace = go.Scatter(
            x=x, y=[lcl]*len(y),
            name='LCL',
            mode='lines',
            connectgaps=True,
            line=dict(
                    color="red",
                    width=3)
    )

    sd_trace = go.Scatter(
            x=x, y=[sd]*len(y),
            name='SD',
            mode='lines', # +text
            textposition='top right',
            connectgaps=True,
            #text="SD",
            line=dict(
                    color="yellow",
                    width=3,
                    dash='dash')
    )

    anomaly = []
    for i in y:
        if i >= ucl:
            anomaly.append(i)
        elif i <= lcl:
            anomaly.append(i)
        else:
            anomaly.append(None)

    anomaly_trace = go.Scatter(
            x=x, y=anomaly,
            name='Anomaly',
            mode='markers',
            opacity=0.5,
            line=dict(
                    color="red",
                    width=2),
            marker = dict(
                    color="red",
                    size=15,
                    line=dict(
                        color=None,
                        width=0.5),
                    ),
    )
            #text = "ANOMALY",
            #textposition='top center'

    mean_trace = go.Scatter(
            x=x, y=[mean]*len(y),
            name='MEAN',
            mode='lines',
            textposition='top right',
            connectgaps=True,
            #text="MEAN",
            line = dict(
                    color="orange",
                    width=3,
                    dash='dash'),
    )   

    data = [trace, ucl_trace, lcl_trace, sd_trace, anomaly_trace, mean_trace]
    for i in data:
        fig.add_trace(i)

    fig.add_annotation(x=x[-1], y=mean,
        text="MEAN",
        bgcolor="orange",
        showarrow=False,)

    fig.add_annotation(x=x[-1], y=sd,
        text="SD",
        bgcolor="yellow",
        showarrow=False,)
    
    fig.add_annotation(x=x[-1], y=ucl,
        text="UCL",
        bgcolor="red",
        showarrow=False,)

    fig.add_annotation(x=x[-1], y=lcl,
        text="LCL",
        bgcolor="red",
        showarrow=False,)

    fig.show()


draw_scatter_plot(x=x, y=y)




df = pd.DataFrame({
    "Task": ["Job A", "Job B", "Job C"],
    "Start": ['2009-01-01', '2008-12-05', '2009-02-20'],
    "Finish": ['2009-02-28', '2009-04-15', '2009-05-30']
})

fig = ff.create_gantt(df, colors='Viridis')
fig.show()