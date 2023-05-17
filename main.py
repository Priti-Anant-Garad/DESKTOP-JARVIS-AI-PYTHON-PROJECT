import pandas as pd
from datetime import timedelta
import plotly
import plotly.express as px

def showganttchart():

    data = pd.read_excel('tasks.xlsx')
    print(data)

    # Convert data str to "datetime" data type, YYYY_MM_DD
    data["START DATE"] = pd.to_datetime(data["START DATE"], format="%Y_%m_%d")
    data["END DATE"] = pd.to_datetime(data["END DATE"], format="%Y_%m_%d")

    # sort tasks by start date
    data.sort_values("START DATE", axis=0, ascending=True, inplace=True)

    # add duration column
    data["DURATION"] = data["END DATE"] - data["START DATE"] + timedelta(days=1)
    # add colunm : start date of each task wrt the project day 1
    data["PastTime"] = data["START DATE"] - data["START DATE"][0]
    print(data)
    fig = px.timeline(data, x_start="START DATE", x_end="END DATE", y="Task", title="Gantt Chart For IOT Based Weather Forecast Station Project")
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(title_font_size=32, font_size=18, title_font_family="Arial")
    plotly.offline.plot(fig, filename="Gantt_Chart_For_Project.html")



