import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())


source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(source)

ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

click_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(click_by_source)

clicks_pivot = click_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
print(clicks_pivot)

clicks_pivot["percent_clicked"] = (clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])) * 100
print(clicks_pivot)

users = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
print(users)

users_clicks = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index()
#print(users_clicks)
users_clicks_pivot = users_clicks.pivot(
  columns = 'is_click',
  index ='experimental_group',
  values = 'user_id'
).reset_index()
#print(users_clicks_pivot)
users_clicks_pivot['percent_clicked'] = (users_clicks_pivot[True]/users_clicks_pivot[True] + users_clicks_pivot[False]) * 100
print(users_clicks_pivot)

a_clicks = ad_clicks.loc[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks.loc[ad_clicks.experimental_group == 'B']
print(a_clicks)
print(b_clicks)

a_clicks_user = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
#print(a_clicks_user)
a_clicks_percent = a_clicks_user.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
#print(a_clicks_percent)
a_clicks_percent["percent_clicked"] = (a_clicks_percent[True]/a_clicks_percent[True] + a_clicks_percent[False]) * 100
print(a_clicks_percent)

b_clicks_user = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
#print(b_clicks_user)
b_clicks_percent = b_clicks_user.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
#print(b_clicks_percent)
b_clicks_percent["percent_clicked"] = (b_clicks_percent[True]/b_clicks_percent[True] + b_clicks_percent[False]) * 100
print(b_clicks_percent)

#based on my analysis i would recommend Ad B.