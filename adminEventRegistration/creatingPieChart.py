from reg.models import Register
from django.db.models import Count
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import os
def createPie():
    res=Register.objects.values('regType').annotate(dcount=Count('regType'))
    # print(res)
    data=[]
    for item in res:
        data.append(item)
    df=pd.DataFrame(data)
    print(df)
    print(df['regType'])
    fig = px.pie(df, values='dcount', names='regType',
             title='Distribution of Registrations' )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    print(os.getcwd())
    fig.write_html('adminEventRegistration/embeddedHTML/pie.html')
    a=plot(fig,filename='adminEventRegistration/embeddedHTML/pie.html',output_type='div',image_width=400,image_height=300)
    return a