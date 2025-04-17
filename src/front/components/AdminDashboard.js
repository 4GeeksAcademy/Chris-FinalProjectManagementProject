import React, { useEffect, useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

function AdminDashboard() {
  const [clients, setClients] = useState([]);
  const [managers, setManagers] = useState([]);
  const [projects, setProjects] = useState([]);
  const [invoices, setInvoices] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const [clientsRes, managersRes, projectsRes, invoicesRes] = await Promise.all([
        API.get("/clients"),
        API.get("/project-managers"),
        API.get("/projects"),
        API.get("/invoices"),
      ]);
      setClients(clientsRes.data);
      setManagers(managersRes.data);
      setProjects(projectsRes.data);
      setInvoices(invoicesRes.data);
    } catch (err) {
      console.error("Error loading dashboard data", err);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Admin Dashboard</h1>

      <section style={{ marginBottom: "40px" }}>
        <h2>Clients</h2>
        <Link to="/add-client">➕ Add New Client</Link>
        <ul>
          {clients.map((client) => (
            <li key={client.id}>
              {client.first_name} {client.last_name} ({client.email})
            </li>
          ))}
        </ul>
      </section>

      <section style={{ marginBottom: "40px" }}>
        <h2>Project Managers</h2>
        <Link to="/add-project-manager">➕ Add New Project Manager</Link>
        <ul>
          {managers.map((manager) => (
            <li key={manager.id}>
              {manager.first_name} {manager.last_name} - {manager.skills}
            </li>
          ))}
        </ul>
      </section>

      <section style={{ marginBottom: "40px" }}>
        <h2>Projects</h2>
        <Link to="/add-project">➕ Add New Project</Link>
        <ul>
          {projects.map((project) => (
            <li key={project.id}>
              {project.name} - Manager: {project.project_manager} | Client: {project.client}
            </li>
          ))}
        </ul>
      </section>

      <section style={{ marginBottom: "40px" }}>
        <h2>Invoices</h2>
        <Link to="/add-invoice">➕ Add New Invoice</Link>
        <ul>
          {invoices.map((invoice) => (
            <li key={invoice.id}>
              {invoice.project} - ${invoice.amount} - {invoice.status}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default AdminDashboard;
