import { useState } from "react";
import api from "./services/api";

export default function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState("");

  const login = async () => {
    const res = await api.post("/auth/login", { username, password });
    setToken(res.data.token);
  };

  return (
    <div>
      <h1>Aetherion Login</h1>
      <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      <button onClick={login}>Login</button>
      {token && <p>Token: {token}</p>}
    </div>
  );
}
