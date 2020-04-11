const imageSrc = document.querySelector('.image img');
const imageForm = document.querySelector('#image-form');
const createImg = document.querySelector('#create-img');

createImg.addEventListener('click', async event => {
  event.preventDefault();

  let formObj = {};

  [...imageForm.elements].forEach(element => {
    formObj[element.name] = element.value;
  });
  delete formObj[''];
  // console.log('image name:', formObj);

  if (!formObj.name) {
    return alert('name field is required!');
  }

  const response = await fetch('http://localhost:5001/api/v1/images/new', {
    method: 'POST',
    headers: {
      'content-type': 'application/json'
    },
    body: JSON.stringify(formObj)
  });

  if (response.ok && response.status === 201) {
    clearForm(imageForm);
    return alert('Image added successfully!');
  }

  return alert('Failed to add image!')
});

const imageItems = document.querySelectorAll('.image-item');
imageItems.forEach(item => {
  item.addEventListener('click', event => {
    event.preventDefault();
    imageForm
      .elements
      .namedItem('name')
      .value = event.target.innerText;
    imageSrc.src = `http://localhost:5001/api/v1/images?image_name=${event.target.innerText}`;
  })
})

function clearForm(form) {
  [...form.elements].forEach(element => {
    element.value = '';
  })
}

document.addEventListener('DOMContentLoaded', event => {
  console.log('>>> Page loaded');
  clearForm(imageForm)
});