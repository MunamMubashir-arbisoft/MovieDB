import React from 'react';
import { Field } from 'redux-form'

const renderField = ({ input, label, placeholder, type, meta: { touched, error, warning } }) => (
    <div>
        <label className="control-label">{label}</label>
        <div>
            <input {...input} placeholder={placeholder} type={type} className="form-control" />
            {touched && ((error && <span className="text-danger">{error}</span>) || (warning && <span>{warning}</span>))}
        </div>
    </div>
)

const AuthInfo = (props) => {
    const { error } = props
    const displayClass = error ? "col-12" : "d-none"
    return (
        <>
            <div className="col-12">
                <div className="input-view-flat input-group d-flex justify-content-center">
                    <Field
                        name="username"
                        type="text"
                        component={renderField}
                        label="Username"
                        placeholder="Type in your username"
                    />
                </div>
            </div>
            <div className="col-12">
                <div className="input-view-flat input-group d-flex justify-content-center">
                    <Field
                        name="password"
                        type="password"
                        component={renderField}
                        label="Password"
                        placeholder="Type in your password"
                    />
                </div>
            </div>
            {props.children}
            <div className={displayClass}>
                <div className="d-flex justify-content-center text-danger">
                    {error && <strong>{error}</strong>}
                </div>
            </div>
            <div className="col-12">
                <button className="px-5 btn btn-theme" type="submit">
                    {props.buttonText}
                </button>
            </div>
        </>
    );
}

export default AuthInfo;
