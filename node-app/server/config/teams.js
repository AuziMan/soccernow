const express = require('express');
const router = express.Router();


const PYTHON_API = 'http://127.0.0.1:5000/teams';

const getAllTeams = async () => {
    try {
        const response = await fetch(`${PYTHON_API}/teams`);
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

const getTeamById = async (teamId) => {
    try {
        const response = await fetch(`${PYTHON_API}/${teamId}`);
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
    getAllTeams,
    getTeamById
}