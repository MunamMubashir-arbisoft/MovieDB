import React from 'react';

const MovieHeader = (props) => {
    return (
        <>
            <h4 className="entity-title">
                <span className="content-link">{props.title}</span>
            </h4>
            <div className="entity-category">
                <span className="content-link">{props.genre.name}</span>
            </div>
            <div className="entity-info">
                <div className="info-lines">
                    <div className="info info-short">
                        <span className="text-theme info-icon"><i className="fas fa-calendar"></i></span>
                        <span className="info-text">{props.release_date}</span>
                    </div>
                    <div className="info info-short">
                        <span className="text-theme info-icon"><i className="fas fa-clock"></i></span>
                        <span className="info-text">{props.runtime}</span>
                        <span className="info-rest">&nbsp;min</span>
                    </div>
                </div>
            </div>
        </>
    );
}

export default MovieHeader;
