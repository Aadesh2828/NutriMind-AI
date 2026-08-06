import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";

import {
  getProducts,
  searchProducts,
} from "../services/api";

import ProductCard from "../components/ProductCard";


function Products() {

  const navigate = useNavigate();

  const location = useLocation();

  const [products, setProducts] = useState([]);

  const [query, setQuery] = useState(
      location.state?.search || ""
  );

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");


useEffect(() => {

    if (location.state?.search) {

        handleSearch(location.state.search);

    } else {

        loadProducts();

    }

}, []);


  const loadProducts = async () => {

    try {

      setLoading(true);

      const data = await getProducts(20);

      setProducts(data);

      setError("");

    } catch (err) {

      console.error(err);

      setError(
        "Unable to connect to NutriMind AI API."
      );

    } finally {

      setLoading(false);

    }

  };


  const handleSearch = async (searchValue = query) => {

    if (!searchValue.trim()) {

      loadProducts();

      return;

    }


    try {

      setLoading(true);

      const data = await searchProducts(searchValue);

      setProducts(data);

      setError("");

    } catch (err) {

      console.error(err);

      setError(
        "Search failed. Please try again."
      );

    } finally {

      setLoading(false);

    }

  };


  return (

<div className="products-page">

  <div className="page-header">

    <h1>
      Explore Food Products
    </h1>

    <p>
      Search our nutrition database
      to understand what's in your food.
    </p>

  </div>

      <div className="search-box">

        <input
          type="text"
          placeholder="Search milk, bread, chocolate..."
          value={query}
          onChange={(e) =>
            setQuery(e.target.value)
          }
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


      {loading && (
        <p>Loading products...</p>
      )}


      {error && (
        <p className="error">
          {error}
        </p>
      )}


      {!loading && products.length === 0 && (
        <p>
          No products found.
        </p>
      )}


      <div className="products-grid">

        {products.map((product) => (

        <ProductCard
          key={product.id}
          product={product}
          onViewDetails={(id) =>
            navigate(`/products/${id}`)
          }
        />

        ))}

      </div>

    </div>

  );

}

export default Products;