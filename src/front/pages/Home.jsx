import React, { useEffect } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import { SignUpPage } from "../components/SignUpPage.jsx";

export const Home = () => {

	const { store, dispatch } = useGlobalReducer()




	return (
		<div className="text-center mt-5">
			<SignUpPage />
		</div>
	);
}; 