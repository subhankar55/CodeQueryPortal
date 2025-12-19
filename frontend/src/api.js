export async function sendQuery(query) {
  const res = await fetch("http://localhost:5000/query", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query })
  });
  return res.json();
}
