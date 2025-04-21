import React, { useState } from "react";

export const SignUpSelector = () => {
  const [formData, setFormData] = useState({ email: "", password: "" });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  const validateEmail = (email) => {
    // Basic email pattern
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setError("");

    // Simple validations
    if (!validateEmail(formData.email)) {
      setError("Please enter a valid email address.");
      return;
    }
    if (formData.password.length < 6) {
      setError("Password must be at least 6 characters long.");
      return;
    }

    // If everything is valid
    console.log("Form Submitted:", formData);
    setSuccess(true);
    setFormData({ email: "", password: "" }); // Clear form
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <div style={{ width: "300px", margin: "0 auto" }}>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
          style={{ width: "100%", padding: "10px", marginBottom: "10px" }}
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
          style={{ width: "100%", padding: "10px", marginBottom: "10px" }}
        />
        <button
          type="submit"
          style={{
            width: "100%",
            padding: "10px",
            backgroundColor: "#4CAF50",
            color: "white",
            border: "none",
            cursor: "pointer"
          }}
        >
          Sign Up
        </button>
      </form>

      {error && <p style={{ color: "red", marginTop: "10px" }}>{error}</p>}
      {success && <p style={{ color: "green", marginTop: "10px" }}>Account created successfully!</p>}
    </div>
  );
};
