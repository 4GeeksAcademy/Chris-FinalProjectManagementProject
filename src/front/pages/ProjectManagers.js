import React, { useState } from "react";
import API from "../api";

function ProjectManagerForm() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    is_active: true,
    first_name: "",
    last_name: "",
    phone_number: "",
    skills: "",
    experience: ""
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    API.post("/project-manager", formData)
      .then(() => alert("Project Manager created!"))
      .catch((err) => {
        console.error(err);
        alert("Error creating Project Manager");
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Create Project Manager</h3>
      <input name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
      <input name="password" type="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
      <input name="first_name" placeholder="First Name" value={formData.first_name} onChange={handleChange} required />
      <input name="last_name" placeholder="Last Name" value={formData.last_name} onChange={handleChange} required />
      <input name="phone_number" placeholder="Phone Number" value={formData.phone_number} onChange={handleChange} required />
      <input name="skills" placeholder="Skills" value={formData.skills} onChange={handleChange} required />
      <textarea name="experience" placeholder="Experience" value={formData.experience} onChange={handleChange}></textarea>
      <button type="submit">Add Manager</button>
    </form>
  );
}

export default ProjectManagerForm;
