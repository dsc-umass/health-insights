import React, { Component } from 'react';
import SearchAutoComplete from './SearchAutoComplete';
import './SearchBar.css';

class SearchBar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            query: "",
            typing: false
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(e) {
        this.setState({[e.target.name]: e.target.value, typing: true});
    }

    handleSubmit(e) {
        e.preventDefault();
        this.setState({typing: false, query: ""});
    }

    render() {
        return (
            <div className="search">
                <div className="search-bar">
                    <input 
                        className={this.state.typing ? "search-on" : "search-off"}
                        type="search" 
                        placeholder="Search here..." 
                        id="query"
                        name="query"
                        value={this.state.query} 
                        onChange={this.handleChange}/>
                    <button 
                        type="submit" 
                        className={this.state.typing ? "search-btn-on" : "search-btn-off"}
                        onClick={this.handleSubmit}>
                        <i className="fas fa-search"></i>
                    </button>
                </div>
                <SearchAutoComplete typing={this.state.typing}/>
            </div>
            
        )
    }
}

export default SearchBar;