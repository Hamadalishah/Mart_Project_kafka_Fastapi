# Mart Project

## Overview
The Mart Project is a FastAPI-based application that provides a user management system with CRUD (Create, Read, Update, Delete) operations. The project uses Kafka for event messaging and SQLModel for database interaction.

## Features
- **User Registration:** Allows new users to register.
- **User Retrieval:** Fetches user information by user ID.
- **User Update:** Updates existing user details.
- **User Deletion:** Deletes a user from the database.
- **Kafka Integration:** Sends events to Kafka for user updates and deletions.

## Technologies Used
- FastAPI: For building the API.
- SQLModel: For database operations.
- AIOKafka: For Kafka integration.
- Python: The programming language used.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Hamadalishah/kafka_practice.git
   cd kafka_practice
