# Quote Web Application

This application will fetch the quotes from an API Gateway.

## Getting started

Clone the repository to your local machine.

```sh
git clone https://github.com/tamkeen-cloud-engineering/quote-web-app.git
```

Change directory into the `quote-web-app` folder.

```sh
cd quote-web-app
```

Open the project in VS Code.

```sh
code .
```

Head over to the `index.html` page and update the `API_BASE_URL` variable to the URL of your API Gateway.

```html
// REPLACE THIS URL with your API Gateway "Invoke URL"
const API_BASE_URL = "https://your-api-gateway-url.execute-api.your-region.amazonaws.com"
```

## Running the web server

Start the web server.

```sh
python3 -m http.server 8080
```

Visit the web app [http://localhost:8080](http://localhost:8080) from your browser. Click on the buttons to make the requests.
