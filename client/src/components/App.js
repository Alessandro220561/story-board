import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import LoginForm from "./LoginForm";

function App() {
  const [user, setUser] = useState({});
  return (
    <div>
      <LoginForm setUser={setUser} />
    </div>
  );
}

export default App;
