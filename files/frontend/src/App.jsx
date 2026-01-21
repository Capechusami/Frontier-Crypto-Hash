import { useEffect, useState } from 'react';
import './index.css';

export default function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/hash")
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch((e) => {
        setError("Failed to load data from backend");
        setLoading(false);
        console.error(e);
      });
  }, []);

  return (
    <div className="page">
      <header>
        <h1>Hashing Demonstration</h1>
        <p>SHA-256 | Avalanche Effect</p>
      </header>

      {loading && <div className="card">Loading…</div>}
      {error && <div className="card error">{error}</div>}

      {data && (
        <div className="grid">
          <div className="card">
            <h2>Original String</h2>
            <p className="mono">{data.original}</p>
            <label>SHA-256 Hash</label>
            <p className="mono hash">{data.original_hash}</p>
          </div>

          <div className="card">
            <h2>Modified String</h2>
            <p className="mono">{data.modified}</p>
            <label>SHA-256 Hash</label>
            <p className="mono hash">{data.modified_hash}</p>
          </div>

          <div className="card highlight">
            <h2>Observation</h2>
            <p>{data.observation}</p>
            <ul>
              <li>One-character change ⇒ drastically different hash.</li>
              <li>Demonstrates SHA-256 avalanche effect.</li>
              <li>Hashes are fixed-length and deterministic.</li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
}