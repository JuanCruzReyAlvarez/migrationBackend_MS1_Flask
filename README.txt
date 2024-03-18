The project entails the development of a microservice tailored to handle HTTPS JSON queries. Its primary function is to process incoming JSON requests, extract pertinent information, transform it as required, and store it in a database. This process involves the creation of new tables within the database to accommodate the migrated data.

The microservice operates within a RESTful architecture, leveraging Flask and Python for implementation. Flask, being a lightweight web framework, efficiently manages HTTP requests and responses, making it well-suited for building RESTful APIs. Python, renowned for its versatility and robustness, serves as the core programming language for executing the logic of the microservice, encompassing data extraction, transformation, and persistence tasks.

To ensure optimal performance and scalability in a production environment, the microservice will be deployed using Gunicorn. Gunicorn, a high-performance WSGI server, offers concurrency and load balancing capabilities, crucial for handling large volumes of incoming requests seamlessly.

Throughout the development and deployment phases, particular emphasis will be placed on security measures. This includes implementing SSL encryption for secure HTTPS communication and integrating authentication mechanisms to regulate access to sensitive endpoints. Additionally, comprehensive monitoring and logging functionalities will be incorporated to facilitate system health tracking and issue diagnosis.

In summary, the microservice architecture serves as a robust solution for facilitating data migration tasks. By adeptly processing JSON queries, performing necessary data transformations, and persisting the data in the database, it enables a smooth transition of data while maintaining high performance and scalability.



## WITHOUT DOCKER

    First, create a virtual environment:

        python -m virtualenv virtualMicroServ1

    To activate the environment:

        source virtualMicroServ1/bin/activate  // (In bash)

    To install necessary packages:

        pip install -r requirements.txt

    The system is set up for development with Flask. For production deployment, use Gunicorn, already installed.


## WITH DOCKER


    docker build -t backendflaskglobant . ## Creacion de Imagen

    docker run -p 5000:5000 backendflaskglobant