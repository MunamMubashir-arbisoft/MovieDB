import React from 'react';

const MoviePoster = (props) => {
    return (
        <div className="entity-poster" data-role="hover-wrap">
            <div className="embed-responsive embed-responsive-poster">
                <img className="embed-responsive-item" src={props.poster || "http://via.placeholder.com/340x510"} alt="" />
            </div>
        </div>
    );
}

export default MoviePoster;
