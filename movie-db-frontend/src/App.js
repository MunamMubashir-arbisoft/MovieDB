import React from 'react';
import { connect } from 'react-redux';
import AuthenicationForm from './features/auth/AuthenticationForm'
import MovieFeed from './features/movies/MovieFeed'
import Navbar from './features/app/Navbar'
import MovieDetail from './features/movies/MovieDetail'
import Home from './features/app/Home'
import { authenticateUser } from './features/auth/AuthenticationSlice'
import { SubmissionError } from 'redux-form'
import {
  Switch,
  Route,
  withRouter
} from "react-router-dom";
import axios from 'axios';

class App extends React.Component {

  handleRegister = (values) => {
    var data = new FormData();
    data.append('username', values.username);
    data.append('password', values.password);
    return axios.post('http://127.0.0.1:8000/users/register/', data)
      .then(response => {
        console.log("User has been created", response)
        this.props.authenticateUser()
        if (this.props.isAuthenticated) {
          this.props.history.push("/movies")
        }
      })
      .catch(error => {
        if (error) {
          throw new SubmissionError({ username: error.response.data.username[0], _error: 'Username already exists.' })
        } else {
          throw new SubmissionError({ _error: 'Username already exists.' })
        }

      });
  }

  handleLogin = (values) => {
    var data = new FormData();
    data.append('username', values.username);
    data.append('password', values.password);
    return axios.post('http://127.0.0.1:8000/users/login/', data)
      .then(response => {
        console.log(response)
        this.props.authenticateUser()
        if (this.props.isAuthenticated) {
          this.props.history.push("/movies")
        }
      })
      .catch(error => {
        if (error.response) {
          throw new SubmissionError({ _error: error.response.data.non_field_errors[0] })
        } else {
          throw new SubmissionError({ _error: 'Username already exists.' })
        }
      });
  }

  render() {
    return (
      <>
        <Navbar />
        <Switch>
          <Route path="/register">
            <AuthenicationForm
              buttonText="Sign Up"
              onSubmit={this.handleRegister}
            />
          </Route>

          <Route path="/login">
            <AuthenicationForm
              buttonText="Log in"
              onSubmit={this.handleLogin}
            />
          </Route>

          <Route path="/movies/:id">
            <MovieDetail />
          </Route>

          <Route path="/movies">
            <MovieFeed />
          </Route>

          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </>
    );
  }
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
});

const mapDispatchToProps = {
  authenticateUser
};


export default withRouter(connect(mapStateToProps, mapDispatchToProps)(App));

