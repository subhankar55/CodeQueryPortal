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
      <div style={{width: "40%",backgroundColor:"gray",height:"60vh",margin:"10vh auto",border:"none",borderRadius:"10px",padding:"2em"}}>
        <div style={{}}>
        <h2 style={{textAlign: "center",color:"white"}}>Login</h2>
        </div>
        <div style={{width: "30%", margin:"5.5em auto"}}>
        <GoogleLogin onSuccess={handleSuccess} onError={() => alert("Login Failed")} />
        </div>
      </div>
      
    
    </>
    
  );
}

export default Login;
