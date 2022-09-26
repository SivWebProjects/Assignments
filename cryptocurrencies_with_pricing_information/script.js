// Objective: To print the list of cryptocurrencies with pricing information by hitting an API

// Deliverable: Backend code which queries the shared API, and prints the cryptocurrency prices 
// that are returned on the frontend. Frontend is not the focus, though a visually appealing 
// interface wouldn't hurt.

// Flow: Read the API URL -> Isolate the Cryptocurrency Titles and Prices through a loop -> 
// Display Prices in a tabular format

// API URL
// https://api.coinstats.app/public/v1/coins?skip=0&limit=100&currency=INR

let tableBody = document.getElementById("tableBody");
const url = "https://api.coinstats.app/public/v1/coins?skip=0&limit=100&currency=INR";

function displayCryptoAndPrices(data) {
    let cryptoName = data.name;
    let cryptoPrice = data.price;

    // Creating Row inside Table Body
    let bodyRowElement = document.createElement("tr");
    tableBody.appendChild(bodyRowElement);

    // Creating Data Cell inside Row
    let rowDataCell1Element = document.createElement("td");
    rowDataCell1Element.textContent = cryptoName;
    bodyRowElement.appendChild(rowDataCell1Element);

    // Creating Another Data Cell inside Row
    let rowDataCell2Element = document.createElement("td");
    rowDataCell2Element.textContent = cryptoPrice;
    bodyRowElement.appendChild(rowDataCell2Element);
}

function displayResults(cryptoData) {
    for (let data of cryptoData) {
        displayCryptoAndPrices(data);
    }
}

function getCryptoCurrencyData() {
    let options = {
        method: "GET"
    };

    fetch(url, options)
        .then(function(response) {
            return response.json();
        })
        .then(function(jsonData) {
            console.log(jsonData);
            let cryptoData = jsonData.coins;
            displayResults(cryptoData);
        });
}
getCryptoCurrencyData();
