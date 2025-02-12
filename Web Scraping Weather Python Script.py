import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=38.676334&lon=-76.805928')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find( id ="seven-day-forecast-body")

items = (week.find_all(class_ = 'tombstone-container'))

time_of = [item.find(class_ = 'period-name').get_text() for item in items]
forcast = [item.find(class_ = 'short-desc').get_text() for item in items]
temp = [item.find(class_ = 'temp').get_text() for item in items]

weather = pd.DataFrame(
    {
        'Time': time_of,
        'Forcast': forcast,
        'Temp': temp,
     }
)

weather.to_excel('Weather_forcast.xlsx')