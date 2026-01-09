import axios from 'axios';

const apiRoom = axios.create({
  baseURL: import.meta.env.VITE_API_ORION_URL,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

const apiDevice = axios.create({
  baseURL: import.meta.env.VITE_API_IOT_URL,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
});

export { apiRoom, apiDevice };
