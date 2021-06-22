const editShow = document.querySelector('.edit')
const editForm = document.querySelector('.edit-details-form')
const details = document.querySelector('.details')

editShow.onclick = () => {
    details.style.display = 'none'
    editForm.style.display = 'block'
}
