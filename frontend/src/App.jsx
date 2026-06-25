import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function App() {
  const [requirement, setRequirement] = useState("");
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [keyword, setKeyword] = useState("");
  const [darkMode, setDarkMode] = useState(
  localStorage.getItem("darkMode") === "true"
);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
  localStorage.setItem("darkMode", darkMode);
}, [darkMode]);

  const fetchHistory = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/history");
      setHistory(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const searchHistory = async () => {
    try {
      if (keyword.trim() === "") {
        fetchHistory();
        return;
      }

      const response = await axios.get(
        "http://127.0.0.1:8000/history/search",
        {
          params: {
            keyword: keyword,
          },
        }
      );

      setHistory(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const generateTestCases = async () => {
    if (!requirement.trim()) {
     toast.warning("Please enter a requirement");
      return;
    }

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/generate-testcases",
        {
          requirement,
        }
      );

      setResult(response.data.testcases);
      fetchHistory();
    } catch (error) {
      console.error(error);
      toast.error("Failed to generate test cases");
    } finally {
      setLoading(false);
    }
  };

  const deleteRecord = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/history/${id}`);
      fetchHistory();
    } catch (error) {
      console.error(error);
    }
  };

  const clearHistory = async () => {
  try {
    await axios.delete(
      "http://127.0.0.1:8000/history"
    );

    fetchHistory();

    toast.success("History cleared successfully");

  } catch (error) {
    console.error(error);
  }
};

  const exportExcel = async () => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/export",
      {
        responseType: "blob",
      }
    );

    const url = window.URL.createObjectURL(
      new Blob([response.data])
    );

    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "history.xlsx");
    document.body.appendChild(link);
    link.click();
    link.remove();
  } catch (error) {
    console.error(error);
  }
};

const exportPDF = async () => {
  try {
    await axios.get(
      "http://127.0.0.1:8000/pdf"
    );

    toast.success("PDF generated successfully");
  } catch (error) {
    console.error(error);
  }
};

const copyTestCases = () => {
  if (!result) return;

  const text = `
Test Scenarios
${result.test_scenarios?.join("\n")}

Positive Test Cases
${result.positive_test_cases?.join("\n")}

Negative Test Cases
${result.negative_test_cases?.join("\n")}

Expected Results
${result.expected_results?.join("\n")}
`;

  navigator.clipboard.writeText(text);
  toast.success("Copied successfully!");
};
  return (
    <div className={darkMode ? "container dark" : "container"}>
      <h1 className="title">TestMind AI 🚀</h1>

      <button
        className="button"
        onClick={() => setDarkMode(!darkMode)}
      >
        {darkMode ? "☀️ Light Mode" : "🌙 Dark Mode"}
      </button>

      <br />
      <br />

      <textarea
        rows="5"
        placeholder="Enter requirement..."
        value={requirement}
        onChange={(e) => setRequirement(e.target.value)}
      />

      <br />
      <br />

      <button
  className="button"
  onClick={generateTestCases}
  disabled={loading}
>
  {loading ? "⏳ Generating Test Cases..." : "🚀 Generate Test Cases"}
</button>

      {/* AI Output */}
      {result && (
        <>
          <div className="card">
            <button className="button" onClick={copyTestCases}>
  📋 Copy Test Cases
</button>

<br />
<br />
            <h2>Test Scenarios</h2>
            <ul>
              {result.test_scenarios?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </div>

          <div className="card">
            <h2>Positive Test Cases</h2>
            <ul>
              {result.positive_test_cases?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </div>

          <div className="card">
            <h2>Negative Test Cases</h2>
            <ul>
              {result.negative_test_cases?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </div>

          <div className="card">
            <h2>Expected Results</h2>
            <ul>
              {result.expected_results?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}
            </ul>
          </div>
        </>
      )}

      <hr />

      <h2>Search History</h2>

      <input
        className="search-box"
        type="text"
        placeholder="Search requirement..."
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
      />

      <button className="button" onClick={searchHistory}>
        Search
      </button>

      <button
        className="button"
        onClick={() => {
          setKeyword("");
          fetchHistory();
        }}
      >
        Reset
      </button>

      <button className="button" onClick={exportExcel}>
        Export Excel
      </button>

      <button className="button" onClick={exportPDF}>
  📄 Export PDF
</button>

      <button className="button" onClick={clearHistory}>
  🗑 Clear History
</button>

      <hr />

<h2>Dashboard</h2>

<div className="stats-container">
  <div className="stat-card">
    <h3>Total Records</h3>
    <p>{history.length}</p>
  </div>

  <div className="stat-card">
    <h3>Search Results</h3>
    <p>{history.length}</p>
  </div>

  <div className="stat-card">
    <h3>Current Mode</h3>
    <p>{darkMode ? "🌙 Dark" : "☀️ Light"}</p>
  </div>
</div>

<hr />

<h2>History</h2>

      {history.map((item) => (
        <div key={item.id} className="history-card">
          <h4>Requirement</h4>
          <p>{item.requirement}</p>

          <h4>Response</h4>
          <pre>{item.response}</pre>

          <button
            className="delete-btn"
            onClick={() => deleteRecord(item.id)}
          >
            Delete
          </button>
        </div>
      ))}
      <ToastContainer />
    </div>
  );
}

export default App;