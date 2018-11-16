const express = require('express')
const app = express()
const path = require('path')
const config = require('./config/config')
const db = require('./config/db')
const query = require('./query')
const stringify = require('csv-stringify');
const fs = require('fs');

// Query the database and export results as CSV
db.result(`${query}`, {
    query: query
})
    .then((results) => {
        // Check that there was results from the query
        if (!results.rows || results.rows.length == 0) {
            console.log("No results were found")
            return
        }

        // Create a header row and add it to the result rows
        header = JSON.parse(JSON.stringify(results.rows[0]))
        for (let key of Object.keys(header)) {
            header[key] = key
        }
        results.rows.unshift(header)

        // Convert the rows to CSV
        stringify(results.rows, (err, output) => {
            // Save the CSV file to disk
            fs.writeFile('data.csv', output, 'utf8', (err) => {
                // Check if an error occured while writing to disk
                if (err) {
                    console.log(err);
                    return
                }

                console.log('Successfully saved results as data.csv')
            });
        });
    })
    .catch(error => {
        console.log(error)
    })

// Serve files from root
app.use(express.static(path.join(__dirname, '/')))

// Start server
app.listen(config.PORT)
console.log(`Server listening on port: ${config.PORT}`)