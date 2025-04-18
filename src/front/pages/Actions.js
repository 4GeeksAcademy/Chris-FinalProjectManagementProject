const handleResponse = async (response) => {
  if (!response.ok) {
    const errorData = await response
      .json()
      .catch(() => ({ message: "Unknown error occurred" }));
    throw new Error(
      errorData.message || `Request failed with status ${response.status}`
    );
  }
  return response.json();
};
export const fetcClients = async (dispatch) => {
    try{
        dispatch({type:"load_clients"})

        const response=await fetch(`${process.env.VITE_BACKEND_URL}/api/clients`)
    }
};
