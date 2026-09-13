# Knowledge Repository for Retail Store Management System
print ("Prerana Arya_14601012023")
knowledge_repository = {
    "Products": {
        "P101": {
            "Name": "Laptop",
            "Price": 55000,
            "Stock": 10
        },
        "P102": {
            "Name": "Headphones",
            "Price": 2000,
            "Stock": 25
        },
        "P103": {
            "Name": "Keyboard",
            "Price": 1200,
            "Stock": 15
        }
    },
    "Customers": {
        "C101": {
            "Name": "Rahul",
            "Membership": "Gold"
        },
        "C102": {
            "Name": "Ananya",
            "Membership": "Regular"
        }
    },
    "Orders": {
        "O101": {
            "Customer": "C101",
            "Product": "Laptop",
            "Quantity": 1
        }
    },
    "Business Rules": {
        "Gold Customer": "10% discount",
        "Low Stock": "Restock product",
        "Out of Stock": "Product unavailable"
    }
}
print("----- RETAIL STORE KNOWLEDGE REPOSITORY -----")

print("\nProducts:")
for product_id, product in knowledge_repository["Products"].items():
    print(product_id, ":", product)
print("\nCustomers:")
for customer_id, customer in knowledge_repository["Customers"].items():
    print(customer_id, ":", customer)
print("\nOrders:")
for order_id, order in knowledge_repository["Orders"].items():
    print(order_id, ":", order)
print("\nBusiness Rules:")
for rule, action in knowledge_repository["Business Rules"].items():
    print(rule, "->", action)