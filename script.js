async function generate() {
  let idea = document.getElementById("idea").value;

  if (!idea) {
    alert("Enter idea!");
    return;
  }

  document.getElementById("output").innerHTML = "⚡ Processing...";

  let res = await fetch("/generate", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({idea})
  });

  let data = await res.json();

  document.getElementById("output").innerHTML = `
    <div class="card"><h3>🔍 Research</h3><p>${data.research}</p></div>
    <div class="card"><h3>🏗 Project</h3><p>${data.project}</p></div>
    <div class="card"><h3>🎓 Learning</h3><p>${data.learning}</p></div>
    <div class="card"><h3>🎨 Content</h3><p>${data.content}</p></div>
  `;
}