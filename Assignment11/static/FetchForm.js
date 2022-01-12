console.log("im inside fatch example")

function get_users(){
    console.log("clicked");
    fetch('https://reqres.in/api/users?page=2').then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data){
    // console.log(response_obj_data);
    const curry_main = document.querySelector("main");
    for (let user of response_obj_data){
        const section = document.createElement('section');
        section.innerHTML = `
            <img src="${user.avatar}" alt="profile pic"/>
            <div>
                <span>${user.first_name} ${user.last_name}</span>
                <br>
                <a href="mailto:${user.email}">send email</a>
            </div>
            `;
        curry_main.appendChild(section);
        }
}

function get_pokemons(num){
    console.log("clicked");

}