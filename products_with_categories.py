from pyspark.sql import DataFrame
from pyspark.sql.functions import explode, col, lit, size

def get_products_with_categories(products, categories, product_categories):
    prod_with_cat = products.join(product_categories, on='product_id', how='left')

    prod_with_cat = prod_with_cat.join(categories, on='category_id', how='left')

    result = prod_with_cat.select('product_name', 'category_name')

    return result

def get_products_with_categories2(
    products_df: DataFrame,
    categories_df: DataFrame
) -> DataFrame:
    exploded = products_df.filter(size(col("category_ids")) > 0) \
        .withColumn("category_id", explode(col("category_ids")))

    joined = exploded.join(
        categories_df.select("category_id", "category_name"),
        on="category_id",
        how="left"
    ).select(
        col("product_id"),
        col("product_name"),
        col("category_name")
    )

    no_categories = products_df.filter(size(col("category_ids")) == 0) \
        .select(
            col("product_id"),
            col("product_name"),
            lit(None).cast("string").alias("category_name")
        )

    return joined.unionByName(no_categories)