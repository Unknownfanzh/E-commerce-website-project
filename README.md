# Django E-commerce Web Application
This is a simple e-commerce web application built using Django framework. The web application allows users to browse through various products, view product details and checkout by placing an order.

## Features
- Browse products: Users can view all the available products on the home page.
- Search products: Users can search for a specific product by typing the name of the product in the search bar.
- View product details: Users can click on a product to view its details such as description, price, and discount (if available).
- Add products to cart: Users can add products to the cart by clicking the 'Add to Cart' button on the product detail page.
- Place order: Users can checkout by filling out a form that includes personal and shipping information. 

## Installation
To run this application on your local machine, follow these steps:

- Clone the repository to your local machine using Git.
Install the required packages using `pip install -r requirements.txt`
- Navigate to the project directory.
- Run the server using `python manage.py runserver`.
- Open your browser and navigate to http://localhost:8000/.

## Dependencies
- Django
- Pillow

## Folder Structure
- `shop`: This folder contains all the Django files and folders required for the application to run.
- `templates`: This folder contains all the HTML templates used in the application.
- `static`: This folder contains all the static files such as CSS, JS, and images used in the application.