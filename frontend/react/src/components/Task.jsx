function Task({ name, description, date }) {
  return (
    <div>
      <h3>Name:{name}</h3>
      <p>Description:{description}</p>
      <small>Date:{date}</small>
    </div>
  );
}
export default Task;
