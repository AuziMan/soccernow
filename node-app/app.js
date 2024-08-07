//require('dotenv').config();
const express = require('express');
const expressLayout = require('express-ejs-layouts');
const app = express();

app.use(express.static('public'));


const PORT = 3000 || process.env.PORT;

// Templating engine
app.use(expressLayout);
app.set('view engine', 'ejs');
app.set('layout', './layouts/main');

const sportsRouter = require('./server/routes/games');
const mainRoute = require('./server/routes/main');
const teamRoute = require('./server/routes/teams');


app.use('/', sportsRouter); // Mount the sports router at root path
app.use('/', mainRoute);
app.use('/', teamRoute);



app.listen(PORT, () =>{
    console.log(`App is listening on port ${PORT}`);
});