# alx_travel_app_0x03

## Background Task Management with Celery and RabbitMQ

This project enhances the Django-based travel application by adding asynchronous
background processing using **Celery** with **RabbitMQ** as the message broker.

## Features

- Asynchronous booking confirmation emails
- Celery background task processing
- RabbitMQ as message broker
- Django email backend integration

## How It Works

When a booking is created, an email notification task is triggered using Celery.
The task runs in the background so the main request-response cycle is not blocked.

## Technologies Used

- Django
- Celery
- RabbitMQ
- Django Email Backend

## Running Celery Worker

```bash
celery -A alx_travel_app worker -l info
