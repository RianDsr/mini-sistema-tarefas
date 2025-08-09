import "./App.css";
import AddTasks from "./components/AddTasks";
import CreatePDF from "./components/CreatePDF";
import Footer from "./components/Footer";
import Header from "./components/Header";
import TasksList from "./components/TasksList";

function App() {
  const tasks = [
    {
      id: 1,
      name: "Estudar React",
      description: "Hooks e componentes",
      date: "2025-08-10",
    },
    {
      id: 2,
      name: "Fazer exercício",
      description: "Corrida de 5km",
      date: "2025-08-11",
    },
  ];

  return (
    <>
      <body>
        <div className="App">
          <Header />
          <div className="main-layout">
            <AddTasks />
            <TasksList tasks={tasks} />
          </div>
          <div className="create-pdf-container">
            <CreatePDF />
          </div>
          <Footer />
        </div>
      </body>
    </>
  );
}

export default App;
