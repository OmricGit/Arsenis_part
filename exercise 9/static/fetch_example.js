function get_user(num){
    console.log("clicked");
    fetch(`https://reqres.in/api/users/${num}`).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data){
    const curry_main = document.querySelector("mainassignment11");
    const section = document.createElement('section');
    section.innerHTML = `
        <img src="${response_obj_data.avatar}" alt="profile pic"/>
        <div>
            <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
            <br>
            <a href="mailto:${response_obj_data.email}">send email</a>
        </div>
        `;
    curry_main.appendChild(section);
}