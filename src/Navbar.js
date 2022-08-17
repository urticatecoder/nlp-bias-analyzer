import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
//import { handleInputChange } from 'react-select/dist/declarations/src/utils';
import './index.css';
//import cnnLinks from './cnn-links.json'


function Navbar(props) {
    const [desiredCategory, setCategory] = useState('politics');

    const categories = [
        { value: 'politics', label: 'Politics' },
        { value: 'business', label: 'Business' },
        { value: 'sports', label: 'Sports' },
        { value: 'entertainment', label: 'Entertainment' }
    ];

    function handleChange(e) {
        setCategory(e.target.value);
        console.log(desiredCategory);
    }


    return (<div>
        <button class='navbarButon' id='homeButton'>Home</button>
        <select 
        defaultValue={desiredCategory} 
        id='categorySelector' 
        onChange={handleChange}>
            <option value='politics'>Politics</option>
            <option value='business'>Business</option>
            <option value='sports'>Sports</option>
            <option value='entertainment'>Entertainment</option>        
        
        </select>

        <button class='navbarButton'> Filler</button>
        <button class='navbarButton'> Filler</button>
        <button class='navbarButton'> Filler</button>

    </div>);
};


export default Navbar;
