import React from 'react';
import Item from './Item';

const ItemsList = (props) => {
    return <>
        {
            props.items.map((item) => {
                return <Item id={item.id} 
                            key={item.id}
                            title={item.title} 
                            description={item.description} 
                            url={item.url}
                            thumbnail={item.thumbnail} />
            })
        }
    </>
}

export default ItemsList;