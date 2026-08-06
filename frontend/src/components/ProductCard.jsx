function ProductCard({
  product,
  onViewDetails
}) {

  const grade =
    product.nutriscore_grade
      ?.toUpperCase();


  return (

    <div className="product-card">


      <h3>

        {product.product_name ||
          "Unnamed Product"}

      </h3>


      <div className="product-info">


        <div className="info-item">

          <small>
            Nutri-Score
          </small>

          <strong>
            {grade || "N/A"}
          </strong>

        </div>


        <div className="info-item">

          <small>
            Calories
          </small>

          <strong>

            {product.energy_kcal ??
              "N/A"}

            {product.energy_kcal &&
              " kcal"}

          </strong>

        </div>


        <div className="info-item">

          <small>
            Protein
          </small>

          <strong>

            {product.proteins ??
              "N/A"}

            {product.proteins &&
              " g"}

          </strong>

        </div>


        <div className="info-item">

          <small>
            Sugar
          </small>

          <strong>

            {product.sugars ??
              "N/A"}

            {product.sugars &&
              " g"}

          </strong>

        </div>


      </div>


      <button
        onClick={() =>
          onViewDetails(product.id)
        }
      >
        View Nutrition Details
      </button>


    </div>

  );

}


export default ProductCard;