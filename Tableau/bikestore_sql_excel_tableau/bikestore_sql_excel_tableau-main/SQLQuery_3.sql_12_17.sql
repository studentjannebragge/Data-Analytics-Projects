SELECT
    ord.order_id,
    CONCAT(cus.first_name,' ',cus.last_name),
    cus.city,
    cus.state,
    ord.order_date,
    SUM(ite.quantity) AS 'total_units',
    SUM(ite.quantity * ite.list_price) AS 'revenue',
    pro.product_name
FROM sales.orders AS ord
JOIN sales.customers AS cus
ON ord.customer_id = cus.customer_id
JOIN sales.order_items AS ite
on ord.order_id = ite.order_id
JOIN production.products AS pro
ON ite.product_id = pro.product_id
GROUP BY
    ord.order_id,
    CONCAT(cus.first_name,' ',cus.last_name),
    cus.city,
    cus.state,
    ord.order_date, 
    pro.product_name
