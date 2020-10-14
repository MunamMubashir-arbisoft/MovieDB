import React from 'react';
import MovieInfoField from './MovieInfoField'

const MovieDescription = (props) => {
    return (
        <ul class="entity-list">
            <MovieInfoField fieldName="Directed" fieldValue={props.director[0].name}/>
            <MovieInfoField fieldName="Language" fieldValue={props.language}/>
            <MovieInfoField fieldName="Genre" fieldValue={props.genre.name} />
        </ul>
    );
}

export default MovieDescription;
