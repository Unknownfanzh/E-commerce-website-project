# Django E-commerce Web Application
This is a simple e-commerce web application built using Django framework. The web application allows users to browse through various products, view product details and checkout by placing an order.

## Key aspects of the project
- **Django framework**: We used Django, a Python web framework, to build this e-commerce website. Django's Model-View-Template (MVT) architecture was used for the backend.

- **Models**: Two models, Products and Order, were defined to represent the data used in the website.

- **Views**: Three views, index, detail, and checkout, were defined to handle different HTTP requests from the frontend.

- **Templates**: HTML templates were used to render dynamic content on the frontend.

- **Forms**: Django forms were used to handle user input and data validation.

- **Paginator**: Django's built-in Paginator class was used to split a large number of products into smaller, more manageable pages.

- **Object-oriented programming**: use object-oriented programming principles to create classes for products and orders in our Django model. This allows us to organize the data and operations related to each class into a single unit, making it easier to manage and maintain the codebase.

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

## References
We relied on a number of online resources to learn Django and build this e-commerce website, including:

- Django's official documentation (https://docs.djangoproject.com/)
- Bootstrap 4.0 (https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- YouTube tutorials (e.g., Corey Schafer's Django series) (https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)
- Udemy Course (https://www.udemy.com/course/django-course/)