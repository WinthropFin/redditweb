#%%
from psaw import PushshiftAPI
from tqdm import tqdm
import datetime
import time
n_days = 3
api = PushshiftAPI()
start_time = int(time.time()) - n_days*60*60*24
submissions = api.search_submissions(after=start_time,
                                            subreddit='wallstreetbets')

#%%
import pandas as pd
import reticker
df = pd.DataFrame(columns = ['time', 'title', 'link','Num_comments','author','score', 'ticker'])
i = 0                                     
for submission in tqdm(submissions):
    submitted_time = datetime.datetime.fromtimestamp(submission.created_utc).isoformat()
    ticker = reticker.TickerExtractor().extract(submission.title)
    df.loc[i] = [submitted_time,  submission.title, submission.permalink, submission.num_comments,submission.author, submission.score,ticker]
    # print(df.loc[i])
    i += 1
#%%
type(df)
df.to_csv('data.csv')
#%%
df = pd.read_csv('data.csv')
output =df.groupby('ticker').size().nlargest(10)

print(output)

# %%
newoutput = pd.DataFrame(output)
newoutput.to_html('templates/table.html')
import time
time.sleep(10)
#%%
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('table.html')
if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
# %%
