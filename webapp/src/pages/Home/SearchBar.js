import React, { useState } from 'react';
import Axios from 'axios';
import ItemsList from './ItemsList';
import './SearchBar.css';

const SearchBar = () => {
    const [terms, setTerms] = useState('');
    const [items, setItems] = useState([]);
    const [message, setMessage] = useState('');

    function handleButtonClick(e) {
        setMessage('Buscando...')
        Axios.get(process.env.REACT_APP_API_URL + '/api/search?q=' + encodeURIComponent(terms))
            .then((result) => {
                setItems(result.data);
                setMessage('');
            })
            .catch((error) => {
                setMessage('Hubo un problema de comunicación con el servicio de búsqueda. Por favor inténtelo más tarde.');
            });
    }

    return <>
        <div id="searchbar-container">
            <label htmlFor="searchbar">Buscar un video:</label>
            <input type="text" name="searchbar" id="searchbar"
                onChange={(e) => setTerms(e.target.value)} 
                onKeyUp={(e) => {
                    if (e.key === 'Enter') handleButtonClick();
                }} 
                value={terms} />
            <button onClick={handleButtonClick}>Buscar</button>
            <p className="small">Escribe las palabras que quieras buscar. Para iniciar la búsqueda haz click en el botón Buscar o presiona Enter.</p>
        </div>

        <div>
            {
                message !== '' ? <p>{message}</p> : ''
            }
            <ItemsList items={items} />
        </div>
    </>;
}

export default SearchBar;