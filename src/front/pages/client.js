import React, { useEffect, useState } from "react";
import API from "../api";

function Clients() {
  const [clients, setClients] = useState([]);

  useEffect(() => {
    API.get("/clients")
      .then((res) => setClients(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h2>Clients</h2>
      <ul>
        {clients.map((client) => (
          <li key={client.id}>
            {client.first_name} {client.last_name} ({client.email})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Clients;
