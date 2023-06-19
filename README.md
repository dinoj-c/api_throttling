
# API Throttling System

This repository contains an implementation of a basic API throttling system built using Django, a popular Python web framework. The system allows for rate limiting and throttling of HTTP(S) requests based on the referrer, limiting the number of requests per second from a specific referrer.


### Features:

- Throttles requests from a specific referrer when the number of requests exceeds a configurable limit per second.
- Uses Django middleware to intercept requests and apply throttling logic.
- Stores request information in a database using Django's built-in ORM.


# Instructions to Run the Project:

* Clone the repository: `git clone https://github.com/dinoj-c/api_throttling.git`
* Install the required dependencies: `pip install -r requirements.txt`
* Configure the Django project settings: 
    * Adjust the throttling settings in the `THROTTLING_REQUEST_LIMIT` in variable `api_throttling/settings.py` if needed.
* Apply database migrations:
    * `python manage.py makemigrations`
    * `python manage.py migrate`
* Start the Django development server: `python manage.py runserver`

* Access the API endpoints and test the throttling functionality.
    * Example Endpoint:
        * `http://localhost:8000/`
        * `Method: GET`
    * Testing the Throttling Functionality:
        * Send multiple requests to the API endpoint within a short time frame, exceeding the throttling limit.
        * After the throttling limit is reached, subsequent requests from the same referrer will receive a 403 Forbidden response.
    * Monitoring the Throttling:
        * The throttling information is stored in the database.
        * You can inspect the `Throttle` model in `throttling/models.py` to access the stored information.
    * Customizing Throttling Rules:
        * You can customize the throttling rules by modifying the `THROTTLING_REQUEST_LIMIT` value in `api_throttling/settings.py`.




