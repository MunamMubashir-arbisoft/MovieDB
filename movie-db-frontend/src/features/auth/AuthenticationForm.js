import React from 'react';
import AuthInfo from './components/AuthInfo'
import { reduxForm } from 'redux-form'

const validate = values => {
    const errors = {}
    if (!values.username) {
        errors.username = 'Required'
    } else if (values.username.length < 4) {
        errors.username = 'username must be at least 4 characters'
    }
    if (!values.password) {
        errors.password = 'Required'
    } else if (values.password.length < 8) {
        errors.password = 'password must be at least 8 characters'
    }

    return errors
}

let AuthenicationForm = (props) => {
    const { handleSubmit, error } = props;
    return (

        <div className="gmap-form bg-white container d-flex justify-content-center text-center">
            <div>
                <h4 className="form-title text-uppercase">Welcome to
                <span className="text-theme"> MovieDB</span>
                </h4>
                <form onSubmit={handleSubmit}>
                    <div className="row form-grid">
                        <AuthInfo buttonText={props.buttonText} error={error}/>
                    </div>
                </form>
            </div>
        </div>
    );
}

AuthenicationForm = reduxForm({
    form: 'login',
    validate,
})(AuthenicationForm)

export default AuthenicationForm;
