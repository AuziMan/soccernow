const express = require('express');
const router = express.Router();

const { getMLSGames } = require('../config/sports'); // Adjust the path

router.get('/', async (req, res) => {
    try {
      const data = await getMLSGames();
      res.render('main', {data});
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        res.status(500).send('Error fetching data from Python API');
    }
  });


  module.exports = router;
