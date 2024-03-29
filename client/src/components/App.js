import React, { useEffect, useState } from "react";
import { createGlobalStyle, styled } from "styled-components";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import LoginForm from "./LoginForm";
import Authorization from "./AuthorizationPage";
import SignUpForm from "./SignUpForm";
import { useHistory } from "react-router-dom";
import { useDispatch } from "react-redux";
import { setUser } from "../slices/userSlice";
import { useSelector } from "react-redux";

function App() {
  const history = useHistory();
  const dispatch = useDispatch();
  // const [user, setUser] = useState({});
  const user = useSelector((state) => state.user.value);

  useEffect(() => {
    getUser();
  }, []);

  const getUser = () => {
    fetch("/auth")
      .then((r) => r.json())
      .then((userObj) => dispatch(setUser(userObj)));
  };

  if (!user)
    return (
      <>
        <Header>Welcome to Story Board</Header>
        <Prompt>Signup or Login to track your reading experience</Prompt>
        <Authorization />
      </>
    );

  const newUser = (newUserData) => {
    setUser([...user, newUserData]);
    history.push("/login");
  };

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
            <SignUpForm newUser={newUser} />
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
