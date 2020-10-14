import React, { useEffect } from 'react'
import { selectAuthState } from '../auth/AuthenticationSlice'
import { fetchMoviesIfNeeded, selectMovie, selectMoviesState } from './MovieSlice'
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from "react-router-dom";
import MovieTile from './components/MovieTile'
import SectionHeader from './components/SectionHeader'



const MovieFeed = () => {
    let history = useHistory();
    const dispatch = useDispatch();

    const isAuthenticated = useSelector(selectAuthState);
    if (!isAuthenticated) {
        history.push("/login")
    }

    const moviesList = useSelector(selectMoviesState);

    
    useEffect(() => {
        if (!isAuthenticated) {
            history.push("/login")
        }
        dispatch(fetchMoviesIfNeeded())
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    const movieSelectHandler = (movie) => {
        console.log(movie)
        dispatch(selectMovie(movie));
        history.push(`/movies/${movie.id}`)
    }

    return (
        <section className="section-long">
            <div className="container">
                <SectionHeader sectionTitle="Movies" />
                {moviesList.map(movie =>
                    <MovieTile movie={movie} key={movie.id} onClickHandler={movieSelectHandler}/>
                )}
            </div>
        </section>
    )
}

export default MovieFeed;