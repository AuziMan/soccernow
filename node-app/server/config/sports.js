const express = require('express');
const router = express.Router();


const PYTHON_API = 'http://127.0.0.1:5000';

const getEuroGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API}/euro-games`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

const getMLSGames = async () => {
    try {
        const response = await fetch(`${PYTHON_API}/mls-games`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        //console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data from Python API:', error);
        throw error; // Re-throw the error to handle it in the calling function
    }
}

module.exports = {
    getMLSGames,
    getEuroGames
};
