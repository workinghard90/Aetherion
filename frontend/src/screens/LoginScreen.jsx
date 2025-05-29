import React, { useState } from "react";
import { login } from "../services/useAuth";

export default function LoginScreen() {
  const [user, setUser] = useState(null);

  const handleLogin = async () => {
    try {
      const response = await login({ username: "autumn", password: "secret" });
      setUser(response);
    } catch (e) {
      alert(e.message);
    }
  };

  return (
    <>
      <button onClick={handleLogin}>Login</button>
      {user && <p>Welcome, {user.username}!</p>}
    </>
  );
}
