import { useState } from "react";
import { askNutri } from "../services/api";
import "./Nutri.css";

export default function Nutri() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;

    setLoading(true);

    try {
      const response = await askNutri(question);
      setAnswer(response.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Unable to generate a response. Please try again.");
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleAsk();
    }
  };

  const suggestions = [
    "Is Maggi healthy?",
    "How much sugar should adults consume?",
    "Why is sodium harmful?",
    "Foods rich in protein"
  ];

  return (
    <div className="nutri-page">

      <div className="nutri-container">

        <h1 className="nutri-title">
          Nutri
        </h1>

        <p className="nutri-subtitle">
          Ask anything about nutrition, food, ingredients and healthy eating.
        </p>

        <div className="nutri-input-container">

          <input
            type="text"
            placeholder="Ask Nutri..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={handleKeyDown}
          />

          <button
            onClick={handleAsk}
            disabled={loading}
          >
            {loading ? "Thinking..." : "Ask Nutri"}
          </button>

        </div>

        <div className="suggestions">

          {suggestions.map((item, index) => (

            <button
              key={index}
              className="suggestion-chip"
              onClick={() => {
                setQuestion(item);
              }}
            >
              {item}
            </button>

          ))}

        </div>

        {answer && (

          <div className="response-card">

            <h2>Response</h2>

            <p>{answer}</p>

            <div className="response-footer">
              Educational information based on WHO, FSSAI and evidence-based nutrition guidance.
            </div>

          </div>

        )}

      </div>

    </div>
  );
}