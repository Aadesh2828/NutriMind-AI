import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

/* ===========================
   PRODUCTS API
=========================== */

export const getProducts = async (limit = 20) => {
  const response = await API.get("/products/", {
    params: {
      limit,
    },
  });

  return response.data;
};

export const searchProducts = async (query, limit = 20) => {
  const response = await API.get("/products/search", {
    params: {
      query,
      limit,
    },
  });

  return response.data;
};

export const getProduct = async (productId) => {
  const response = await API.get(`/products/${productId}`);
  return response.data;
};

/* ===========================
   PREDICTION API
=========================== */

export const predictNutriScore = async (data) => {
  const response = await API.post("/api/predict", data);
  return response.data;
};

// =====================================
// Nutri AI Assistant
// =====================================

export const askNutri = async (question) => {
  const response = await API.post("/chatbot/chat", {
    question: question,
  });

  return response.data;
};