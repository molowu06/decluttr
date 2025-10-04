import { Link } from "react-router-dom";

export default function Landing() {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-b from-slate-900 to-slate-700 text-white">
      <h1 className="text-5xl font-bold mb-6">Decluttr</h1>
      <p className="text-lg mb-8 text-gray-300 text-center max-w-md">
        Clean up your inbox and reclaim your focus. Decluttr helps you sort, unsubscribe, and stay organized effortlessly.
      </p>
      <div className="space-x-4">
        <Link to="/auth">
          <button className="px-6 py-3 bg-blue-500 hover:bg-blue-600 rounded-lg font-semibold">
            Get Started
          </button>
        </Link>
        <Link to="/auth">
          <button className="px-6 py-3 border border-white rounded-lg font-semibold hover:bg-white hover:text-slate-800">
            Log In
          </button>
        </Link>
      </div>
    </div>
  );
}