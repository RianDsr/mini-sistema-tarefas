import "./App.css";
import AddTasks from "./components/AddTasks";
import Footer from "./components/Footer";
import Header from "./components/Header";
import TasksList from "./components/TasksList";

function App() {
  return (
    <>
      <body>
        <div className="App">
          <Header />
          <AddTasks />
          <TasksList />
          <Footer />
        </div>
      </body>
    </>
  );
}

export default App;
