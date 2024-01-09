const url = "https://kj3jc5vpz3eylnbdrw6xhp5tjy0jznva.lambda-url.us-east-1.on.aws/"
const counter = document.querySelector()

async function getViewerCount(){
  fetch(url)
  .then(res => res.json())
  .then(data => console.log(data))
  counter.innerHTML = `Views: ${data}`

}
getViewerCount()
