sales_and_product = sales.merge(
    product,
    on=["product_id"]
    )