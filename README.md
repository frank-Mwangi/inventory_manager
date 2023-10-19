## inventory_manager

This is a nifty application that helps business owners track their inventory. 
Built entirely in django, the platform utilizes bootstrap for its frontend implementation alongside Chartjs for displaying charts. 

## Admin's view
On the dashboard, a superuser(admin) can view the total product count, staff count and orders count, as well as charts on orders and available products. 
Clicking on the staff tab shows a list of all available staff, and admin can click on either one of them to view their detailed profiles.
Clicking on products shows a tabular list of all products, their category and quantity. There is also a functional edit and delete button next to each product. Additionally, a form for adding new products.
Clicking on orders displays a tabular list of all orders, detailing the product, quantity ordered, staff serving the order, and the order time and date.

## staff's view
Naturally, a staff member will have a much more limited view upon logging in than a superuser. To that end, the dashboard shows a list of orders served by the staff member, as well as a nifty form for creating new order entries.

### The Backend
Django provides an intuitive admin panel which is accessible only by a superuser. From this panel, an admin can do all CRUD operations on products, users, and orders. Additionally, admin can add, modify or remove permissions for any user.
