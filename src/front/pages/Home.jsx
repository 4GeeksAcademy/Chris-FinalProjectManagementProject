import React, { useEffect } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import { SignUpPage } from "../components/SignUpPage.jsx";

export const Home = () => {

	const { store, dispatch } = useGlobalReducer()

	const containerStyle = {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        minHeight: "100vh",
        padding: "2rem",
        background: "linear-gradient(to right, #74ebd5, #acb6e5)"
    };




	return (
		<div className="home-container">
			<SignUpPage /> 
			<style>
                {`
                    .home-container {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        flex-direction: column;
                        min-height: 100vh;
                        padding: 2rem;
                        background: linear-gradient(to right, #74ebd5, #acb6e5);
                    }
                `}
            </style>
		</div>
	);
}; 