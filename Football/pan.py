import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_html('https://en.wikipedia.org/wiki/List_of_chocolate_bar_brands')

print(df)
