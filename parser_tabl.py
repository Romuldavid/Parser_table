import requests
import pandas as pd

url = 'https://www.investing.com/equities/google-inc-c-balance-sheet'


header = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.4.3.268 (beta) Yowser/2.5 Safari/537.36', 'accept': '*/*'
}

r = requests.get(url, headers=header)

df = pd.read_html(r.text, match='Total\s+.*')[0]

df = df.rename(columns={'Period Ending:':'Name'})

res = df.loc[df['Name'].str.len() < 100]
# save to CSV
res.to_csv(r'result.csv', sep=',', index=False)
# save to Excel
#res.to_excel(r'result.xlsx', index=False)