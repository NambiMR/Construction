function addUser() {
    var name = document.getElementById('addName').value;
    var age= document.getElementById('addAge').value;
    var contact= document.getElementById('addContact').value;
    var desgination=document.getElementById('addDesgination')
    var tbody = document.querySelector('tbody');
    var newRow = document.createElement('tr');
    newRow.innerHTML = `
        <th scope="row">${tbody.children.length + 1}</th>
        <td>${name }</td>
        <td>${age}</td>
        <td>${contact }</td>
        <td>${desgination}</td>
        
        <td>
            <button type="button" class="btn btn-success" onclick="openEditModal('${name}', '${age}', '${contact}','${desgination}')" id="edit">Edit</button>
            <button type="button" class="btn btn-danger" id="delete">Delete</button>
        </td>
    `;

    
    tbody.appendChild(newRow); 
    document.getElementById('addUserForm').reset();
}