import React from 'react';

const CharacterTile = (props) => {
    const { character } = props;
    return (
        <div class="movie-short-line-entity">
            <a class="entity-preview" href="movie-info-sidebar-right.html">
                <span class="embed-responsive embed-responsive-16by9">
                    <img class="embed-responsive-item" src="http://via.placeholder.com/1920x1080" alt="" />
                </span>
            </a>
            <div class="entity-content">
                <h4 class="entity-title">
                    <span class="content-link" >{character.actor.name}</span>
                </h4>
                <p class="entity-subtext">{character.name}</p>
            </div>
        </div>
    );
}

export default CharacterTile;
