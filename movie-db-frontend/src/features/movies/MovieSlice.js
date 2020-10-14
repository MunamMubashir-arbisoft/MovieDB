import { createSlice } from '@reduxjs/toolkit'
import axios from 'axios';

export const movie = createSlice({
    name: 'movie',
    initialState: {
        movies: {
            isFetching: false,
            didInvalidate: false,
            items: [],
            lastUpdated: 0
        },
        selectedMovie: null,
    },
    reducers: {
        sendFetchRequest: (state) => {
            state.movies.isFetching = true;
            state.movies.didInvalidate = false;
        },
        invalidateFetchRequest: (state) => {
            state.movies.didInvalidate = true;
        },
        receiveFetchedMovies: (state, action) => {
            state.movies.isFetching = false;
            state.movies.didInvalidate = false;
            state.movies.items = action.payload.movieItems;
            state.movies.lastUpdated = action.payload.receivedAt;
        }
        ,
        selectMovie: (state, action) => {
            console.log(action)
            state.selectedMovie = action.payload
        }
    },

})

const { sendFetchRequest, receiveFetchedMovies, selectMovie } = movie.actions;


function fetchMovies() {
    return dispatch => {
        dispatch(sendFetchRequest())
        return axios.get('http://127.0.0.1:8000/api/movies/')
            .then(response => {
                dispatch(receiveFetchedMovies({ receivedAt: Date.now(), movieItems: response.data }))
            })
    }
}


function shouldFetchMovies(state) {
    const movies = state.movie.movies;
    console.log(movies)
    if (!movies.items.length) {
        return true
    } else if (movies.isFetching) {
        return false
    } else {
        return movies.didInvalidate
    }
}

function fetchMoviesIfNeeded() {
    return (dispatch, getState) => {
        if (shouldFetchMovies(getState())) {
            return dispatch(fetchMovies())
        }
    }
}


function fetchMovie(movieId) {
    return dispatch => {
        dispatch(sendFetchRequest())
        return axios.get(`http://127.0.0.1:8000/api/movies/${movieId}`)
            .then(response => {
                dispatch(selectMovie(response.data))
            })
    }
}


function shouldFetchSpecifiedMovie(state, movieId) {
    const movies = state.movie.movies.items;
    const requiredMovie = movies.filter((movie) => movie.id === movieId);
    console.log("required Movie", requiredMovie)
    if (requiredMovie.length > 1) {
        return requiredMovie[0];
    }
    return null;
}


function fetchMovieByIdIfNeeded(movieId) {
    return (dispatch, getState) => {
        const requiredMovie = shouldFetchSpecifiedMovie(getState(), movieId)
        console.log("required Movie in 2nd:", requiredMovie)
        if (!requiredMovie) {
            return dispatch(fetchMovie(movieId))
        }
    }

}


export const selectMoviesState = (state) => state.movie.movies.items
export const currentMovieState = (state) => state.movie.selectedMovie
export { fetchMoviesIfNeeded, fetchMovieByIdIfNeeded, selectMovie };
export default movie.reducer;