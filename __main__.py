from app import MercadonaScrapper
import pandas as pd

res = MercadonaScrapper().get_products()

pd.DataFrame(
    [[p.title, p.link, p.price] for p in res],
    columns=['title', 'link', 'price']
).to_csv('result.csv')