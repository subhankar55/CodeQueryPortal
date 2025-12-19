import { GoogleLogin } from "@react-oauth/google";

function Login({ onLogin }) {
  const handleSuccess = async (credentialResponse) => {
    const res = await fetch("http://localhost:5000/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        token: credentialResponse.credential
      })
    });

    const data = await res.json();

    if (res.ok) {
      onLogin(data.user);
    }
  };

  return (
    <>
      <div>
      <h2 style={{textAlign: "center"}}>Login</h2>
      </div>
      <div style={{width: "20%", margin:"40px auto"}}>
      <GoogleLogin style={{with: "40%"}} onSuccess={handleSuccess} onError={() => alert("Login Failed")} />
      </div>
    
    </>
    
  );
}

export default Login;
