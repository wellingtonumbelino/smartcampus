import { iotApi } from "../api/config";

export async function getAllDevices() {
  try {
    const { data } = await iotApi.get("/devices");

    return { data: data, error: null };
  } catch (error) {
    return { data: null, error: error };
  }
}
