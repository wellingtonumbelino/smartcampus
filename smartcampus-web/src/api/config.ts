import axios from "axios";

const roomApi = axios.create({
  baseURL: import.meta.env.VITE_API_ORION_URL,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

const iotApi = axios.create({
  baseURL: import.meta.env.VITE_API_IOT_URL,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "http://localhost:5173",
  },
});

export { roomApi, iotApi };
