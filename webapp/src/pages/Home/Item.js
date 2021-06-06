import React from 'react';
import './Item.css';

const Item = (props) => {
    return <>
        <article id={"video-" + props.id} className="item">
            <div className="item-image">
                <a href={props.url}>
                    <img src={props.thumbnail.url} height={props.thumbnail.height} width={props.thumbnail.width} alt={props.title} />
                </a>
            </div>
            <div className="item-data">
                <h4><a href={props.url}>{props.title}</a></h4>
                <p>{props.description}</p>
            </div>
        </article>
    </>
}

export default Item;