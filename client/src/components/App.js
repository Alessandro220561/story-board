import React, { useEffect, useState } from "react";
import { createGlobalStyle, styled } from "styled-components";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import LoginForm from "./LoginForm";
import Authorization from "./AuthorizationPage";
import SignUpForm from "./SignUpForm";

function App() {
  const [user, setUser] = useState({});

  // useEffect(() => {
  //   getUser();
  // }, []);

  // const getUser = () => {
  //   fetch("/auth")
  //     .then((r) => r.json())
  //     .then((userData) => setUser(userData));
  // };

  if (Object.keys(user).length === 0)
    return (
      <>
        <Header>Welcome to Story Board</Header>
        <Prompt>Signup or Login to track your reading experience</Prompt>
        <Authorization />
      </>
    );

  return (
    <>
      <GlobalStyle />
      <Router>
        <Switch>
          <Route path="/login">
            <LoginForm setUser={setUser} />
          </Route>
          <Route path="/authorization">
            <Authorization />
          </Route>
          <Route path="/signup">
            <SignUpForm setUser={setUser} />
          </Route>
        </Switch>
      </Router>
    </>
  );
}

export default App;

const GlobalStyle = createGlobalStyle`
    body{
      background-color: black; 
      color:white;
    }
    `;

const Header = styled.h1`
  font-size: 350%;
  font-family: arial;
  color: white;
`;

const Prompt = styled.h2`
  padding-bottom: 50px;
  color: red;
`;
