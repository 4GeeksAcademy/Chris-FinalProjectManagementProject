import React, { useEffect } from "react"
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";

export const SignUpSelector = () => {

    const { store, dispatch } = useGlobalReducer()

    


    return (
        <div className="text-center mt-5"> 
            <buttton className="btn">ProjectManager</buttton>
            <buttton className="btn">Client</buttton>
            <buttton className="btn">SoftwareDeveloper</buttton>

        </div>
    );
}; 