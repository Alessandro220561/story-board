import styled from "styled-components";
import React, { useState } from "react";
import LoginForm from "./LoginForm";
import SignUpForm from "./SignUpForm";

const Authorization = () => {
  const [signedUp, setSignedUp] = useState(true);

  return (
    <>
      {signedUp ? (
        <>
          <LoginForm />
          <StyledButton onClick={() => setSignedUp(false)}>
            Create New Account
          </StyledButton>
        </>
      ) : (
        <>
          <SignUpForm />
          <StyledButton onClick={() => setSignedUp(true)}>
            Back to Login
          </StyledButton>
        </>
      )}
    </>
  );
};

export default Authorization;

const StyledButton = styled.button`
  float: left;
  border-radius: 4px;
  border: 1px solid transparent;
  padding: 0.3em 1em;
  font-size: 1em;
  font-weight: 800;
  font-family: Arial;
  background-color: white;
  cursor: pointer;
  /* Add more styling here based on your design */
`;
