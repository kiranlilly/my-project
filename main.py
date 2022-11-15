import pandas as pd
import fastapi
import uvicorn
from fastapi.responses import HTMLResponse

app = fastapi.FastAPI()

@app.get("/")

def index():

    data = pd.read_csv(r"titanic_test.csv")

    data1 = data.loc[(data['pclass']==1) | (data['AGE']>=18)]
    data2 = data.loc[(data['pclass']==2) | (data['AGE']>=18)]
    data3 = data.loc[(data['pclass']==3) | (data['AGE']>=18)]

    data_f = pd.concat([data1, data2, data3])

    del data1
    del data2
    del data3

    data_f = data_f.groupby(['SEX', 'pclass'], as_index=False).agg({'FARE': 'mean', 'AGE':'mean'})
    data_f.rename(columns={'SEX': 'Gender', 'pclass': 'Class', 'FARE': 'Fare_Mean', 'AGE': 'Age_Mean'}, inplace=True)
    data_f['Gender'] = data_f['Gender'].apply(lambda x: 'M' if x=='male' else 'F')

    data_html = data_f.to_html()

    #text_file = open("index.html", "w")
    #text_file.write(data_html)
    #text_file.close()

    #print(data_f)

    return HTMLResponse(content=data_html, status_code=200)
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

