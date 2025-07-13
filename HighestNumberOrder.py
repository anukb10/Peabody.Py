from collections import defaultdict

def get_nth_highest_customer_orders(orders_data, n):
    """
    Finds the nth highest number of orders placed by a single customer.

    Args:
        orders_data (list of dict): A list where each dictionary represents an order
                                    and contains a 'customer_id' key.
        n (int): The 'n' for the nth highest number of orders.

    Returns:
        int or None: The nth highest number of orders, or None if n is out of range.
    """

    customer_order_counts = defaultdict(int)

    # Count orders for each customer
    for order in orders_data:
        customer_id = order['customer_id']
        customer_order_counts[customer_id] += 1

    # Get a list of order counts
    order_counts = list(customer_order_counts.values())

    # Sort the order counts in descending order
    order_counts.sort(reverse=True)

    # Check if n is a valid index
    if 1 <= n <= len(order_counts):
        return order_counts[n - 1]
    else:
        return None  # n is out of range

# Example Usage:
orders = [
    {'order_id': 1, 'customer_id': 'A'},
    {'order_id': 2, 'customer_id': 'B'},
    {'order_id': 3, 'customer_id': 'A'},
    {'order_id': 4, 'customer_id': 'C'},
    {'order_id': 5, 'customer_id': 'A'},
    {'order_id': 6, 'customer_id': 'B'},
    {'order_id': 7, 'customer_id': 'D'},
    {'order_id': 8, 'customer_id': 'D'},
]

# Find the 2nd highest number of orders
nth_highest = get_nth_highest_customer_orders(orders, 2)
print(f"The 2nd highest number of orders is: {nth_highest}")

# Find the 1st highest number of orders
nth_highest = get_nth_highest_customer_orders(orders, 1)
print(f"The 1st highest number of orders is: {nth_highest}")

# Find the 5th highest number of orders (might be out of range)
nth_highest = get_nth_highest_customer_orders(orders, 5)
print(f"The 5th highest number of orders is: {nth_highest}")