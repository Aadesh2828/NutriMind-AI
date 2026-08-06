import { useEffect } from "react";
import "./Visualization.css";

export default function Visualization() {

  useEffect(() => {

    const existingScript = document.getElementById("tableau-script");

    if (!existingScript) {

      const script = document.createElement("script");

      script.id = "tableau-script";

      script.src = "https://public.tableau.com/javascripts/api/viz_v1.js";

      script.async = true;

      document.body.appendChild(script);

    }

  }, []);

  return (

    <div className="visualization-page">

      <div className="visualization-header">

        <h1>Nutrition Analytics Dashboard</h1>

        <p>
          Explore interactive insights from the Open Food Facts dataset
          through Tableau dashboards. Analyze Nutri-Score distribution,
          nutrition trends, product categories, and other key statistics.
        </p>

      </div>

      <div className="dashboard-card">

        <div
          className="tableauPlaceholder"
          id="vizContainer"
        >

          <noscript>

            <a href="#">
              <img
                alt="Dashboard"
                src="https://public.tableau.com/static/images/Nu/Nutri-scoreanalytics/AnalysisofOpenFoodFacts/1_rss.png"
                style={{ border: "none" }}
              />
            </a>

          </noscript>

          <object className="tableauViz">

            <param
              name="host_url"
              value="https%3A%2F%2Fpublic.tableau.com%2F"
            />

            <param
              name="embed_code_version"
              value="3"
            />

            <param
              name="site_root"
              value=""
            />

            <param
              name="name"
              value="Nutri-scoreanalytics/AnalysisofOpenFoodFacts"
            />

            <param
              name="tabs"
              value="no"
            />

            <param
              name="toolbar"
              value="yes"
            />

            <param
              name="device"
              value="desktop"
            />

            <param
              name="showVizHome"
              value="no"
            />

          </object>

        </div>

      </div>

      <div className="dashboard-footer">

        Dashboard Source:
        <strong> Tableau Public</strong>

        <br />

        Dataset:
        <strong> Open Food Facts</strong>

      </div>

    </div>

  );

}