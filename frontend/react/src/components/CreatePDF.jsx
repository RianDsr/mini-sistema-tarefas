function CreatePDF() {
  const handleCreatePDF = () => {
    console.log("Creating PDF...");
  };

  return (
    <div className="create-pdf">
      <button onClick={handleCreatePDF} className="create-pdf-button">
        Create PDF
      </button>
    </div>
  );
}
export default CreatePDF;
