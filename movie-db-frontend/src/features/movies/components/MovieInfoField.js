import React from 'react'

export default function MovieInfoField(props) {
    return (
        <li className="text-capitalize">
            <span className="entity-list-title ">{props.fieldName}:</span>{props.fieldValue}
            {props.children}
        </li>
    )
}
