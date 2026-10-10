SELECT sales.order_id, sales.product_name, customers.customer_name, customers.segment
FROM sales
LEFT JOIN customers
ON sales.customer_id = customers.customer_id
LIMIT 10;
