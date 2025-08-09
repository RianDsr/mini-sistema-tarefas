function Task({ name, description, date }) {
  return (
    <div className="Task">
      <h3>{name}</h3>
      <p>{description}</p>
      <small>{date}</small>
    </div>
  );
}

export default Task;
