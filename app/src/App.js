import React from 'react';
import { withAuthenticator } from '@aws-amplify/ui-react'

import { Auth } from 'aws-amplify';
import './App.css';


function App() {

  async function signOut() {
    try {
      await Auth.signOut();
    } catch (error) {
      console.log('error signing out: ', error);
    }
  }

  return (
    <div className="App">
      {/* <header className="App-header">
        <h1>User Management</h1>

      </header> */}

      <button onClick={signOut}>Logout</button>

      {/* <Routes /> */}
    </div>
  );
}

export default withAuthenticator(App);
