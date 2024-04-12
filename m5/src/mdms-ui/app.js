const { MongoClient } = require('mongodb');
const express = require('express');
const path = require('path');
const fs = require('fs');
const uri = "mongodb+srv://User1:TestPassword9028_@cluster0.boy2x7w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
  const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
  const bodyParser = require('body-parser');

const app = express();
app.set('port', process.env.PORT || 3000);

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.json());


//gets called by the statistics.ejs file
//updates the statistics page based on the smart meter chose
app.post('/process', async (req, res) => {

  //get the smart meter chosen and turn value into a Number
  const selectedOption = req.body.option;
  const intValue = Number(selectedOption);

  //get the databse and collection and query for the apartment we selected
  const database = client.db("SmartMeters"); 
  const collection = database.collection("multipleApartments"); 
  const apartments = await collection.find({apartment: intValue});
    

    //store the power consumtion values of the selected apartment
    const powers = [];

    await apartments.forEach(document => {
      powers.push(document.power);
    });
    

    let sum = 0;

    // Iterate through each element in the powers array and find the sum of power consumption
    for (let i = 0; i < powers.length; i++) {
        sum += powers[i];
    }

    //get the statistics file content
    const ejsContent = fs.readFileSync('views/statistics.ejs', 'utf8');

    //convert the comsumptions to have 2 decimals
    const consumptionForPriceCalculation = (sum/1000).toFixed(2);
    const consumptionkW  = sum.toFixed(2)

    //calculate the price and insert into statistics page
    const price = (consumptionForPriceCalculation* 0.073*24).toFixed(2);
    const val = `<br><label >The total power consumption for the last 3 days is: ${consumptionkW} kW</label><br><label >The total price is: ${price} $</label>`;
    const renderedContent = ejsContent.replace('<!-- INSERT_POWER_DATA -->', val);
    
    
    res.send(val);


  
});

//gets called by the login.html page once succesfully logged in
app.get('/smartMeters', async (req, res) => {

  try {
  
    //get the database and collection
    const database = client.db("SmartMeters"); // Replace with your database name
    const collection = database.collection("multipleApartments"); // Replace with your collection name
    const resultArray = [];

    //the following code will get the current smart meters available

    // Loop through apartment numbers from 101 to 110
    for (let apartmentNumber = 101; apartmentNumber <= 110; apartmentNumber++) {
        // Query to get the first entry for the current apartment number
        const query = { apartment: apartmentNumber };
        const document = await collection.findOne(query);

        // Extract the desired attributes and add them to the result array
        if (document) {
            resultArray.push({
                _id: document._id,
                apartment: document.apartment,
                time: document.time,
                power: document.power
            });
        }
    }



    //get the smartMeters.ehs page contnent and edit it with the apartment values
    
    const ejsContent = fs.readFileSync('views/smartMeters.ejs', 'utf8');


    const renderedContent = ejsContent.replace('<!-- INSERT_APARTMENT_DATA -->', generateApartmentRows(resultArray));
    
    
    res.send(renderedContent);
} catch (error) {
  console.error('Error fetching apartments:', error);
  res.status(500).send('Internal server error');
}
});

//gets called by the smartMeters.ejs file when clicking on the tab statistics
app.get('/statistics', async (req, res) => {

  //get the database and collection
  const database = client.db("SmartMeters"); // Replace with your database name
    const collection = database.collection("multipleApartments"); // Replace with your collection name
    const resultArray = [];

    //this will get all apartments

    // Loop through apartment numbers from 101 to 110
    for (let apartmentNumber = 101; apartmentNumber <= 110; apartmentNumber++) {
        // Query to get the first entry for the current apartment number
        const query = { apartment: apartmentNumber };
        const document = await collection.findOne(query);

        // Extract the desired attributes and add them to the result array
        if (document) {
            resultArray.push({
                apartment: document.apartment
            });
        }
    }

  
  

  try {
      //get the contenst of the statistics page and insert the apartment data into the <select> drop down
    const ejsContent = fs.readFileSync('views/statistics.ejs', 'utf8');

    
    const renderedContent = ejsContent.replace('<!-- INSERT_APARTMENT_DATA -->', generateStatsDropDown(resultArray));
    
    
    res.send(renderedContent);
} catch (error) {
  console.error('Error fetching apartments:', error);
  res.status(500).send('Internal server error');
}
});


//this will generate the rows of the smart meters page
function generateApartmentRows(array) {
 
  //get the values of the inputed apartments
  const rows = [];
  for (const apartments of array){
    const row = {
      id: apartments._id,
      number: apartments.apartment,
      time: apartments.time,
      power: apartments.power
  };
  rows.push(row);
  }

  //create and return the rows shown on the smart meters page
  return rows.map(row => `

      <tr>
          <td>${row.number}</td>
          <td>Active</td>
          <td><a href="statistics?param1=${row.number}">${row.number} Statistics</a></td>
      </tr>
  `).join('');
}

//this will create the <select> drop down on the statistics page
function generateStatsDropDown(array) {
  
  //get the values of the inputed apartments
  const rows = [];
  for (const apartments of array){
    const row = {
      id: apartments._id,
      number: apartments.apartment,
      time: apartments.time,
      power: apartments.power
  };
  rows.push(row);
  }

  //create and return the options showsn in the satistics drop down
  return rows.map(row => `
  <option value="${row.number}">${row.number}</option>
 
  `).join('');
}




// Define the route for the login page
app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'login.html'));
});


// Start the server, make the server start on the login page
app.listen(app.get('port'), () => {
    console.log(`Server running at http://localhost:${app.get('port')}/login`);
});

async function main() {
  

  try {
    //connect to the mongodb database
    await client.connect();
    console.log('Connected to MongoDB Atlas');

    
  } catch (error) {
    console.error('Error:', error);
  } finally {
    
  }
}

main().catch(console.error);


  