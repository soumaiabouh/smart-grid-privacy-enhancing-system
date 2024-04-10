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
//app.set('view engine', 'ejs');


app.post('/process', async (req, res) => {
  const selectedOption = req.body.option;
  const intValue = Number(selectedOption);

  const database = client.db("SmartMeters"); // Replace with your database name
  const collection = database.collection("multipleApartments"); // Replace with your collection name
  const apartments = await collection.find({apartment: intValue});
    

    const powers = [];

    await apartments.forEach(document => {
      powers.push(document.power);
    });
    

    let sum = 0;

    // Iterate through each element in the array
    for (let i = 0; i < powers.length; i++) {
        sum += powers[i];
    }

    const ejsContent = fs.readFileSync('views/statistics.ejs', 'utf8');

    const consumptionkW = (sum/1000).toFixed(2);
    const price = (consumptionkW* 0.073*24).toFixed(2);
    const val = `<br><label >The total power consumption for the last 3 days is: ${consumptionkW} kW</label><br><label >The total price is: ${price} $</label>`;
    const renderedContent = ejsContent.replace('<!-- INSERT_POWER_DATA -->', val);
    
    
    res.send(val);


  //console.log("Powers:", powers);


  // Process the arguments (e.g., call a function)
  // ...

  // Send a response back to the client
  //res.json({ message: 'Option received and processed.' });
});


app.get('/smartMeters', async (req, res) => {
  // Read the content of smartMeters.ejs (assuming it's in the same folder)
  

  try {
  
    
    const database = client.db("SmartMeters"); // Replace with your database name
    const collection = database.collection("multipleApartments"); // Replace with your collection name
    const resultArray = [];

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


    //const apartments = await collection.findOne({apartment : 101});
    //IMPORTANT
    /*const apartments = await collection.find().limit(5);
    

    const ids = [];
    const Apartments = [];
    const times = [];
    const powers = [];

    await apartments.forEach(document => {
      ids.push(document._id);
      Apartments.push(document.apartment);
      times.push(document.time);
      powers.push(document.power);
    });

    console.log("IDs:", ids);
    console.log("Apartments:", apartments);
    console.log("Times:", times);
    console.log("Powers:", powers);*/



    
    const ejsContent = fs.readFileSync('views/smartMeters.ejs', 'utf8');

    //console.log(generateApartmentRows(resultArray));
    const renderedContent = ejsContent.replace('<!-- INSERT_APARTMENT_DATA -->', generateApartmentRows(resultArray));
    
    
    res.send(renderedContent);
} catch (error) {
  console.error('Error fetching apartments:', error);
  res.status(500).send('Internal server error');
}
});

app.get('/statistics', async (req, res) => {
  // Read the content of smartMeters.ejs (assuming it's in the same folder)
  const database = client.db("SmartMeters"); // Replace with your database name
    const collection = database.collection("multipleApartments"); // Replace with your collection name
    const resultArray = [];

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
      
    const ejsContent = fs.readFileSync('views/statistics.ejs', 'utf8');

    
    const renderedContent = ejsContent.replace('<!-- INSERT_APARTMENT_DATA -->', generateStatsDropDown(resultArray));
    
    
    res.send(renderedContent);
} catch (error) {
  console.error('Error fetching apartments:', error);
  res.status(500).send('Internal server error');
}
});



function generateApartmentRows(array) {
  // if (!Array.isArray(apartments)) {
  //     console.error('Apartments data is not an array.');
  //     console.log(apartments.apartment);
  //     return ''; // Return an empty string or handle the error as needed
  // }
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
  
  

//<td>${row.time}</td>
  return rows.map(row => `

      <tr>
          <td>${row.number}</td>
          <td>Active</td>
          <td><a href="statistics?param1=${row.number}">${row.number} Statistics</a></td>
      </tr>
  `).join('');
}

function generateStatsDropDown(array) {
  // if (!Array.isArray(apartments)) {
  //     console.error('Apartments data is not an array.');
  //     console.log(apartments.apartment);
  //     return ''; // Return an empty string or handle the error as needed
  // }
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
  
  

//<td>${row.time}</td>
  return rows.map(row => `
  <option value="${row.number}">${row.number}</option>
 
  `).join('');
}


app.get('/display-apartments', async (req, res) => {
  try {
    // Fetch apartments where "apartment" is set to 101
    const apartments = await collection.find({ apartment: '101' });

    // Render the EJS template with the fetched data
    res.render('apartments.ejs', { apartments });
} catch (error) {
    console.error('Error fetching apartments:', error);
    res.status(500).send('Internal server error');
}
});


// Define the route for the login page
app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'login.html'));
});
app.get('/public/smartMeters', async (req, res) => {
  //const data = await fetchData(); // Retrieve data from MongoDB
  const data = { username: 'exampleUser' };
    res.render('smartMeters', { data }); // Render your HTML template
});

// Start the server
app.listen(app.get('port'), () => {
    console.log(`Server running at http://localhost:${app.get('port')}/login`);
});

async function main() {
  //const uri = "mongodb+srv://User1:TestPassword9028_@cluster0.boy2x7w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
  //const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  try {
    await client.connect();
    console.log('Connected to MongoDB Atlas');
    
    const database = client.db('SmartMeters'); // Replace with your database name
    const collection = database.collection('multipleApartments'); // Replace with your collection name

    //const doc = { name: 'Neapolitan pizza', shape: 'round' };
    //const result = await collection.insertOne(doc);

    //console.log(`A document was inserted with the _id: ${result.insertedId}`);
  } catch (error) {
    console.error('Error:', error);
  } finally {
    //await client.close();
  }
}

main().catch(console.error);

async function fetchData() {
    const uri = "mongodb+srv://User1:TestPassword9028_@cluster0.boy2x7w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
  
    try {
      await client.connect();
      const database = client.db('SmartMeters');
      const collection = database.collection('multipleApartments');
      //const data = await collection.find({}).toArray();
      //return data;
    } finally {
      await client.close();
    }
  }
  