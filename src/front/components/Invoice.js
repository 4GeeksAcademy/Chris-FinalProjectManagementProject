import React, { useEffect, useState } from "react";
import API from "../api";

function Invoices() {
  const [invoices, setInvoices] = useState([]);

  useEffect(() => {
    API.get("/invoices")
      .then((res) => setInvoices(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h2>Invoices</h2>
      <ul>
        {invoices.map((invoice) => (
          <li key={invoice.id}>
            {invoice.project} - ${invoice.amount} - {invoice.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Invoices;
  