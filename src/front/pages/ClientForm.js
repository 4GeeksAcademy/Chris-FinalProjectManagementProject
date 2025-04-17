import React, { useState } from "react";
import API from "../api";

function ClientForm() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    is_active: true,
    first_name: "",
    last_name: "",
    phone_number: "",
    about_me: ""
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    API.post("/add-client", formData)
      .then((res) => {
        alert("Client added!");
        setFormData({
          email: "",
          password: "",
          is_active: true,
          first_name: "",
          last_name: "",
          phone_number: "",
          about_me: ""
        });
      })
      .catch((err) => {
        console.error(err);
        alert("Failed to add client.");
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Create Client</h3>
      <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
      <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
      <input type="text" name="first_name" placeholder="First Name" value={formData.first_name} onChange={handleChange} required />
      <input type="text" name="last_name" placeholder="Last Name" value={formData.last_name} onChange={handleChange} required />
      <input type="text" name="phone_number" placeholder="Phone Number" value={formData.phone_number} onChange={handleChange} required />
      <textarea name="about_me" placeholder="About Me" value={formData.about_me} onChange={handleChange}></textarea>
      <button type="submit">Add Client</button>
    </form>
  );
}

export default ClientForm;
