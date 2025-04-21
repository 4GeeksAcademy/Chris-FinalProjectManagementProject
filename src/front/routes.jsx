

import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
} from "react-router-dom";
import { Layout } from "./pages/Layout";
import { Home } from "./pages/Home";

import { SignUpPage } from "./components/SignUpPage";




export const router = createBrowserRouter(
  createRoutesFromElements(
    
       
    <Route path="/" element={<Layout />} errorElement={<h1>Not found!</h1>} >

      {/* Nested Routes: Defines sub-routes within the BaseHome component. */}
      <Route index element={<Home />} />
 

      <Route path="/signup" element={<SignUpPage />} />
    </Route>
  )
);