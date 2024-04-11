const express = require('express');

const mongoose = require('mongoose');
const app = express();
const ejs = require('ejs');

app.set('view engine', 'ejs'); // Set your templating engine (EJS in this case)

const uri = "mongodb+srv://User1:TestPassword9028_@cluster0.boy2x7w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  
    await client.connect();
    console.log('Connected to MongoDB Atlas');

    const database = client.db('SmartMeters'); // Replace with your database name
    const collection = database.collection('multipleApartments');

    app.get('/display-apartments', async (req, res) => {
      try {
          const db = client.db('SmartMeters');
          const collection = db.collection('multipleApartments');
  
          // Fetch apartments where "apartment" is set to 101
          const apartments = await collection.find({ apartment: '101' }).toArray();
  
          // Render the EJS template with the fetched data
          res.render('apartments.ejs', { apartments });
      } catch (error) {
          console.error('Error fetching apartments:', error);
          res.status(500).send('Internal server error');
      }
  });


/*app.get('/post', async(req, res) => {
    const uri = "mongodb+srv://User1:TestPassword9028_@cluster0.boy2x7w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
    await client.connect();
      const database = client.db('SmartMeters');
      const collection = database.collection('multipleApartments');
      console.log('went through');
      const data = await collection.find({ "apartment": 101 }).limit(1).toArray();

      res.json(data);

})*/
app.use(express.static('public'));
//app.set('view engine', 'ejs');

/*
app.get('/views/afterlogIn', (req, res) => {
  // Read the content of afterlogin.ejs (assuming it's in the same folder)
  /*const ejsContent = fs.readFileSync('afterlogin.ejs', 'utf8');
  //res.send(ejsContent);

  const username = 'John'; // Replace with actual username (from session or authentication)
    res.render('afterlogin', { username });
});*/

// server.js (Express route handler)
app.get('/smartMeters', (req, res) => {
  // Read the .ejs file content (assuming it's in the 'views' folder)
  //const ejsContent = fs.readFileSync(path.join(__dirname, 'views', 'my_template.ejs'), 'utf8');
  //res.send(ejsContent);
  const username = 'John'; // Replace with actual username (from session or authentication)
    res.render('smartMeters', { username });
});

/*
app.get('/public/afterlogIn', async (req, res) => {
  //const data = await fetchData(); // Retrieve data from MongoDB
  const data = { username: 'exampleUser' };
    res.render('afterlogIn', { data }); // Render your HTML template
});
*/
app.use(express.static('public')); 

app.get('/login', (req, res) => {
    res.sendFile(__dirname + '/login.html'); // Replace with the actual path to your HTML file
  });

app.listen(3000, () => {
  console.log('Server running on port 3000');
});


