import Task from "./Task";

function TasksList({ tasks }) {
  return (
    <div className="tasks-list">
      <h2 className="HeaderText">Tasks list</h2>
      {tasks.map((task) => (
        <Task
          key={task.id}
          name={task.name}
          description={task.description}
        />
      ))}
    </div>
  );
}

export default TasksList;
