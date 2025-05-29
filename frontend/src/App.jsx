import { useState, useEffect } from 'react';

const API_URL = import.meta.env.VITE_API_URL || "https://aetherionai-mobile.onrender.com";

function App() {
  const [buttons, setButtons] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/api/buttons`)
      .then(res => res.json())
      .then(setButtons)
      .catch(err => console.error("Failed to load buttons:", err));
  }, []);

  {user?.isAdmin && (
  <a href="https://aetherionai-mobile.onrender.com/admin">Admin Panel</a>
)}
  
  return (
    <div className="App">
      <h1>Aetherion</h1>
      <div className="button-container">
        {buttons.map(({ id, label, sigil, url }) => (
          <a key={id} href={url} target="_blank" rel="noopener noreferrer" className="button">
            <span className="sigil">{sigil}</span>
            <span className="label">{label}</span>
          </a>
        ))}
      </div>
    </div>
  );
}

export default App;
