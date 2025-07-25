from trending import gather_trending_products

print("AI Profit Suite Initialized.")

if __name__ == "__main__":
    products = gather_trending_products()
    if products:
        print("Top products to promote:")
        for product in products:
            print(product)
    else:
        print("No products retrieved.")
