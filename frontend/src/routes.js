import { BrowserRouter, Route, Switch } from 'react-router-dom'
import React from 'react'
import LoginPage from './containers/LoginPage'

export default class Main extends React.Component {
	constructor(){
		super();

        var today = new Date(),
            date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate() + ' ' + today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds();

		this.state = {
			users: {
				user_id			    : 1,
				user_email		    : '',
				user_username	    : '',
				user_password	    : '',
				user_profile_pict   : '',
				user_first_name	    : '',
				user_last_name		: '',
				user_friends	    : 0,
				user_is_activated	: 0,
				user_created_at	    : date,
				user_updated_at	    : date
			},
			url: {
				site: 'http://192.168.0.11:5000',
				route: { 
					login_page	: '/',
				},
			} 
		};
	}


   render() {
	return (
		<div>
			<BrowserRouter>
			<Switch>
				{
					<Route exact path={this.state.url.route.login_page}>
						<LoginPage 
                            user	= {this.state.users}
                            url		= {this.state.url}
                        />
					</Route>
				}
				{
                    <Route exact path="*">
                        <div>
                            {console.log('Hello World2')}
                        </div>
                    </Route>
				}
			</Switch>
			</BrowserRouter>
		</div>
      )
   }
}
