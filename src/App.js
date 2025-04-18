import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Clients from "./components/Clients";
import ClientForm from "./components/ClientForm";
import ProjectManagers from "./components/ProjectManagers";
import ProjectManagerForm from "./components/ProjectManagerForm";
import Projects from "./components/Projects";
import ProjectForm from "./components/ProjectForm";
import Invoices from "./components/Invoices";
import InvoiceForm from "./components/InvoiceForm";
import AdminDashboard from "./components/AdminDashboard";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css';  



function App() {
  return (
    <Router>
      <nav style={{ padding: "10px", background: "#eee" }}>
        <Link to="/">Clients</Link> |{" "}
        <Link to="/add-client">Add Client</Link> |{" "}
        <Link to="/managers">Project Managers</Link> |{" "}
        <Link to="/add-project-manager">Add Project Manager</Link> |{" "}
        <Link to="/projects">Projects</Link> |{" "}
        <Link to="/add-project">Add Project</Link> |{" "}
        <Link to="/invoices">Invoices</Link> |{" "}
        <Link to="/add-invoice">Add Invoice</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Clients />} />
        <Route path="/add-client" element={<ClientForm />} />
        <Route path="/managers" element={<ProjectManagers />} />
        <Route path="/add-project-manager" element={<ProjectManagerForm />} />
        <Route path="/projects" element={<Projects />} />
        <Route path="/add-project" element={<ProjectForm />} />
        <Route path="/invoices" element={<Invoices />} />
        <Route path="/add-invoice" element={<InvoiceForm />} />
        <Route path="/admin" element={<AdminDashboard />} />
      </Routes>
    </Router>
  );
}

export default App;
