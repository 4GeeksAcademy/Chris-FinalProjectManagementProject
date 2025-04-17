import React, { useEffect } from "react";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import { SignUpSelector } from "../components/SignUpSelector.js";
export const SignUpPage = () => {
  const { store, dispatch } = useGlobalReducer();

  return (
    <div className="text-center mt-5">
      <SignUpSelector />
    </div>
  );
};
