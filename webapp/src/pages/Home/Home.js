import './Home.css';
import SearchBar from './SearchBar';

function Home() {
  return (
    <div className="Home">
      <header className="Home-header">
        <SearchBar />
      </header>
    </div>
  );
}

export default Home;
