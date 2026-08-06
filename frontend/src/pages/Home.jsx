import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Home() {

  const navigate =
    useNavigate();

  const [searchTerm, setSearchTerm] = useState("");

  const handleSearch = () => {

    if (!searchTerm.trim()) {
      navigate("/products");
      return;
    }

    navigate("/products", {
      state: {
        search: searchTerm
      }
    });

  };


  return (

    <div className="home-page">

      <section className="hero">

        <h1>
          Make Smarter
          <br />

          <span>
            Food Choices
          </span>
        </h1>


        <p>

          NutriMind AI helps you understand
          the nutritional quality of food,
          predict Nutri-Score, and discover
          healthier alternatives.

        </p>


        <div className="hero-search">

          <input
              type="text"
              placeholder="Search a food product..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              onKeyDown={(e) => {
                  if (e.key === "Enter") {
                      handleSearch();
                  }
              }}
          />

          <button
            onClick={handleSearch}
          >

            Search

          </button>

        </div>

      </section>


      <section
        className="features-section"
      >

        <div className="section-title">

          <h2>
            Everything You Need
          </h2>

          <p>
            Explore the intelligence
            behind your food choices.
          </p>

        </div>


        <div className="features">


          <div className="feature-card">

            <div className="feature-icon">
              🔍
            </div>

            <h3>
              Product Search
            </h3>

            <p>

              Search thousands of food
              products and explore their
              nutritional information.

            </p>

          </div>


          <div className="feature-card">

            <div className="feature-icon">
              🧠
            </div>

            <h3>
              AI Prediction
            </h3>

            <p>

              Predict the Nutri-Score
              of food products using
              Machine Learning.

            </p>

          </div>


          <div className="feature-card">

            <div className="feature-icon">
              🤖
            </div>

            <h3>
              AI Nutrition Assistant
            </h3>

            <p>

              Ask questions and get
              intelligent answers using
              RAG and Generative AI.

            </p>

          </div>


          <div className="feature-card">

            <div className="feature-icon">
              📊
            </div>

            <h3>
              Nutrition Insights
            </h3>

            <p>

              Explore nutritional trends
              and insights through
              interactive visualizations.

            </p>

          </div>


        </div>

      </section>

    </div>

  );

}


export default Home;