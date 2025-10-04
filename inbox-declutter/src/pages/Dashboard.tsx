export default function Dashboard() {
  return (
    <div className="min-h-screen bg-slate-900 text-white flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4">Welcome to Decluttr</h1>
      <p className="text-gray-400 mb-8">Let’s start cleaning up your inbox 🧹</p>
      <button className="bg-green-500 hover:bg-green-600 px-6 py-3 rounded-lg font-semibold">
        Connect Inbox
      </button>
    </div>
  );
}
