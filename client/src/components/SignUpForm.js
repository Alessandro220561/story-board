import styled from "styled-components";
import React, { useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";
import { useHistory } from "react-router-dom";

const SignUpForm = ({ setUser }) => {
  const history = useHistory();
  const [errors, setErrors] = useState([]);

  const formSchema = yup.object().shape({
    username: yup.string().required(),
    email: yup.string().email().required(),
  });

  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
    },

    validationSchema: formSchema,
    validateOnBlur: false,
    validateOnChange: false,

    onSubmit: (values) => {
      fetch("/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      })
        .then((r) => r.json())
        .then((userData) => setUser(userData));
    },
  });

  return (
    <Form onSubmit={formik.handleSubmit}>
      <label>Username</label>
      <input
        type="text"
        name="username"
        value={formik.values.username}
        onChange={formik.handleChange}
      />
      <label>Email</label>
      <input
        type="text"
        name="email"
        value={formik.values.email}
        onChane={formik.handleChange}
      />
      <label>Password</label>
      <input
        type="password"
        name="password"
        value={formik.values.password}
        onChange={formik.handleChange}
      />
      <input type="submit" value={"Sign Up"} />
    </Form>
  );
};

export default SignUpForm;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  width: 300px;
  margin: auto;
  font-family: arial;
  font-size: 20px;
  input[type="submit"] {
    background-color: pink;
    color: black;
    height: 40px;
    font-family: Arial;
    font-size: 30px;
    margin-top: 10px;
    margin-bottom: 10px;
  }
`;
