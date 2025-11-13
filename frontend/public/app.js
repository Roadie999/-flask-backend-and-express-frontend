const API_BASE = 'http://localhost:5000/api'; // Flask backend


async function fetchHello() {
const res = await fetch(`${API_BASE}/hello`);
const j = await res.json();
document.getElementById('hello').textContent = j.message;
}


async function loadTodos() {
const res = await fetch(`${API_BASE}/todos`);
const todos = await res.json();
const ul = document.getElementById('todos');
ul.innerHTML = '';
todos.forEach(t => {
const li = document.createElement('li');
li.textContent = `${t.id}: ${t.task} ${t.done ? '(done)' : ''}`;
li.style.cursor = 'pointer';
li.onclick = async () => {
await fetch(`${API_BASE}/todos/${t.id}`, {
method: 'PATCH',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ done: !t.done })
});
loadTodos();
}
ul.appendChild(li);
});
}


document.getElementById('addForm').addEventListener('submit', async (e) => {
e.preventDefault();
const task = document.getElementById('taskInput').value.trim();
if (!task) return;
await fetch(`${API_BASE}/todos`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ task })
});
document.getElementById('taskInput').value = '';
loadTodos();
});


// Init
fetchHello();
loadTodos();