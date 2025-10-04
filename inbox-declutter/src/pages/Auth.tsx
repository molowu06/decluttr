import { useNavigate } from "react-router-dom";
import { useState } from "react";

export default function Auth() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // For demo, pretend user logged in
    navigate("/dashboard");
  };

  return (
    <div className="flex items-center justify-center h-screen bg-slate-800 text-white">
      <form onSubmit={handleSubmit} className="bg-slate-900 p-8 rounded-2xl shadow-lg w-80">
        <h2 className="text-2xl font-bold mb-6 text-center">Sign In / Sign Up</h2>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full p-2 mb-4 bg-slate-700 rounded-lg focus:outline-none"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 mb-6 bg-slate-700 rounded-lg focus:outline-none"
        />
        <button
          type="submit"
          className="w-full bg-blue-500 hover:bg-blue-600 py-2 rounded-lg font-semibold"
        >
          Continue
        </button>
      </form>
    </div>
  );
}