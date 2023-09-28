#!/usr/bin/node

const request = require('request');
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(filmUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;

    for (const characterUrl of characters) {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    }
  }
});
