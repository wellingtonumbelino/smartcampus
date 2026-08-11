import { roomApi } from "../config/api";

export async function getAllBuildings() {
  try {
    const { data } = await roomApi.get(
      "/entities/?type=Room&options=keyValues&attrs=name,description",
    );
    return { data, error: null };
  } catch (error) {
    console.error("Error fetching buildings:", error);
    return { data: null, error };
  }
}
