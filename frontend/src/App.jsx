import { useState, useEffect } from "react";
import { login } from "./services/useAuth";
import api from "./services/api"; // Auth-aware Axios instance

function App() {
  const [buttons, setButtons] = useState([]);
  const [user, setUser] = useState(() => {
    const saved = localStorage.getItem("user");
    return saved ? JSON.parse(saved) : null;
  });

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    api.get("/api/buttons")
      .then(res => setButtons(res.data))
      .catch(err => console.error("Failed to load buttons:", err));
  }, []);

  const handleLogin = async () => {
    try {
      const res = await login({ username, password });
      setUser(res);
      localStorage.setItem("user", JSON.stringify(res));
    } catch (err) {
      alert(err.message);
    }
  };

  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem("user");
  };

  return (
    <div className="App">
      <h1>Aetherion</h1>

      {!user ? (
        <div className="login-form">
          <input
            placeholder="Username"
            value={username}
            onChange={e => setUsername(e.target.value)}
          />
          <input
            placeholder="Password"
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
          />
          <button onClick={handleLogin}>Login</button>
        </div>
      ) : (
        <div>
          <p>Welcome, {user.username}</p>
          <button onClick={handleLogout}>Logout</button>
          {user?.isAdmin && (
            <a href="https://aetherionai-mobile.onrender.com/admin">Admin Panel</a>
          )}
        </div>
      )}

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
