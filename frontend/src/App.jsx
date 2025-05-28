// frontend/src/App.jsx
import React from "react";
import "./App.css";

function App() {
  return (
    <div className="homepage-container">
      <div className="hero">
        <h1 className="title">AetherionAI</h1>
        <p className="tagline">Empowering secure, intelligent infrastructure for the future.</p>

        <a href="#vault" className="cta-button">
          Enter the Vault
        </a>

        <div className="button-row">
          <a href="#docs" className="secondary-button">Docs</a>
          <a href="#api" className="secondary-button">API</a>
          <a href="#team" className="secondary-button">Team</a>
        </div>
      </div>
    </div>
  );
}

export default App;
