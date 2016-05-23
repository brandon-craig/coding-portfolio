import Vue from 'vue';

import { EventEmitter } from 'events';
import { Promise } from 'es6-promise';

const shipCache = Object.create(null);
const ship = new EventEmitter();
const shipBaseUrl = 'http://swapi.co/api/starships/';
export default ship;

ship.fetch = id => {
  if (!id) {
    return Promise.resolve('');
  }
  return new Promise((resolve, reject) => {
    if (shipCache[id]) {
      resolve(shipCache[id]);
    }
    const shipToGet = `${shipBaseUrl}${id}/`;
    Vue.http.get(shipToGet).then(response => {
      const shipData = shipCache[id] = response.data;
      resolve(shipData);
    }, reject);
  });
};
