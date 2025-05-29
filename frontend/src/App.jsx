import React, { useEffect, useState } from "react";
import linksData from "./data/links.json";

function App() {
  const [links, setLinks] = useState([]);

  useEffect(() => {
    setLinks(linksData);
  }, []);

  return (
    <div className="button-group">
      {links.map((link, idx) => (
        <a
          key={idx}
          className="mystic-btn"
          href={link.url}
          target="_blank"
          rel="noopener noreferrer"
        >
          {link.icon} {link.label}
        </a>
      ))}
    </div>
  );
}

export default App;
