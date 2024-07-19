
const express = require('express');
const router = express.Router();


const PYTHON_API = 'http://127.0.0.1:5000';

// Get sports data from python API 
// Route to get data from the Python API
router.get('/euro-games', async (req, res) => {
    try {
      const response = await fetch(`${PYTHON_API}/euro-games`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      if(data.result === 0){
        res.render('./partials/no-games');
      }else{
        res.render('index', { data });
      }
    } catch (error) {
      console.error('Error fetching data from Python API:', error);
      res.status(500).send('Error fetching data from Python API');
    }
  });


router.get('/mls-games', async (req, res) => {
  try {
    const response = await fetch(`${PYTHON_API}/mls-games`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    if(data.result === 0){
      res.render('./partials/no-games');
    }else{
      res.render('index', { data });
    }
  } catch (error) {
      console.error('Error fetching data from Python API:', error);
      res.status(500).send('Error fetching data from Python API');
    }
  });

module.exports = router;
