import Task from "./Task";

function TasksList({ tasks }) {
  return (
    <div>
      <h2>Tasks list</h2>
      {tasks.map((task) => (
        <Task
          key={task.id}
          name={task.name}
          description={task.description}
          date={task.date}
        />
      ))}
    </div>
  );
}

export default TasksList;
