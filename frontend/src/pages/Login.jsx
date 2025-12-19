function Login({ onLogin }) {
  const handleLogin = () => {
    // For now this is a dummy login
    // Later this will redirect to Google OAuth
    onLogin();
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2 style={{margin: "0 auto", textAlign: "center"}}>Code Query Portal</h2>
      <p style={{textAlign: "center", margin: "10rm 0"}}>Please login to continue</p>

      <button style={{display: "block",backgroundColor: "green",boxShadow: "2px 2px 5px gray",border:"none",color: "white",padding: "15px 15px",borderRadius: "10px" , margin: "10vh auto"}} onClick={handleLogin}>
        Login with Google
      </button>
    </div>
  );
}

export default Login;
