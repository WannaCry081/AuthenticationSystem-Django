# Authentication System [Django]

This project implements an authentication system Restful-API using Django and Django Rest Framework (DRF). It provides endpoints for user registration, login, and password reset with code verification using smtp. The authentication mechanism is based on JWT (JSON Web Tokens) for secure authentication.

## Features

- User Registration: Allows users to register with their email and password.
- User Login: Provides endpoints for user authentication using email and password.
- Password Reset: Allows users to request a password reset and verifies the reset code before updating the password.

## Authentication Workflow

1. **User Registration**: Users can register by providing their email and password.
2. **User Login**: Registered users can log in by providing their email and password. Upon successful login, the system issues JWT tokens.
3. **Password Reset Request**: Users can request a password reset by providing their email. The system sends a reset code to the user's email.
4. **Password Reset Verification**: Users verify the reset code sent to their email and provide a new password. The system updates the password upon successful verification.

## Endpoints

- `/api/v1/register/`: POST endpoint for user registration.
- `/api/v1/login/`: POST endpoint for user login to obtain JWT tokens.
- `/api/v1/reset-password/`: POST endpoint for password reset request.
- `/api/v1/reset-password/verify/`: POST endpoint for verifying password reset code and updating the password.
- `/api/v1/users/{id}/`: GET endpoint to retrieve authenticated user information by ID.
- `/api/v1/users/{id}/`: PUT endpoint to update authenticated user information by ID.
- `/api/v1/users/{id}/`: DELETE endpoint to delete authenticated user by ID.
- `/api/v1/users/me/`: GET endpoint to retrieve authenticated user's own information.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/WannaCry081/AuthenticationSystem-Django.git
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root directory of your project and add the following environment variables:

    ```
    DJANGO_ENV="development"
    DJANGO_SECRET_KEY=your_secret_key_here
    DJANGO_EMAIL_HOST_USER=your_email_host_user_here
    DJANGO_EMAIL_HOST_PASSWORD=your_email_host_password_here
    ```

3. **Start the development server:**

    ```bash
    ./run.sh
    ```

> [!NOTE]
>
> This authentication system is hard-coded and does not rely on the `djoser` package. It provides a basic implementation of authentication using Django and DRF with JWT tokens.
