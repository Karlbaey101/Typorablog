(async () => {
  const res = await fetch('/blog/index.json');
  const articles = await res.json();

  const ul = document.createElement('ul');
  articles.forEach(({ title, url }) => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = url;
    a.textContent = title;
    li.appendChild(a);
    ul.appendChild(li);
  });

  document.body.appendChild(ul);
})();