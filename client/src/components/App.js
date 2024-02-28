import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

function App() {
  const [users, setUsers] = useState([]);
  const [books, setBooks] = useState([]);

  useEffect(() => {
    getUsers();
    getBooks();
  }, []);

  const getUsers = () => {
    fetch("/users")
      .then((r) => r.json())
      .then((usersData) => setUsers(usersData));
  };

  const getBooks = () => {
    fetch("/books")
      .then((r) => r.json())
      .then((bookData) => setBooks(bookData));
  };

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.username} - {user.email}
          </li>
        ))}
        <h1>Books</h1>
        <ul>
          {books.map((book) => (
            <li key={book.id}>
              <h4>{book.title}</h4>
              <ul>
                <li>{book.author}</li>
                <li>{book.genre}</li>
                <li>{book.pages}</li>
              </ul>
            </li>
          ))}
        </ul>
      </ul>
    </div>
  );
}

export default App;
