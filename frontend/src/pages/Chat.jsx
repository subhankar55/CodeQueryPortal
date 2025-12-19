import { useState } from "react";
import { sendQuery } from "../api";

function Chat({ user }) {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    const res = await sendQuery(query);
    setResponse(res.code || res.message);
  };

  return (
    <div>
      <div>
      <p style={{textAlign:"center"}}>Welcome, {user.name}</p>
      </div>
      <textarea style={{display: "block", margin: "10px auto"}}
        placeholder="Enter your coding question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <br />
      <button style={{display:"block", margin: "10px auto", backgroundColor: "green",boxShadow: "2px 2px 5px gray",border:"none",borderRadius: "10px",padding: "15px 15px",color: "white",}} onClick={handleSend}>Submit</button>
      <pre style={{display: "block",margin: "10px auto"}}>{response}</pre>
    </div>
  );
}

export default Chat;
