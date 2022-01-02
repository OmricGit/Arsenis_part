function put_users_inside_html(response_obj){
    const curr_main = document.querySelector(selectors:"main");
    for (let user of response_obj) {
        const selection = document.createElement(tagName: 'section');
        <img src={"${user.avatar}" alt="Profile Picture"/>
            <div>
            <span>${user.firstname} ${user.lastname}</span>
            <br>
            <a href="mailto:${user.email}">Send Mail</a>
            </div>
            ;
            curr_main.appendChild(section);
        }
        }
    }
}