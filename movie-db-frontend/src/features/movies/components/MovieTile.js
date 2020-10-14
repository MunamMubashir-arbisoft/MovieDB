import React from 'react'
import MoviePoster from './MoviePoster'
import MovieHeader from './MovieHeader'

const MovieTile = (props) => {
    return (
        <article className="movie-line-entity" onClick={() => props.onClickHandler(props.movie)}>
            <MoviePoster
                poster={props.movie.poster_image_url}
            />

            <div className="entity-content">
                <MovieHeader
                    title={props.movie.title}
                    genre={props.movie.genre}
                    runtime={props.movie.runtime}
                    release_date={props.movie.release_date}
                />
                <p className="text-short entity-text">
                    {props.movie.plot}
                </p>
            </div>
        </article>
    )
}


export default MovieTile;
