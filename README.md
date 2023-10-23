# Python Server with IP Info

This is a simple Python server that provides information about the current date, time, IP address, and the approximate location of the client using the IPinfo API. The server renders this information as an HTML page.

## Prerequisites

Before running the server, you need to have the following:

1. Python 3.x installed
2. Required Python libraries (installed when building the Docker image)

## Usage

### Running the Docker Container

To run the server as a Docker container, follow these steps:

1. Build the Docker image:

   ```shell
   docker build -t my-python-server .
   ```
2. Run the Docker container:
    ```
    docker run -p 12345:12345 -e IPINFO_API_KEY=your_api_key my-python-server
    ```
3. The server will be accesible at `http://localhost:12345`