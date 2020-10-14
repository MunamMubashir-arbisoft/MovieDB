import React, { useEffect } from 'react';
import { selectAuthState } from '../auth/AuthenticationSlice'
import { currentMovieState, fetchMovieByIdIfNeeded } from './MovieSlice'
import { useSelector, useDispatch } from 'react-redux';
import { useParams, useHistory } from "react-router-dom";
import MovieHeader from './components/MovieHeader'
import MoviePoster from './components/MoviePoster'
import SectionHeader from './components/SectionHeader'
import MovieDescription from './components/MovieDescription';
import CharacterTile from './components/CharacterTile'

const MovieDetail = () => {
    const dispatch = useDispatch()
    const { id } = useParams();
    let history = useHistory();

    const isAuthenticated = useSelector(selectAuthState);
    if (!isAuthenticated) {
        history.push("/login")
    }

    const currentMovie = useSelector(currentMovieState)


    useEffect(() => {
        if (!isAuthenticated) {
            history.push("/login")
        }
        dispatch(fetchMovieByIdIfNeeded(id))
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    if (currentMovie) {
        return (
            <div class="container">
                <div class="sidebar-container">
                    <div class="content">
                        <section class="section-long">
                            <div class="section-line">
                                <div class="movie-info-entity">
                                    <MoviePoster poster={currentMovie.poster_image_url} />
                                    <div className="entity-content">
                                        <MovieHeader
                                            title={currentMovie.title}
                                            genre={currentMovie.genre}
                                            runtime={currentMovie.runtime}
                                            release_date={currentMovie.release_date}
                                        />
                                        <MovieDescription
                                            director={currentMovie.director}
                                            characters={currentMovie.characters}
                                            language={currentMovie.language}
                                            genre={currentMovie.genre}
                                        />
                                    </div>
                                </div>
                            </div>
                            <div class="section-line">
                                <SectionHeader sectionTitle="Sypnosis" />
                                <div class="section-description">
                                    <p class="lead">{currentMovie.plot}</p>
                                    <h6 class="text-dark">What the movie is about?</h6>
                                    <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
                                    <h6 class="text-dark">Detailed summary</h6>
                                    <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.</p>
                                    <p>The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.</p>
                                </div>
                            </div>
                        </section>
                    </div>
                    <div class="sidebar section-long order-lg-last">
                        <section class="section-sidebar">
                            <SectionHeader sectionTitle="Starring" />
                            {currentMovie.characters.map(character =>
                                <CharacterTile character={character} />
                            )}
                        </section>
                    </div>
                </div>
            </div>
        )
    }

    return (
        <SectionHeader sectionTitle="Movie not found" />
    )
}

export default MovieDetail;
