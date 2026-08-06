import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import { getProduct } from "../services/api";


function ProductDetails() {

  const { productId } = useParams();

  const navigate = useNavigate();

  const [product, setProduct] = useState(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");


  useEffect(() => {

    loadProduct();

  }, [productId]);


  const loadProduct = async () => {

    try {

      setLoading(true);

      const data =
        await getProduct(productId);

      setProduct(data);

      setError("");

    } catch (err) {

      console.error(err);

      setError(
        "Unable to load product details."
      );

    } finally {

      setLoading(false);

    }

  };


  if (loading) {

    return (

      <div className="details-page">

        <h2>
          Loading product details...
        </h2>

      </div>

    );

  }


  if (error) {

    return (

      <div className="details-page">

        <h2>
          {error}
        </h2>

        <button
          onClick={() =>
            navigate("/products")
          }
        >
          Back to Products
        </button>

      </div>

    );

  }


  if (!product) {

    return (

      <div className="details-page">

        <h2>
          Product not found.
        </h2>

      </div>

    );

  }


  return (

    <div className="details-page">

      <button
        className="back-button"
        onClick={() =>
          navigate("/products")
        }
      >
        ← Back to Products
      </button>


      <div className="product-details-header">

        <h1>
          {product.product_name ||
            "Unnamed Product"}
        </h1>

        <div className="nutriscore-badge">

          Nutri-Score:{" "}

          <strong>

            {product.nutriscore_grade
              ?.toUpperCase() || "N/A"}

          </strong>

        </div>

      </div>


      <div className="details-grid">


        <div className="details-card">

          <h2>
            🥗 Product Information
          </h2>


          <div className="detail-row">

            <span>
              Product Code
            </span>

            <strong>
              {product.product_code ||
                "N/A"}
            </strong>

          </div>


          <div className="detail-row">

            <span>
              Categories
            </span>

            <strong>
              {product.categories ||
                "N/A"}
            </strong>

          </div>


          <div className="detail-row">

            <span>
              Countries
            </span>

            <strong>
              {product.countries ||
                "N/A"}
            </strong>

          </div>


          <div className="detail-row">

            <span>
              Nutri-Score Grade
            </span>

            <strong>
              {product.nutriscore_grade
                ?.toUpperCase() ||
                "N/A"}
            </strong>

          </div>


          <div className="detail-row">

            <span>
              Nutri-Score Score
            </span>

            <strong>
              {product.nutriscore_score ??
                "N/A"}
            </strong>

          </div>


          <div className="detail-row">

            <span>
              NOVA Group
            </span>

            <strong>
              {product.nova_group ??
                "N/A"}
            </strong>

          </div>

        </div>


        <div className="details-card">

          <h2>
            📊 Nutritional Information
          </h2>


          <div className="nutrition-grid">


            <div className="nutrition-item">

              <span>
                Energy
              </span>

              <strong>
                {product.energy_kcal ??
                  "N/A"}{" "}

                {product.energy_kcal &&
                  "kcal"}

              </strong>

            </div>


            <div className="nutrition-item">

              <span>
                Fat
              </span>

              <strong>
                {product.fat ??
                  "N/A"} g
              </strong>

            </div>


            <div className="nutrition-item">

              <span>
                Saturated Fat
              </span>

              <strong>
                {product.saturated_fat ??
                  "N/A"} g
              </strong>

            </div>


            <div className="nutrition-item">

              <span>
                Carbohydrates
              </span>

              <strong>
                {product.carbohydrates ??
                  "N/A"} g
              </strong>

            </div>


            <div className="nutrition-item">

              <span>
                Sugars
              </span>

              <strong>
                {product.sugars ??
                  "N/A"} g
              </strong>

            </div>


            <div className="nutrition-item">

              <span>
                Proteins
              </span>

              <strong>
                {product.proteins ??
                  "N/A"} g
              </strong>

            </div>


            <div className="nutrition-item">

              <span>
                Fiber
              </span>

              <strong>
                {product.fiber ??
                  "N/A"} g
              </strong>

            </div>


            <div className="nutrition-item">

              <span>
                Salt
              </span>

              <strong>
                {product.salt ??
                  "N/A"} g
              </strong>

            </div>


            <div className="nutrition-item">

              <span>
                Sodium
              </span>

              <strong>
                {product.sodium ??
                  "N/A"} mg
              </strong>

            </div>


          </div>

        </div>


      </div>

    </div>

  );

}


export default ProductDetails;