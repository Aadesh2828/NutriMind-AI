import { useState } from "react";
import "./Prediction.css";
import { predictNutriScore } from "../services/api";

const gradeInfo = {
  A: {
    color: "#16a34a",
    title: "Excellent Nutritional Quality",
    description:
      "Rich in healthy nutrients and suitable for regular consumption.",
    recommendation:
      "Excellent choice for daily consumption as part of a balanced diet.",
  },
  B: {
    color: "#65a30d",
    title: "Good Nutritional Quality",
    description:
      "A healthy food choice with only minor nutritional concerns.",
    recommendation:
      "Suitable for frequent consumption in a balanced diet.",
  },
  C: {
    color: "#eab308",
    title: "Moderate Nutritional Quality",
    description:
      "Can be consumed in moderation as part of a healthy lifestyle.",
    recommendation:
      "Balance this food with fruits, vegetables and whole grains.",
  },
  D: {
    color: "#f97316",
    title: "Poor Nutritional Quality",
    description:
      "Contains higher amounts of sugar, salt or saturated fat.",
    recommendation:
      "Consume occasionally and consider healthier alternatives.",
  },
  E: {
    color: "#dc2626",
    title: "Very Poor Nutritional Quality",
    description:
      "High nutritional risk due to unhealthy nutrient composition.",
    recommendation:
      "Limit consumption and choose healthier alternatives whenever possible.",
  },
};

export default function Prediction() {
  const [form, setForm] = useState({
    energy_kcal: "",
    fat: "",
    saturated_fat: "",
    carbohydrates: "",
    sugars: "",
    proteins: "",
    fiber: "",
    salt: "",
    sodium: "",
  });

  const [shapData, setShapData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [grade, setGrade] = useState(null);
  const [error, setError] = useState("");


  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleReset = () => {
    setForm({
      energy_kcal: "",
      fat: "",
      saturated_fat: "",
      carbohydrates: "",
      sugars: "",
      proteins: "",
      fiber: "",
      salt: "",
      sodium: "",
    });

    setGrade(null);
    setShapData([]);
    setError("");
  };

  const handlePredict = async () => {
  try {
    setLoading(true);
    setError("");

    // ✅ Step 6 starts here

    const payload = {
      energy_kcal: parseFloat(form.energy_kcal),
      fat: parseFloat(form.fat),
      saturated_fat: parseFloat(form.saturated_fat),
      carbohydrates: parseFloat(form.carbohydrates),
      sugars: parseFloat(form.sugars),
      proteins: parseFloat(form.proteins),
      fiber: parseFloat(form.fiber),
      salt: parseFloat(form.salt),
      sodium: parseFloat(form.sodium),
    };

    // Optional validation
    if (Object.values(payload).some(value => isNaN(value))) {
      setError("Please enter valid values for all fields.");
      setLoading(false);
      return;
    }

    // API Call
    const res = await predictNutriScore(payload);

    console.log("API Response:", JSON.stringify(res, null, 2));
    console.log("Predicted Grade:", res.predicted_grade);

    setGrade(res.predicted_grade);
    setShapData(res.shap || []);

  } catch (err) {
    setError("Prediction failed.");
    console.error(err);
  } finally {
    setLoading(false);
  }
};

  const info =
    grade && gradeInfo[grade]
      ? gradeInfo[grade]
      : null;

  const maxImpact =
  shapData.length > 0
    ? Math.max(...shapData.map((item) => item.abs_impact))
    : 1;

  return (
    <div className="prediction-page">

      <div className="prediction-container">

        {/* LEFT PANEL */}

        <div className="prediction-form">

          <h2>Nutrition Information</h2>

          {Object.keys(form).map((key) => (
            <div className="input-group" key={key}>
              <label>
                {key.replaceAll("_", " ").toUpperCase()}
              </label>

              <input
                type="number"
                name={key}
                value={form[key]}
                onChange={handleChange}
              />
            </div>
          ))}

          <div className="button-group">

            <button
              className="predict-btn"
              onClick={handlePredict}
            >
              {loading ? "Predicting..." : "Predict"}
            </button>

            <button
              className="reset-btn"
              onClick={handleReset}
            >
              Reset
            </button>

          </div>

        </div>

        {/* RIGHT PANEL */}

        <div className="prediction-result">

          {!grade && (
            <div className="empty-card">

              <h2>Prediction Result</h2>

              <p>
                Enter nutritional values and click Predict.
              </p>

            </div>
          )}

          {info && (

            <div
              className="result-card"
              style={{
                borderColor: info.color,
              }}
            >

              <div
                className="grade-circle"
                style={{
                  background: info.color,
                }}
              >
                {grade}
              </div>

              <h2
                style={{
                  color: info.color,
                }}
              >
                {info.title}
              </h2>

              <p>{info.description}</p>

              <hr />

              <hr />

              <h3>Why this prediction?</h3>

              {shapData.length > 0 ? (

                <div className="shap-card">

                  {shapData.map((item, index) => (

                    <div
                      key={index}
                      className="shap-item"
                    >

                      <div className="shap-header">

                        <span>

                          {item.direction === "positive"
                            ? "🟢"
                            : "🔴"}

                          {" "}

                          {item.feature}

                        </span>

                        <span>

                          {item.impact > 0 ? "+" : ""}

                          {item.impact}

                        </span>

                      </div>

                      <div className="bar-bg">

                        <div

                          className={`bar ${item.direction}`}

                          style={{

                            width: `${(item.abs_impact / maxImpact) * 100}%`

                          }}

                        />

                      </div>

                    </div>

                  ))}

                </div>

              ) : (

                <p>No SHAP explanation available.</p>

              )}

              <h3>Recommendation</h3>

              <p>{info.recommendation}</p>

            </div>

          )}

          {error && (
            <p className="error">
              {error}
            </p>
          )}

        </div>

      </div>

    </div>
  );
}