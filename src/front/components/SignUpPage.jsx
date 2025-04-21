import React, { useEffect, useState } from "react";
import { SignUpSelector } from "./SignUpSelector.jsx";

export const SignUpPage = () => {
  const [fadeIn, setFadeIn] = useState(false);
  const [loading, setLoading] = useState(true); // <--- NEW

  useEffect(() => {
    // Delay for 0.3 seconds, then fade in
    const timer = setTimeout(() => {
      setFadeIn(true);
      setLoading(false); // <--- NEW: stop loading
    }, 300);

    // Cleanup
    return () => clearTimeout(timer);
  }, []);

  const pageStyle = {
    textAlign: "center",
    marginTop: "5rem",
    opacity: fadeIn ? 1 : 0,
    transform: fadeIn ? "translateY(0)" : "translateY(20px)",
    transition: "opacity 1s ease-out, transform 1s ease-out"
  };

  const headingStyle = {
    fontSize: "2.5rem",
    color: "#333",
    fontWeight: "bold",
    marginBottom: "2rem"
  };

  const spinnerStyle = {
    width: "50px",
    height: "50px",
    border: "6px solid #f3f3f3",
    borderTop: "6px solid #3498db",
    borderRadius: "50%",
    animation: "spin 1s linear infinite",
    margin: "0 auto",
    marginTop: "5rem"
  };

  return (
    <>
      {loading ? (
        <div style={spinnerStyle}></div>
      ) : (
        <div style={pageStyle}>
          <h1 style={headingStyle}>Welcome to the Project Management App</h1>
          <SignUpSelector />
        </div>
      )}

      {/* Spinner Keyframes (inside style tag) */}
      <style>
        {`
          @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }
        `}
      </style>
    </>
  );
};
