const hindi=document.querySelector('.hindi')
const english=document.querySelector('.english')
const math= document.querySelector('.math')
const physics=document.querySelector('.physics')
const chemistry=document.querySelector('.chemistry')
const submitBtn=document.querySelector('.submitBtn')
const container=document.querySelector('.container')

const deleteData = async (dataID) => {

    const response = await fetch(`http://localhost:3000/posts/${dataID}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    getData()
    return response.json()
}
const displayData = (data) => {
    container.innerHTML = ""
    data.map((item, index) => {
        container.innerHTML += `<tr>
        <td>${item.hindi}</td>
        <td>${item.english}</td>
        <td>${item.math}</td>
        <td>${item.physics}</td>
        <td>${item.chemistry}</td>
        <td><button onclick="deleteData(${item.hindi})">DELETE</button></td>
        </tr>`
    })

}

const getData = async () => {
    const response = await fetch(`http://localhost:3000/posts`)
    const data = await response.json()
    console.log(data)
    displayData(data)
}
getData()

const postData = async () => {
    const data = { "hindi": hindi.value, "english": english.value, "math": math.value ,"physics":physics.value,"chemistry":chemistry.value}
    const response = await fetch(`http://localhost:3000/posts`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    getData()
    return response.json()
}

submitBtn.addEventListener('click', postData)


