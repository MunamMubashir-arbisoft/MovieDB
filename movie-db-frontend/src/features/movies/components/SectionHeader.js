import React from 'react';

const SectionHeader = (props) => {
    return (
        <div className="section-head">
            <h2 className="section-title text-uppercase">{props.sectionTitle}</h2>
        </div>
    );
}

export default SectionHeader;
