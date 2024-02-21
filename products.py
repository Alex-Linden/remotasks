# import requests

# def get_products(api_url, category=None):
#     # Send the request and get the response
#     response = requests.get(api_url)

#     # If we get a valid response, parse the content and fetch the products
#     # into a JSON list
#     products = response.json()['products']

#     # If the results are not paginated, iterate over it and print results
#     if 'next' not in response.links:
#         for product in products:
#             # Print only products in the specified category
#             if category is None or product['category'] == category:
#                 print(f"{product['title']} in {product['category']}")

#     # If the results are paginated, fetch all the pages before iterating
#     else:
#         while True:
#             for product in products:
#                 # Print only products in the specified category
#                 if category is None or product['category'] == category:
#                     print(f"{product['title']} in {product['category']}")
#             if 'next' in response.links:
#                 response = requests.get(response.links['next']['url'])
#                 products = response.json()['products']
#             else:
#                 break

# import requests

# def get_products(api_url, category=None):
#     response = requests.get(api_url)
#     # print(response)
#     try:
#         products = response.json()['products']
#     except:
#         print("No products found.")
#         return []
#     # print(products)
#     print(response.links)
#     if 'next' not in response.links:
#         print("next not in response.links")
#         return [product for product in products if category is None or product['category'] == category]
#     else:
#         while True:
#             for product in products:
#                 yield product
#             if 'next' in response.links:
#                 response = requests.get(response.links['next']['url'])
#                 products = response.json()['products']
#             else:
#                 break

import requests

def get_products(api_url, category=None):
    # Send the request and get the response
    try:
        response = requests.get(api_url)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}", file=sys.stderr)
        return []

    # If we get a valid response, parse the content and fetch the products
    # into a JSON list
    if response.status_code == 200:
        products = response.json().get('products', [])
    else:
        print(f"HTTP error: {response.status_code}", file=sys.stderr)
        return []

    # Filter the products based on the category
    if category is not None:
        products = [product for product in products if product['category'] == category]

    return products

products = get_products('https://dummyjson.com/products')
products2 = get_products('https://dummyjson.com/products', 'smartphones')
products3 = get_products('ttps://dummyjson.com/pro', 'smartphones')
print(products)
print(products2)
print(products3)

for product in products:
    print("1")
    print(f"{product['title']} in {product['category']}")

# get_products('https://dummyjson.com/products')
# get_products('https://dummyjson.com/products', 'smartphones')


    # randome changehghkasdjlfhasjkldfh a
    #only testing git
    #testing git again


    #testing git again