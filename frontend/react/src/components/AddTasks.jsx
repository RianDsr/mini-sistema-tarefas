import { useState } from "react";
import axios from "axios";

function AddTasks() {
  const [taskName, setTaskName] = useState("");
  const [taskDescription, setTaskDescription] = useState("");
  const [taskDate, setTaskDate] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://127.0.0.1:5000/tarefas", {
        name: taskName,
        description: taskDescription,
        date: taskDate,
      });
      setTaskName("");
      setTaskDescription("");
      setTaskDate("");
      alert("Tarefa adicionada com sucesso!");
    } catch (error) {
      console.error("Erro ao adicionar tarefa:", error);
    }
  };

  return (
    <div className="Bloco">
      <h2 className="HeaderText">Add Tasks Component</h2>
      <form className="HeaderText" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Task Name"
          value={taskName}
          onChange={(e) => setTaskName(e.target.value)}
          required
        />
        <br />
        <input
          type="text"
          placeholder="Task Description"
          value={taskDescription}
          onChange={(e) => setTaskDescription(e.target.value)}
          required
        />
        <input
          type="date"
          placeholder="Task Description"
          value={taskDate}
          onChange={(e) => setTaskDate(e.target.value)}
          required
        />
        <br />
        <button type="submit">Add Task</button>
      </form>
    </div>
  );
}

export default AddTasks;
