import { BrowserRouter, Route, Switch } from 'react-router-dom'
import React from 'react'

import LoginPage from './containers/LoginPage'
import BoardPage from './containers/BoardPage'
import ProfilePage from './containers/ProfilePage'

export default class Main extends React.Component {
	constructor(){
		super();

        var today = new Date(),
            date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate() + ' ' + today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds();

		this.state = {
			user: {
				id			    : 1,
				email		    : '',
				username	    : '',
				password	    : '',
				profile_pict   : '',
				name	    	: '',
				friends	    : 0,
				is_activated	: 0,
				created_at	    : date,
				updated_at	    : date
			},
			notebook:{
				id 					: null,
				name 				: '',
				paper 				: [],				
			},
			paper:{
				id 					: null,
				text				: '',
			},
			url: {
				site: 'http://localhost:5000',
				// site: 'http://192.168.0.11:5000',
				frontendRoute: {
					login_page		: '/',
					signup_page		: '/signup',
					board_page		: '/board',
					profile_page	: '/account/:id',
					friendlist_page	: '/friendlist',
					note_page		: '/note',
				},
				backendRoute: {
					version		: '/v1',
					admin		: '/admin',
					notebook	: '/notebook',
					paper		: '/paper',
					user		: '/user',
					violation	: '/violation',
				},
			},
			color: {
				cream: '#FFFCC9',
				brown: '#C2A060',
			}
		};
	}


   render() {
	return (
		<div>
			<BrowserRouter>
			<Switch>
				{
					<Route exact path={this.state.url.frontendRoute.login_page}>
						<LoginPage 
                            user	= {this.state.users}
                            url		= {this.state.url}
                        />
					</Route>
				}
				{
					<Route exact path={this.state.url.frontendRoute.board_page}>
						<BoardPage 
                            color	= {this.state.color}
                            user	= {this.state.users}
                            url		= {this.state.url}
                        />
					</Route>
				}
				{
					<Route exact path={this.state.url.frontendRoute.profile_page}>
						<ProfilePage 
                            color	= {this.state.color}
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
