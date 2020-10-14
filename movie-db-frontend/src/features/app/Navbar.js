import React from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { selectAuthState, logOutUser } from '../auth/AuthenticationSlice'
import {
    Link
} from "react-router-dom";

const Navbar = () => {
    const isAuthenticated = useSelector(selectAuthState)
    const dispatch = useDispatch()

    const logInOrOut = !isAuthenticated ? 
    (<div className="navbar-extra">
        <Link to="/login" className="m-2">
            <span className="btn-theme btn"><i className="fas fa-sign-in"></i>&nbsp;&nbsp;Log in</span>
        </Link>
        <Link to="/register">
            <span className="btn-theme btn"><i className="fas fa-plus"></i>&nbsp;&nbsp;Sign up</span>
        </Link>
    </div>) : 
    (<div className="navbar-extra">
        <span className="m-2" onClick={() => {
            dispatch(logOutUser())
        }}>
            <span className="btn-theme btn"><i className="fas fa-sign-out"></i>&nbsp;&nbsp;Log Out</span>
        </span>
    </div>);

    return (
        <header className="header header-horizontal header-view-pannel">
            <div className="container">
                <nav className="navbar">
                    <Link className="navbar-brand" to="./">
                        <span className="logo-element">
                            <span className="logo-tape">
                                <span className="svg-content svg-fill-theme" data-svg="./images/svg/logo-part.svg"></span>
                            </span>
                            <span className="logo-text">
                                <span>M</span>MovieDB</span>
                        </span>
                    </Link>
                    <button className="navbar-toggler" type="button">
                        <span className="th-dots-active-close th-dots th-bars">
                            <span></span>
                            <span></span>
                            <span></span>
                        </span>
                    </button>
                    <div className="navbar-collapse">
                        <ul className="navbar-nav">
                            <Link to="/">
                                <li className="nav-item nav-item-arrow-down nav-hover-show-sub">
                                    <span className="nav-link">Homepage</span>
                                    <div className="nav-arrow"><i className="fas fa-chevron-down"></i></div>
                                </li>
                            </Link>
                        </ul>
                        <ul className="navbar-nav ml-3">
                            <Link to="/movies">
                                <li className="nav-item nav-item-arrow-down nav-hover-show-sub">
                                    <span className="nav-link">Movies</span>
                                    <div className="nav-arrow"><i className="fas fa-chevron-down"></i></div>
                                </li>
                            </Link>
                        </ul>
                        {logInOrOut}
                    </div>
                </nav>
            </div>
        </header>
    );
}

export default Navbar;
