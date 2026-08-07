import {
  BrowserRouter,
  Routes,
  Route,
  Link,
} from "react-router-dom";

import Home from "./pages/Home";
import Products from "./pages/Products";
import ProductDetails from "./pages/ProductDetails";
import Prediction from "./pages/Prediction";
import Nutri from "./pages/Nutri";
import Visualization from "./pages/Visualization";


function App() {

  return (

    <BrowserRouter>

<nav className="navbar">

  <Link
    to="/"
    className="logo"
  >
    🥗 Nutri<span>Mind AI</span>
  </Link>


  <div className="nav-links">

    <Link to="/">
      Home
    </Link>

    <Link to="/products">
      Products
    </Link>

    <Link to="/prediction">
      Prediction
    </Link>

    <Link to="/nutri">
      Nutri
    </Link>

    <Link to="/visualization">
      Insights
    </Link>

  </div>

</nav>


      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/products"
          element={<Products />}
        />

        <Route
          path="/products/:productId"
          element={<ProductDetails />}
        />

        <Route
          path="/prediction"
          element={<Prediction />}
        />

        <Route
          path="/nutri"
          element={<Nutri />}
        />

        <Route
          path="/visualization"
          element={<Visualization />}
        />

      </Routes>

    </BrowserRouter>

  );

}

export default App;