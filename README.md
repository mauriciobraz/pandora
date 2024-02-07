# Pandora

A RAG bot efficiently updates its knowledge base with new documents through an API. It processes submissions to improve the accuracy of its responses, remaining up-to-date and valuable.

## Prerequisites

Before initiating the deployment, confirm the installation of the following essential tools:

-   [htpasswd](https://httpd.apache.org/docs/current/programs/htpasswd.html)
-   [Poetry](https://python-poetry.org/)
-   [Docker](https://www.docker.com/)
-   [Docker Compose](https://docs.docker.com/compose/)

## Deployment

TODO

## API Documentation

### Authentication

Most endpoints require authentication, which is handled using JWT (JSON Web Tokens). Our authentication system is powered by [FastAPI Users](https://github.com/fastapi-users/fastapi-users), a highly customizable and secure user management library for FastAPI. To access restricted endpoints, make sure to obtain your `access_token` through the login endpoint and include it as a bearer token in the `Authorization` header of your subsequent requests.

<details>
  <summary>
    Routes
  </summary>

#### Login to Generate JWT Token

```http
POST /auth/jwt/login
```

**Parameters** (application/x-www-form-urlencoded):

-   `username`: Your username.
-   `password`: Your password.

**Successful Response**: Returns a `BearerResponse` with your `access_token` and `token_type`.

#### Logout

```http
POST /auth/jwt/logout
```

**Requirement**: Bearer token authentication.

**Successful Response**: Logs out the user, invalidating the current token.

### Account Management

#### Register a New User

```http
POST /auth/register
```

**Body** (application/json):

-   `email`: Valid email address.
-   `password`: Password for the account.

**Successful Response**: Returns user details upon successful account creation.

#### Forgot Password

```http
POST /auth/forgot-password
```

**Body** (application/json):

-   `email`: Email address associated with your account.

**Successful Response**: Initiates a password reset process.

#### Reset Password

```http
POST /auth/reset-password
```

**Body** (application/json):

-   `token`: Password reset token sent to your email.
-   `password`: New password for your account.

**Successful Response**: Confirms the password has been successfully reset.

### Verification

#### Request Verification Token

```http
POST /auth/request-verify-token
```

**Body** (application/json):

-   `email`: Your account's email address to receive the verification token.

**Successful Response**: Sends a verification token to the provided email.

#### Verify Account

```http
POST /auth/verify
```

**Body** (application/json):

-   `token`: Verification token sent to your email.

**Successful Response**: Account is verified.

</details>

### General

<details>
  <summary>Routes</summary>

#### Get Root Message

```http
GET /
```

**Successful Response**: Returns a welcome message or API status.

#### Health Check

```http
GET /health
```

**Successful Response**: Returns "OK" if the service is up and running.

</details>

### Query Processing

<details>
  <summary>Routes</summary>

#### Submit a Query

```http
POST /query
```

**Body** (application/json):

-   `query`: Your query string.

**Successful Response**: Processes and returns the result of your query.

</details>

### Document Management

<details>
  <summary>Routes</summary>

#### List Documents

```http
GET /documents/documents
```

**Requirement**: Bearer token authentication.

**Successful Response**: Lists all documents associated with the user.

#### Upload a Document

```http
POST /documents/documents
```

**Requirement**: Bearer token authentication.

**Form Data**:

-   `files`: One or more files to upload.

**Successful Response**: Confirms the document(s) have been uploaded.

</details>
