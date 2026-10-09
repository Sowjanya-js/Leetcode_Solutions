import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    product_filter=(products['low_fats']=='Y') & (products['recyclable']=='Y')
    return products.loc[product_filter,['product_id']]