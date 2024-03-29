// import React from "react";
// import App from "./components/App";
// import { createRoot } from "react-dom/client";

// const container = document.getElementById("root");
// const root = createRoot(container);
// root.render(<App />);

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./components/App";
import { BrowserRouter } from "react-router-dom";
import { configureStore } from "@reduxjs/toolkit";
import { Provider } from "react-redux";
import userReducer from "./slices/userSlice";

const store = configureStore({
  reducer: {
    user: userReducer,
  },
});

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </React.StrictMode>
);

// import React from "react";
// import ReactDOM from "react-dom/client";
// import App from "./components/App";
// import { BrowserRouter } from "react-router-dom";
// import { configureStore } from "@reduxjs/toolkit";
// import { Provider } from "react-redux";
// import userReducer from "./slices/userSlice";

// const store = configureStore({
//   reducer: {
//     user: userReducer,
//   },
// });

// ReactDOM.createRoot(document.getElementById("root")).render(
//   <React.StrictMode>
//     <Provider store={store}>
//       <BrowserRouter>
//         <App />
//       </BrowserRouter>
//     </Provider>
//   </React.StrictMode>
// );
