import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import "./styles/app.css";
import { GoogleOAuthProvider } from "@react-oauth/google";

createRoot(document.getElementById('root')).render(
   <GoogleOAuthProvider clientId="1057703273834-ln6o2p8n8evoho9sqjg52un487s4lrit.apps.googleusercontent.com">
    <App />
  </GoogleOAuthProvider>,
)
